"""BrokeProofKids house style: light green + white grid, sage, earthy tones."""
from PIL import Image, ImageDraw, ImageFont
import re

W, H = 1080, 1920
BG = (214, 232, 204)        # light green
GRID = (255, 255, 255, 70)  # transparent white grid
SAGE = (143, 168, 128)
SAGE_D = (92, 120, 82)
INK = (38, 52, 36)          # near-black green for text
BROWN = (139, 104, 72)
SAND = (233, 214, 175)
CREAM = (251, 247, 236)
TERRA = (196, 112, 76)      # accent for emphasis
GOLD = (222, 176, 74)

F_BOLD = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
F_XB = "/usr/share/fonts/truetype/google-fonts/Poppins-ExtraBold.ttf"
F_SEMI = "/usr/share/fonts/truetype/google-fonts/Poppins-SemiBold.ttf"
F_MED = "/usr/share/fonts/truetype/google-fonts/Poppins-Medium.ttf"
import os
for _f in ("F_XB", "F_SEMI", "F_MED"):
    if not os.path.exists(globals()[_f]):
        globals()[_f] = F_BOLD

_cache = {}
def font(path, size):
    k = (path, size)
    if k not in _cache:
        _cache[k] = ImageFont.truetype(path, size)
    return _cache[k]


def background(w=W, h=H, step=60):
    img = Image.new("RGBA", (w, h), BG + (255,))
    ov = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    for x in range(0, w + 1, step):
        d.line([(x, 0), (x, h)], fill=GRID, width=2)
    for y in range(0, h + 1, step):
        d.line([(0, y), (w, y)], fill=GRID, width=2)
    img = Image.alpha_composite(img, ov)
    # soft vignette toward bottom for depth
    vg = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vg)
    for i in range(40):
        a = int(2.2 * i)
        vd.rectangle([0, h - (40 - i) * 12, w, h], fill=(92, 120, 82, 2))
    return Image.alpha_composite(img, vg)


def parse_runs(text):
    """'Make the goal *visible*' -> [(word, emph)]"""
    words = []
    for tok in text.split(" "):
        emph = "*" in tok
        words.append((tok.replace("*", ""), emph))
    return words


def wrap_runs(words, fnt, maxw, draw):
    lines, cur = [], []
    for w, e in words:
        trial = " ".join(x for x, _ in cur + [(w, e)])
        if cur and draw.textlength(trial, font=fnt) > maxw:
            lines.append(cur); cur = [(w, e)]
        else:
            cur.append((w, e))
    if cur:
        lines.append(cur)
    return lines


def text_block(draw, text, cx, y, size, maxw, color=INK, emph=TERRA,
               path=F_XB, lh=1.18, align="center", alpha=255, measure=False):
    """Draw centered multi-line text with *emphasis*. Returns bottom y."""
    fnt = font(path, size)
    lines = wrap_runs(parse_runs(text), fnt, maxw, draw)
    step = int(size * lh)
    if measure:
        return y + step * len(lines)
    for ln in lines:
        full = " ".join(w for w, _ in ln)
        lw = draw.textlength(full, font=fnt)
        x = cx - lw / 2 if align == "center" else cx
        for i, (w, e) in enumerate(ln):
            col = emph if e else color
            draw.text((x, y), w, font=fnt, fill=col + (alpha,))
            x += draw.textlength(w + " ", font=fnt)
        y += step
    return y


def pill(draw, cx, y, text, size=34, fg=CREAM, bg=SAGE_D, padx=30, pady=14, alpha=255):
    fnt = font(F_BOLD, size)
    tw = draw.textlength(text, font=fnt)
    box = [cx - tw / 2 - padx, y, cx + tw / 2 + padx, y + size + 2 * pady]
    draw.rounded_rectangle(box, radius=(size + 2 * pady) // 2, fill=bg + (alpha,))
    draw.text((cx - tw / 2, y + pady - size * 0.12), text, font=fnt, fill=fg + (alpha,))
    return box[3]


def card(img, box, fill=CREAM, radius=40, shadow=True, alpha=255):
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    if shadow:
        sb = [box[0] + 8, box[1] + 12, box[2] + 8, box[3] + 12]
        d.rounded_rectangle(sb, radius=radius, fill=(60, 80, 55, int(45 * alpha / 255)))
    d.rounded_rectangle(box, radius=radius, fill=fill + (alpha,))
    return Image.alpha_composite(img, ov)


def brand_tag(draw, w=W, y=232, alpha=255):
    # small brand chip at top, below IG header safe zone
    pill(draw, w // 2, y, "BrokeProofKids", size=30, fg=CREAM, bg=SAGE_D, alpha=alpha)
