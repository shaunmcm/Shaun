"""Render a BrokeProofKids carousel (1080x1350 JPGs) from a slide spec.
slide = {"kicker":..., "text":..., "size":.., "sub":.., "draw": callable(img)->img, "swipe": bool}"""
import os
from PIL import Image, ImageDraw
from style import *

CW, CH = 1080, 1350


def render(spec, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    paths = []
    n = len(spec["slides"])
    for i, s in enumerate(spec["slides"]):
        img = background(CW, CH)
        if s.get("draw"):
            img = s["draw"](img)
        d = ImageDraw.Draw(img)
        pill(d, CW // 2, 70, "BrokeProofKids", size=28)
        y = s.get("y", 170)
        if s.get("kicker"):
            y = pill(d, CW // 2, y, s["kicker"], size=32, bg=TERRA) + 26
        y = text_block(d, s["text"], CW // 2, y, s.get("size", 74), 940)
        if s.get("sub"):
            text_block(d, s["sub"], CW // 2, y + 22, s.get("sub_size", 44), 920, color=SAGE_D, path=F_BOLD)
        # progress dots
        for k in range(n):
            x = CW // 2 + (k - (n - 1) / 2) * 30
            r = 8 if k == i else 6
            d.ellipse([x - r, CH - 60 - r, x + r, CH - 60 + r], fill=(INK if k == i else SAGE) + (255,))
        if s.get("swipe"):
            f = font(F_BOLD, 34)
            d.text((CW - 230, CH - 84), "Swipe", font=f, fill=SAGE_D + (255,))
            d.polygon([(CW - 112, CH - 76), (CW - 112, CH - 44), (CW - 84, CH - 60)], fill=SAGE_D + (255,))
        p = os.path.join(out_dir, f"{spec['id']}_{i + 1}.jpg")
        img.convert("RGB").save(p, quality=93)
        paths.append(p)
    sheet = Image.new("RGB", (270 * n, 338), "white")
    for i, p in enumerate(paths):
        sheet.paste(Image.open(p).resize((270, 338)), (270 * i, 0))
    sheet.save(os.path.join(out_dir, f"{spec['id']}_sheet.jpg"))
    return paths
