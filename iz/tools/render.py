"""Render Impact Zero Reels + carousel from posts/dayNN.json.
Usage: python3 tools/render.py posts/day01.json
Outputs to out/<day>/ : R*.mp4, C*_N.jpg
"""
import json, os, subprocess, sys, textwrap, shutil
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
FONT_B = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
FONT_M = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
W, H = 1080, 1920
CYAN = (95, 208, 255)
RED = (255, 74, 74)
WHITE = (255, 255, 255)

spec = json.load(open(sys.argv[1]))
OUT = os.path.join(ROOT, "out", spec["day"].replace("-", ""))
TMP = os.path.join(OUT, "tmp")
os.makedirs(TMP, exist_ok=True)


def run(cmd):
    print(" ".join(cmd)[:300])
    subprocess.run(cmd, check=True)


# ---------- backdrop ----------
def backdrop(path):
    bg = Image.open(os.path.join(SRC, "keyart_bg.jpg")).convert("RGB")
    bg = bg.resize((W, int(bg.height * W / bg.width)))
    canvas = Image.new("RGB", (W, H), (0, 0, 0))
    canvas.paste(bg, (0, (H - bg.height) // 2))
    canvas = canvas.filter(ImageFilter.GaussianBlur(2))
    canvas = Image.eval(canvas, lambda v: int(v * 0.42))
    canvas.save(path)


# ---------- text cards ----------
def wrap_lines(text, font, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_rich_line(img, y, line, font, default):
    """Draw one line centered; ALL-CAPS words get colored (RED -> red, others -> cyan)."""
    words = line.split(" ")
    widths = [font.getlength(w + " ") for w in words]
    total = sum(widths) - font.getlength(" ")
    x = (W - total) / 2
    glow = Image.new("RGBA", img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    d = ImageDraw.Draw(img)
    for w, ww in zip(words, widths):
        core = w.strip(".,!?:")
        if core.isupper() and len(core) >= 3:
            col = RED if core in ("RED", "ZERO", "ENDS") else CYAN
        else:
            col = default
        gd.text((x, y), w, font=font, fill=col + (160,))
        d.text((x, y), w, font=font, fill=col, stroke_width=6, stroke_fill=(0, 0, 0))
        x += ww
    return glow


def make_card(text, style, zone, path):
    size = {"hook": 78, "answer": 66, "question": 66, "cta": 64}[style]
    font = ImageFont.truetype(FONT_B, size)
    lines = wrap_lines(text, font, 940)
    lh = int(size * 1.22)
    block_h = lh * len(lines)
    cy = {"top": 400, "bottom": 1520}[zone]
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # soft dark plate behind text for readability
    plate = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    pd = ImageDraw.Draw(plate)
    pd.rounded_rectangle([40, cy - block_h // 2 - 40, W - 40, cy + block_h // 2 + 40], radius=40, fill=(0, 0, 0, 120))
    plate = plate.filter(ImageFilter.GaussianBlur(18))
    img.alpha_composite(plate)
    default = CYAN if style == "cta" else WHITE
    y = cy - block_h // 2
    glows = []
    for ln in lines:
        glows.append(draw_rich_line(img, y, ln, font, default))
        y += lh
    for g in glows:
        img.alpha_composite(g.filter(ImageFilter.GaussianBlur(12)))
    # redraw crisp text on top of glow
    y = cy - block_h // 2
    for ln in lines:
        draw_rich_line(img, y, ln, font, default)
        y += lh
    img.save(path)
    return len(lines)


def make_label(path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    f = ImageFont.truetype(FONT_M, 34)
    txt = "IMPACT ZERO   •   OUT NOW ON iPHONE   •   $2.99"
    tw = f.getlength(txt)
    d.rounded_rectangle([(W - tw) / 2 - 30, 1745, (W + tw) / 2 + 30, 1815], radius=35, fill=(0, 0, 0, 150), outline=CYAN + (200,), width=2)
    d.text((W / 2, 1780), txt, font=f, fill=(230, 245, 255), anchor="mm")
    img.save(path)


def overlay_chain(base_label, cards):
    """Build ffmpeg filter for overlaying card PNGs with time windows. Inputs are 1..n after base video 0."""
    parts = []
    last = base_label
    for i, c in enumerate(cards):
        a, b = c["t"]
        parts.append(f"[{last}][{i + 1}:v]overlay=0:0:enable='between(t,{a},{b - 0.02})'[o{i}]")
        last = f"o{i}"
    return ";".join(parts), last


def render_reel(pid, r):
    out_mp4 = os.path.join(OUT, f"{pid}.mp4")
    base = os.path.join(TMP, f"{pid}_base.mp4")
    bgp = os.path.join(TMP, "bg.png")
    if not os.path.exists(bgp):
        backdrop(bgp)
    dur = r["cards"][-1]["t"][1]
    # ----- base composition per reel -----
    if "segments" in r:
        _tot = sum(sg["end"] - sg["start"] for sg in r["segments"])
        if _tot + 0.05 < dur:
            raise SystemExit(f"{pid}: SEGMENTS TOO SHORT ({_tot:.1f}s < {dur}s) - extend segments")
        # generic: list of {src, start, end} from the clean band sources; concatenated, scaled to 1080x540, centred on backdrop
        seg = os.path.join(TMP, f"{pid}_seg.mp4")
        ins, fc, labels = [], [], []
        for i, sg in enumerate(r["segments"]):
            ins += ["-i", os.path.join(SRC, sg["src"] + ".mp4")]
            fc.append(f"[{i}:v]trim={sg['start']}:{sg['end']},setpts=PTS-STARTPTS,scale=1080:-2,crop=1080:540,setsar=1,fps=30[v{i}];"
                      f"[{i}:a]atrim={sg['start']}:{sg['end']},asetpts=PTS-STARTPTS[a{i}]")
            labels.append(f"[v{i}][a{i}]")
        n = len(r["segments"])
        if "audio_bed" in r:
            # silent sources (e.g. v4_bts): video-only concat, audio from a bed clip
            bed = r["audio_bed"]
            ins += ["-i", os.path.join(SRC, bed["src"] + ".mp4")]
            fc = [f.split(";")[0] for f in fc]  # keep only the video parts
            fc.append("".join(l.split("][")[0] + "]" for l in labels) + f"concat=n={n}:v=1:a=0[v]")
            fc.append(f"[{n}:a]atrim={bed['start']}:{bed['start'] + dur},asetpts=PTS-STARTPTS[a]")
        else:
            fc.append("".join(labels) + f"concat=n={n}:v=1:a=1[v][a]")
        run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]",
             "-c:v", "libx264", "-crf", "16", "-c:a", "aac", seg])
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", bgp, "-i", seg, "-filter_complex",
             "[0:v][1:v]overlay=0:690:shortest=1[v]", "-map", "[v]", "-map", "1:a", "-t", str(dur),
             "-r", "30", "-c:v", "libx264", "-crf", "16", "-c:a", "aac", "-af", f"volume={r.get('gain', 1.6)},afade=t=out:st={dur - 1.2}:d=1.2", base])
    elif pid.startswith("R001"):
        # two clean gameplay segments from gp_v5 (skip the old 'co-op' segment)
        seg = os.path.join(TMP, "r1_seg.mp4")
        run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(SRC, "gp_v5.mp4"), "-filter_complex",
             "[0:v]trim=0:13,setpts=PTS-STARTPTS[v0];[0:a]atrim=0:13,asetpts=PTS-STARTPTS[a0];"
             "[0:v]trim=23.5:30.5,setpts=PTS-STARTPTS[v1];[0:a]atrim=23.5:30.5,asetpts=PTS-STARTPTS[a1];"
             "[v0][a0][v1][a1]concat=n=2:v=1:a=1[v][a];[v]scale=1080:540[vc]",
             "-map", "[vc]", "-map", "[a]", "-c:v", "libx264", "-crf", "16", "-c:a", "aac", seg])
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", bgp, "-i", seg, "-filter_complex",
             "[0:v][1:v]overlay=0:690:shortest=1[v]", "-map", "[v]", "-map", "1:a", "-t", str(dur),
             "-r", "30", "-c:v", "libx264", "-crf", "16", "-c:a", "aac", "-af", "volume=1.6", base])
    elif pid.startswith("R002"):
        seg = os.path.join(TMP, "r2_seg.mp4")
        # bts (1080x580) then gp_v1 (1080x542) padded to 1080x600 bands, with gp_v5 audio bed
        run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(SRC, "v4_bts.mp4"), "-i", os.path.join(SRC, "gp_v1.mp4"),
             "-i", os.path.join(SRC, "gp_v5.mp4"), "-filter_complex",
             "[0:v]scale=1080:-2,pad=1080:600:0:(600-ih)/2,setsar=1,fps=30[v0];"
             "[1:v]trim=0:7.6,setpts=PTS-STARTPTS,scale=1080:-2,pad=1080:600:0:(600-ih)/2,setsar=1,fps=30[v1];"
             "[v0][v1]concat=n=2:v=1:a=0[v];[2:a]atrim=0:20,asetpts=PTS-STARTPTS,volume=1.8,afade=t=out:st=18.5:d=1.5[a]",
             "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "16", "-c:a", "aac", seg])
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-i", bgp, "-i", seg, "-filter_complex",
             "[0:v][1:v]overlay=0:660:shortest=1[v]", "-map", "[v]", "-map", "1:a", "-t", str(dur),
             "-r", "30", "-c:v", "libx264", "-crf", "16", "-c:a", "aac", base])
    elif pid.startswith("R003"):
        poster = os.path.join(TMP, "poster_1080.png")
        p = Image.open(os.path.join(SRC, "poster_299.jpg")).convert("RGB")
        p = p.resize((int(p.width * H / p.height), H))
        p = p.crop(((p.width - W) // 2, 0, (p.width - W) // 2 + W, H))
        p.save(poster)
        run(["ffmpeg", "-v", "error", "-y", "-i", os.path.join(SRC, "v2_main.mp4"), "-loop", "1", "-t", "5.5", "-i", poster,
             "-filter_complex",
             "[0:v]fps=30,setsar=1[v0];[1:v]fps=30,setsar=1,format=yuv420p[v1];[v0][v1]concat=n=2:v=1:a=0[v];"
             "[0:a]atrim=8.2:13.7,asetpts=PTS-STARTPTS,afade=t=out:st=4.3:d=1.2[tail];[0:a][tail]concat=n=2:v=0:a=1[a]",
             "-map", "[v]", "-map", "[a]", "-t", str(dur), "-c:v", "libx264", "-crf", "16", "-c:a", "aac", base])
    # ----- cards -----
    inputs = ["-i", base]
    for i, c in enumerate(r["cards"]):
        cp = os.path.join(TMP, f"{pid}_card{i}.png")
        n = make_card(c["text"], c["style"], c["zone"], cp)
        words = len(c["text"].split())
        secs = c["t"][1] - c["t"][0]
        flag = "" if secs / words >= 0.3 else "  <-- FAST"
        print(f"  card {i}: {secs:.1f}s / {words} words = {secs / words:.2f} s/word{flag}")
        inputs += ["-i", cp]
    label = os.path.join(TMP, "label.png")
    make_label(label)
    inputs += ["-i", label]
    chain, last = overlay_chain("0:v", r["cards"])
    n = len(r["cards"])
    lab_until = r.get("label_until", dur)
    chain += f";[{last}][{n + 1}:v]overlay=0:0:enable='between(t,0,{lab_until})'[vout]"
    run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", chain, "-map", "[vout]", "-map", "0:a",
         "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
         "-c:a", "aac", "-b:a", "160k", out_mp4])
    print("rendered", out_mp4)


# ---------- carousel ----------
CW, CH = 1080, 1350


def grab_frame(ref):
    """ref like gp_v5@12 -> PIL image of that frame."""
    name, t = ref.split("@")
    srcmap = {"gp_v5": "gp_v5.mp4", "gp_v1": "gp_v1.mp4", "v2": "v2_main.mp4"}
    fp = os.path.join(TMP, f"frame_{name}_{t}.png")
    if not os.path.exists(fp):
        run(["ffmpeg", "-v", "error", "-y", "-ss", t, "-i", os.path.join(SRC, srcmap[name]), "-frames:v", "1", fp])
    return Image.open(fp).convert("RGB")


def render_carousel(pid, c):
    bg = Image.open(os.path.join(SRC, "keyart_bg.jpg")).convert("RGB")
    bg = bg.resize((CW, int(bg.height * CW / bg.width)))
    n = len(c["slides"])
    for i, s in enumerate(c["slides"], 1):
        canvas = Image.new("RGB", (CW, CH), (0, 0, 0))
        canvas.paste(bg, (0, (CH - bg.height) // 2))
        canvas = Image.eval(canvas, lambda v: int(v * 0.55))
        d = ImageDraw.Draw(canvas)
        vis = s["visual"]
        if vis == "keyart":
            art = Image.open(os.path.join(SRC, "poster_299.jpg")).convert("RGB")
            art = art.crop((0, 230, art.width, 1230))  # cube + title lockup
            art = art.resize((900, int(art.height * 900 / art.width)))
            canvas.paste(art, ((CW - art.width) // 2, 60))
            text_top = 60 + art.height + 30
        elif vis == "poster":
            art = Image.open(os.path.join(SRC, "poster_299.jpg")).convert("RGB")
            art = art.resize((int(art.width * 760 / art.height), 760))
            canvas.paste(art, ((CW - art.width) // 2, 70))
            text_top = 860
        else:
            fr = grab_frame(vis)
            fr = fr.resize((980, int(fr.height * 980 / fr.width)))
            # cyan frame
            d.rounded_rectangle([44, 96, 44 + fr.width + 12, 96 + fr.height + 12], radius=18, outline=CYAN, width=4, fill=(0, 0, 0))
            canvas.paste(fr, (50, 102))
            text_top = 102 + fr.height + 60
        # headline
        fh = ImageFont.truetype(FONT_B, 64 if i == 1 else 58)
        lines = wrap_lines(s["head"], fh, 960)
        y = text_top + 20
        for ln in lines:
            d.text((CW / 2, y), ln, font=fh, fill=WHITE, anchor="ma", stroke_width=4, stroke_fill=(0, 0, 0))
            y += int(fh.size * 1.2)
        if s["sub"]:
            fs = ImageFont.truetype(FONT_M, 42)
            y += 24
            for ln in wrap_lines(s["sub"], fs, 940):
                d.text((CW / 2, y), ln, font=fs, fill=CYAN, anchor="ma", stroke_width=3, stroke_fill=(0, 0, 0))
                y += 54
        # footer
        ff = ImageFont.truetype(FONT_M, 30)
        d.text((60, CH - 60), "IMPACT ZERO  •  iPhone  •  $2.99", font=ff, fill=(190, 215, 235), anchor="lm")
        d.text((CW - 60, CH - 60), f"{i}/{n}" + ("   swipe >>" if i < n else ""), font=ff, fill=(190, 215, 235), anchor="rm")
        if i == 1:
            fsw = ImageFont.truetype(FONT_B, 36)
            d.text((CW / 2, CH - 130), "swipe >>", font=fsw, fill=CYAN, anchor="mm")
        canvas.save(os.path.join(OUT, f"{pid}_{i}.jpg"), quality=92)
    print("rendered carousel", pid, n, "slides")


ONLY = set(sys.argv[2:])  # optional: render only these post ids
for pid, r in spec["reels"].items():
    if not ONLY or pid in ONLY:
        render_reel(pid, r)
for pid, c in spec["carousel"].items():
    if not ONLY or pid in ONLY:
        render_carousel(pid, c)
