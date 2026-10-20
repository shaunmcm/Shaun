"""Render a BrokeProofKids Reel from a scene spec.
spec = {"id":..., "music": {"style":..,"seed":..}, "scenes":[
   {"dur": 3.6, "text": "Hook with *emphasis*", "size": 84, "sub": "smaller line", "kicker": "small pill above",
    "draw": callable(img, t) -> img   # props for the scene, t = 0..1 progress in the scene
   }, ...]}
Text lives in y 330..~1000 (clear of IG header); props in ~1050..1500 (clear of caption/buttons)."""
import os, subprocess, shutil, sys
from PIL import Image, ImageDraw
from style import *
import music

FPS = 30
XF = 0.25  # crossfade seconds


def ease(t):
    t = max(0, min(1, t)); return 1 - (1 - t) ** 3


def scene_frame(bg, sc, lt):
    img = bg.copy()
    dur = sc["dur"]
    t = lt / dur
    if sc.get("draw"):
        img = sc["draw"](img, t)
    d = ImageDraw.Draw(img)
    brand_tag(d)
    # text pop: slide up 30px + fade over .3s (hook scene appears instantly, readable at frame 1)
    k = 1.0 if sc.get("instant") else ease(lt / .3)
    a = int(255 * k); dy = int(30 * (1 - k))
    y = sc.get("y", 340)
    if sc.get("kicker"):
        y = pill(d, W // 2, y + dy, sc["kicker"], size=34, bg=TERRA, alpha=a) + 28
    y = text_block(d, sc["text"], W // 2, y + dy, sc.get("size", 80), 900, alpha=a)
    if sc.get("sub"):
        k2 = 1.0 if sc.get("instant") else ease((lt - sc.get("sub_at", .5)) / .35)
        if k2 > 0:
            text_block(d, sc["sub"], W // 2, y + 26, sc.get("sub_size", 50), 880, color=SAGE_D, emph=TERRA,
                       path=F_BOLD, alpha=int(255 * k2))
    return img


def render(spec, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    fr = os.path.join(out_dir, "frames_" + spec["id"]); shutil.rmtree(fr, ignore_errors=True); os.makedirs(fr)
    bg = background()
    scenes = spec["scenes"]
    starts, acc = [], 0
    for s in scenes:
        starts.append(acc); acc += s["dur"]
    total = acc
    n = int(total * FPS)
    for i in range(n):
        tt = i / FPS
        si = max(j for j in range(len(scenes)) if starts[j] <= tt)
        lt = tt - starts[si]
        img = scene_frame(bg, scenes[si], lt)
        # crossfade from previous scene at the start of each scene (not the first)
        if si > 0 and lt < XF:
            prev = scene_frame(bg, scenes[si - 1], scenes[si - 1]["dur"] - 0.001)
            img = Image.blend(prev, img, lt / XF)
        img.convert("RGB").save(os.path.join(fr, f"{i:05d}.jpg"), quality=92)
    wav = os.path.join(out_dir, spec["id"] + ".wav")
    minfo = music.make(wav, total, spec.get("music", {}).get("style"), spec.get("music", {}).get("seed"))
    mp4 = os.path.join(out_dir, spec["id"] + ".mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", os.path.join(fr, "%05d.jpg"),
                    "-i", wav, "-c:v", "libx264", "-pix_fmt", "yuv420p", "-profile:v", "high", "-crf", "20",
                    "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", mp4], check=True)
    shutil.rmtree(fr)
    return mp4, total, minfo


def stills(mp4, times, out_png):
    """Contact sheet of frames at given times, for QA."""
    tiles = []
    for k, t in enumerate(times):
        p = out_png + f".{k}.jpg"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-ss", str(t), "-i", mp4, "-frames:v", "1", p], check=True)
        tiles.append(Image.open(p).resize((360, 640)))
    sheet = Image.new("RGB", (360 * len(tiles), 640), "white")
    for k, im in enumerate(tiles):
        sheet.paste(im, (360 * k, 0)); os.remove(out_png + f".{k}.jpg")
    sheet.save(out_png)
    return out_png
