#!/usr/bin/env python3
"""Impact Zero creative format v2 (Nov 9 2026 user prompt).
Gameplay-first Reels: blurred gameplay backdrop + large centred gameplay crop,
big bold 3-7 word text, no persistent branding, short end card "IMPACT ZERO PROJECT / ON STEAM".
Usage: python3 tools/render2.py posts/dayNN.json [post_ids...]
Spec per reel: segments [{src,start,end}], texts [{t:[a,b], text, zone:'top'|'mid'}],
endcard {sub: 'CAN YOU BEAT IT?'} (last `endcard_len` s, default 2.5), optional audio_bed.
Carousels: slides [{visual, head, sub}], visual = 'src@sec' | 'keyart' | 'endcard'.
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "src")
FB = "/usr/share/fonts/opentype/inter/Inter-Black.otf"
FM = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
W, H = 1080, 1920
FG_H, FG_Y = 860, 520
LIMIT = {"gp_v5": 28.6, "gp_v1": 14.4, "v4_bts": 12.4}
YELLOW, RED, WHITE = (255, 214, 0), (255, 70, 70), (255, 255, 255)


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr[-2000:])


def check_seg(pid, sg):
    if sg["end"] > LIMIT.get(sg["src"], 1e9) + 0.01:
        sys.exit(f"{pid}: {sg} past end of clip / old end card - BANNED")
    if sg["src"] == "gp_v5" and sg["start"] < 23.5 and sg["end"] > 19.5:
        sys.exit(f"{pid}: {sg} overlaps gp_v5 19.5-23.5 co-op text - BANNED")


def wrap(text, font, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if font.getlength(t) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_text(d, cx, y, text, size, maxw=960, stroke=9):
    """Words in *stars* are yellow, words in !bangs! red."""
    font = ImageFont.truetype(FB, size)
    plain = text.replace("*", "").replace("!", "")
    lines = wrap(plain, font, maxw)
    # rebuild per-word colours
    toks = text.split()
    cols = []
    for t in toks:
        cols.append(YELLOW if t.startswith("*") else RED if t.startswith("!") else WHITE)
    i = 0
    lh = int(size * 1.12)
    for ln in lines:
        ws = ln.split()
        widths = [font.getlength(w) for w in ws]
        sp = font.getlength(" ")
        x = cx - (sum(widths) + sp * (len(ws) - 1)) / 2
        for w, wd in zip(ws, widths):
            d.text((x, y), w, font=font, fill=cols[i], stroke_width=stroke, stroke_fill=(0, 0, 0))
            x += wd + sp; i += 1
        y += lh
    return y


def text_png(text, zone, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    n = len(text.replace("*", "").replace("!", "").split())
    size = 112 if n <= 4 else 96
    if zone == "top":
        draw_text(d, W / 2, 150, text, size)
    else:  # mid-low, inside gameplay, above IG caption area
        draw_text(d, W / 2, 1420, text, size)
    img.save(path)


def endcard_png(sub, path):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 175))
    d = ImageDraw.Draw(img)
    y = draw_text(d, W / 2, 700, "IMPACT ZERO PROJECT", 104, maxw=900)
    f = ImageFont.truetype(FB, 86)
    d.text((W / 2, y + 60), "ON STEAM", font=f, fill=YELLOW, anchor="ma", stroke_width=7, stroke_fill=(0, 0, 0))
    if sub:
        draw_text(d, W / 2, y + 220, sub, 64, stroke=6)
    img.save(path)


def render_reel(pid, r, out):
    tmp = os.path.join(out, f"_{pid}"); os.makedirs(tmp, exist_ok=True)
    segs = r["segments"]
    for sg in segs:
        check_seg(pid, sg)
    total = sum(s["end"] - s["start"] for s in segs)
    ec = r.get("endcard_len", 2.5)
    last_t = max(t["t"][1] for t in r["texts"])
    if total + 0.05 < last_t + ec:
        sys.exit(f"{pid}: footage {total:.1f}s shorter than texts {last_t}s + end card {ec}s")
    # 1) normalise + concat gameplay (1440x720, 30fps, stereo 44.1k)
    parts = []
    for k, sg in enumerate(segs):
        p = os.path.join(tmp, f"s{k}.mp4"); parts.append(p)
        src = os.path.join(SRC, sg["src"] + ".mp4")
        has_a = sg["src"] != "v4_bts"
        cmd = ["ffmpeg", "-y", "-loglevel", "error", "-ss", str(sg["start"]), "-t", str(sg["end"] - sg["start"]), "-i", src]
        if not has_a:
            cmd += ["-f", "lavfi", "-t", str(sg["end"] - sg["start"]), "-i", "anullsrc=r=44100:cl=stereo"]
        cmd += ["-vf", "scale=1440:720,setsar=1,fps=30", "-map", "0:v"] + (["-map", "0:a"] if has_a else ["-map", "1:a"]) + [
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-c:a", "aac", "-ar", "44100", "-ac", "2", "-shortest", p]
        run(cmd)
    lst = os.path.join(tmp, "l.txt")
    open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    cat = os.path.join(tmp, "cat.mp4")
    run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", cat])
    # 2) overlays
    pngs = []
    for k, t in enumerate(r["texts"]):
        p = os.path.join(tmp, f"t{k}.png"); text_png(t["text"], t.get("zone", "top"), p); pngs.append((p, t["t"]))
    ecp = os.path.join(tmp, "end.png"); endcard_png(r.get("endcard", {}).get("sub", "CAN YOU BEAT IT?"), ecp)
    dur = total
    pngs.append((ecp, [dur - ec, dur + 1]))
    inputs = ["-i", cat]
    for p, _ in pngs:
        inputs += ["-i", p]
    fc = (f"[0:v]split[a][b];[a]scale=-2:{H},crop={W}:{H},boxblur=24:3,eq=brightness=-0.22:saturation=1.1[bg];"
          f"[b]scale=-2:{FG_H},crop={W}:{FG_H}[fg];[bg][fg]overlay=0:{FG_Y}[v0]")
    last = "v0"
    for k, (_, (a, b)) in enumerate(pngs):
        fc += f";[{last}][{k+1}:v]overlay=0:0:enable='between(t,{a},{b})'[v{k+1}]"; last = f"v{k+1}"
    af = f"[0:a]volume={r.get('gain',1.4)},afade=t=out:st={max(dur-1.2,0)}:d=1.2[aout]"
    o = os.path.join(out, f"{pid}.mp4")
    run(["ffmpeg", "-y", "-loglevel", "error"] + inputs + ["-filter_complex", fc + ";" + af, "-map", f"[{last}]", "-map", "[aout]",
         "-t", str(dur), "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", "30",
         "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", o])
    for t in r["texts"]:
        words = len(t["text"].split()); span = t["t"][1] - t["t"][0]
        if words > 7: print(f"  WARN {pid}: >7 words: {t['text']}")
        if span / max(words, 1) < 0.3: print(f"  FAST {pid}: {t['text']}")
    print(f"rendered {o} ({dur:.1f}s)")


def grab(ref, tmp):
    src, sec = ref.split("@")
    p = os.path.join(tmp, f"g_{src}_{sec}.png")
    run(["ffmpeg", "-y", "-loglevel", "error", "-ss", sec, "-i", os.path.join(SRC, src + ".mp4"), "-frames:v", "1", p])
    return Image.open(p).convert("RGB")


def render_carousel(pid, c, out):
    CW, CH = 1080, 1350
    tmp = os.path.join(out, f"_{pid}"); os.makedirs(tmp, exist_ok=True)
    n = len(c["slides"])
    for i, s in enumerate(c["slides"], 1):
        v = s["visual"]
        if v in ("keyart", "endcard"):
            fr = Image.open(os.path.join(SRC, "keyart_bg.jpg")).convert("RGB")
        else:
            fr = grab(v, tmp)
        # cover-fit
        sc = max(CW / fr.width, CH / fr.height)
        bg = fr.resize((int(fr.width * sc) + 1, int(fr.height * sc) + 1))
        bg = bg.crop(((bg.width - CW) // 2, (bg.height - CH) // 2, (bg.width - CW) // 2 + CW, (bg.height - CH) // 2 + CH))
        if v == "endcard":
            bg = ImageEnhance.Brightness(bg).enhance(0.45)
        img = bg.convert("RGBA")
        shade = Image.new("RGBA", (CW, 420), (0, 0, 0, 0))
        sd = ImageDraw.Draw(shade)
        for y in range(420):
            sd.line([(0, y), (CW, y)], fill=(0, 0, 0, int(170 * (1 - y / 420))))
        img.alpha_composite(shade, (0, 0))
        d = ImageDraw.Draw(img)
        if v == "endcard":
            y = draw_text(d, CW / 2, 440, "IMPACT ZERO PROJECT", 96, maxw=900)
            f = ImageFont.truetype(FB, 80)
            d.text((CW / 2, y + 40), "ON STEAM", font=f, fill=YELLOW, anchor="ma", stroke_width=7, stroke_fill=(0, 0, 0))
            if s.get("head"):
                draw_text(d, CW / 2, y + 190, s["head"], 62, stroke=6)
        else:
            y = draw_text(d, CW / 2, 90, s["head"], 96 if len(s["head"].split()) <= 4 else 84)
            if s.get("sub"):
                draw_text(d, CW / 2, y + 10, s["sub"], 54, stroke=5)
        fs = ImageFont.truetype(FM, 34)
        if i < n:
            d.text((CW - 50, CH - 60), "swipe >>", font=fs, fill=WHITE, anchor="rm", stroke_width=3, stroke_fill=(0, 0, 0))
        img.convert("RGB").save(os.path.join(out, f"{pid}_{i}.jpg"), quality=93)
    print(f"rendered carousel {pid} {n} slides")


def main():
    spec = json.load(open(sys.argv[1]))
    only = set(sys.argv[2:])
    out = os.path.join(ROOT, "out", spec["day"].replace("-", ""))
    os.makedirs(out, exist_ok=True)
    for pid, r in spec.get("reels", {}).items():
        if not only or pid in only:
            render_reel(pid, r, out)
    for pid, c in spec.get("carousel", {}).items():
        if not only or pid in only:
            render_carousel(pid, c, out)


if __name__ == "__main__":
    main()
