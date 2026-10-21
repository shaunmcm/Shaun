"""Flat, warm illustrated props drawn with PIL. Every prop: fn(img, cx, cy, t=1.0, **kw) -> img.
t is the animation progress 0..1 within the scene (props may animate with it)."""
from PIL import Image, ImageDraw
import math
from style import *


def _ov(img):
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    return ov, ImageDraw.Draw(ov)


def ease(t):
    t = max(0.0, min(1.0, t))
    return 1 - (1 - t) ** 3


def coin(d, cx, cy, r=38, label="$1", alpha=255):
    d.ellipse([cx - r, cy - r + 6, cx + r, cy + r + 6], fill=(170, 125, 40, alpha))
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GOLD + (alpha,))
    d.ellipse([cx - r * .72, cy - r * .72, cx + r * .72, cy + r * .72], outline=(250, 220, 140, alpha), width=4)
    if label:
        f = font(F_BOLD, int(r * .7))
        tw = d.textlength(label, font=f)
        d.text((cx - tw / 2, cy - r * .48), label, font=f, fill=(140, 95, 25, alpha))


def bill(d, cx, cy, w=230, h=110, label="$1", alpha=255, rot=0):
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=12, fill=(160, 196, 140, alpha), outline=(92, 130, 82, alpha), width=4)
    d.ellipse([cx - 32, cy - 32, cx + 32, cy + 32], outline=(92, 130, 82, alpha), width=4)
    f = font(F_BOLD, 34)
    tw = d.textlength(label, font=f)
    d.text((cx - tw / 2, cy - 22), label, font=f, fill=(60, 95, 55, alpha))
    for sx in (-1, 1):
        d.text((cx + sx * (w / 2 - 34) - 14, cy - h / 2 + 6), "1", font=font(F_BOLD, 26), fill=(60, 95, 55, alpha))


def jar(img, cx, cy, t=1.0, coins=3, label="", w=300, h=360, glow=False):
    ov, d = _ov(img)
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    # lid
    d.rounded_rectangle([x0 + 30, y0 - 46, x1 - 30, y0 + 8], radius=14, fill=BROWN + (255,))
    # glass
    d.rounded_rectangle([x0, y0, x1, y1], radius=50, fill=(255, 255, 255, 120), outline=(255, 255, 255, 230), width=6)
    # coins stacking from bottom
    n = int(round(coins * ease(t))) if coins > 0 else 0
    for i in range(n):
        row, col = divmod(i, 3)
        coin(d, x0 + 70 + col * 80 + (row % 2) * 20, y1 - 52 - row * 46, r=34, label="")
    # shine
    d.rounded_rectangle([x0 + 26, y0 + 30, x0 + 48, y1 - 80], radius=10, fill=(255, 255, 255, 110))
    if label:
        lb = [x0 + 40, cy - 40, x1 - 40, cy + 30]
        d.rounded_rectangle(lb, radius=12, fill=CREAM + (255,))
        f = font(F_BOLD, 38)
        tw = d.textlength(label, font=f)
        d.text((cx - tw / 2, cy - 34), label, font=f, fill=INK + (255,))
    return Image.alpha_composite(img, ov)


def tag(img, cx, cy, t=1.0, text="$30", sub="", faded=False, w=320, h=170, angle=-8):
    layer = Image.new("RGBA", (w + 120, h + 120), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    a = 110 if faded else 255
    ox, oy = 60, 60
    pts = [(ox, oy + h / 2), (ox + 60, oy), (ox + w, oy), (ox + w, oy + h), (ox + 60, oy + h)]
    d.polygon(pts, fill=SAND + (a,), outline=BROWN + (a,))
    d.line(pts + [pts[0]], fill=BROWN + (a,), width=5)
    d.ellipse([ox + 34, oy + h / 2 - 14, ox + 62, oy + h / 2 + 14], fill=BG + (a,), outline=BROWN + (a,), width=4)
    f = font(F_XB, 64 if not sub else 56)
    tw = d.textlength(text, font=f)
    ty = oy + (h / 2 - 40 if not sub else 18)
    d.text((ox + 60 + (w - 60 - tw) / 2, ty), text, font=f, fill=INK + (a,))
    if sub:
        fs = font(F_SEMI, 30)
        sw = d.textlength(sub, font=fs)
        d.text((ox + 60 + (w - 60 - sw) / 2, oy + h - 58), sub, font=fs, fill=BROWN + (a,))
    layer = layer.rotate(angle, resample=Image.BICUBIC)
    img = img.copy()
    img.alpha_composite(layer, (int(cx - layer.width / 2), int(cy - layer.height / 2)))
    return img


def skateboard(d, cx, cy, s=1.0, alpha=255):
    w, h = 300 * s, 46 * s
    d.rounded_rectangle([cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2], radius=h / 2, fill=TERRA + (alpha,))
    d.line([cx - w / 2 + 30 * s, cy, cx + w / 2 - 30 * s, cy], fill=(230, 160, 120, alpha), width=int(6 * s))
    for sx in (-1, 1):
        wx = cx + sx * w * .32
        d.rectangle([wx - 14 * s, cy + h / 2, wx + 14 * s, cy + h / 2 + 14 * s], fill=(120, 120, 120, alpha))
        d.ellipse([wx - 28 * s, cy + h / 2 + 8 * s, wx - 2 * s, cy + h / 2 + 34 * s], fill=INK + (alpha,))
        d.ellipse([wx + 2 * s, cy + h / 2 + 8 * s, wx + 28 * s, cy + h / 2 + 34 * s], fill=INK + (alpha,))


def tracker(img, cx, cy, t=1.0, total=30, start=0, end=0, goal="Skateboard", price="$30", cols=6, cell=84, show_count=True):
    """Coloring-style savings tracker: goal picture + grid of boxes that fill from start->end with t."""
    rows = math.ceil(total / cols)
    gw, gh = cols * cell, rows * cell
    top = cy - (gh + 230) / 2
    img = card(img, [cx - gw / 2 - 40, top - 30, cx + gw / 2 + 40, top + 230 + gh + 40], fill=CREAM)
    ov, d = _ov(img)
    skateboard(d, cx - 120, top + 70, s=.62)
    f = font(F_XB, 46)
    filled = start + (end - start) * ease(t)
    d.text((cx + 10, top + 22), f"{goal}", font=font(F_BOLD, 38), fill=INK + (255,))
    head = f"${int(round(filled))} of {price}" if show_count else f"Goal: {price}"
    d.text((cx + 10, top + 72), head, font=f, fill=TERRA + (255,))
    nfull = int(filled)
    gy = top + 170
    for i in range(total):
        r, c = divmod(i, cols)
        x0, y0 = cx - gw / 2 + c * cell, gy + r * cell
        box = [x0 + 6, y0 + 6, x0 + cell - 6, y0 + cell - 6]
        if i < nfull:
            col = [SAGE, (171, 196, 150), TERRA, GOLD][(i * 7) % 4]
            d.rounded_rectangle(box, radius=12, fill=col + (255,))
        elif i == nfull and filled - nfull > 0.05:
            a = int(255 * (filled - nfull))
            d.rounded_rectangle(box, radius=12, fill=SAGE + (a,))
        d.rounded_rectangle(box, radius=12, outline=(120, 140, 110, 255), width=4)
        fs = font(F_SEMI, 26)
        lab = f"${i + 1}"
        tw = d.textlength(lab, font=fs)
        d.text((x0 + cell / 2 - tw / 2, y0 + cell / 2 - 18), lab, font=fs,
               fill=(255, 255, 255, 230) if i < nfull else (150, 165, 140, 255))
    return Image.alpha_composite(img, ov)


def check(d, cx, cy, r=70, alpha=255):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SAGE_D + (alpha,))
    d.line([(cx - r * .45, cy), (cx - r * .1, cy + r * .35), (cx + r * .5, cy - r * .35)], fill=CREAM + (alpha,), width=int(r * .22), joint="curve")


def bubble(img, cx, cy, text, w=760, size=46, fill=CREAM, color=INK, tail="left", alpha=255):
    tmp = ImageDraw.Draw(img)
    h = text_block(tmp, text, 0, 0, size, w - 80, path=F_BOLD, measure=True) + 70
    box = [cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2]
    img = card(img, box, fill=fill, radius=44, alpha=alpha)
    d = ImageDraw.Draw(img)
    tx = box[0] + 90 if tail == "left" else box[2] - 90
    d.polygon([(tx - 30, box[3] - 2), (tx + 30, box[3] - 2), (tx + (-40 if tail == "left" else 40), box[3] + 48)], fill=fill + (alpha,))
    text_block(d, text, cx, box[1] + 35, size, w - 80, color=color, path=F_BOLD, alpha=alpha)
    return img


def wallet_empty(img, cx, cy, t=1.0):
    ov, d = _ov(img)
    d.rounded_rectangle([cx - 190, cy - 120, cx + 190, cy + 130], radius=36, fill=BROWN + (255,))
    d.rounded_rectangle([cx - 190, cy - 120, cx + 190, cy - 20], radius=36, fill=(160, 122, 86, 255))
    d.ellipse([cx + 110, cy - 40, cx + 150, cy], fill=SAND + (255,))
    f = font(F_XB, 60)
    d.text((cx - 50, cy + 10), "$0", font=f, fill=CREAM + (255,))
    return Image.alpha_composite(img, ov)


def calendar(img, cx, cy, t=1.0, label="1 WEEK LATER", day="7"):
    img = card(img, [cx - 170, cy - 170, cx + 170, cy + 170], fill=CREAM, radius=30)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([cx - 170, cy - 170, cx + 170, cy - 80], radius=30, fill=TERRA + (255,))
    d.rectangle([cx - 170, cy - 110, cx + 170, cy - 80], fill=TERRA + (255,))
    f = font(F_BOLD, 34)
    tw = d.textlength(label, font=f)
    d.text((cx - tw / 2, cy - 152), label, font=f, fill=CREAM + (255,))
    f2 = font(F_XB, 150)
    tw = d.textlength(day, font=f2)
    d.text((cx - tw / 2, cy - 90), day, font=f2, fill=INK + (255,))
    return img


def slime(d, cx, cy, s=1.0, alpha=255):
    d.rounded_rectangle([cx - 90 * s, cy - 60 * s, cx + 90 * s, cy + 90 * s], radius=26 * s, fill=(255, 255, 255, int(alpha * .7)), outline=(255, 255, 255, alpha), width=5)
    d.ellipse([cx - 80 * s, cy - 10 * s, cx + 80 * s, cy + 84 * s], fill=(150, 205, 190, alpha))
    d.rounded_rectangle([cx - 100 * s, cy - 92 * s, cx + 100 * s, cy - 52 * s], radius=14 * s, fill=TERRA + (alpha,))


def split_bar(img, cx, cy, t=1.0, parts=(("Saving goal", 7, SAGE_D), ("Free choice", 3, TERRA)), total=10, w=840):
    ov, d = _ov(img)
    x = cx - w / 2
    p = ease(t)
    for name, val, col in parts:
        seg = w * val / total * p
        d.rounded_rectangle([x, cy - 70, x + seg, cy + 70], radius=24, fill=col + (255,))
        if p > .6:
            f = font(F_XB, 64)
            lab = f"${val}"
            tw = d.textlength(lab, font=f)
            d.text((x + seg / 2 - tw / 2, cy - 48), lab, font=f, fill=CREAM + (255,))
            fs = font(F_BOLD, 34)
            tw = d.textlength(name, font=fs)
            d.text((x + seg / 2 - tw / 2, cy + 90), name, font=fs, fill=INK + (255,))
        x += seg
    return Image.alpha_composite(img, ov)


def crayons(d, cx, cy, s=1.0, alpha=255):
    cols = [TERRA, GOLD, SAGE, (110, 150, 190), BROWN]
    for i, c in enumerate(cols):
        x = cx + (i - 2) * 70 * s
        ang = (i - 2) * 6
        d.rounded_rectangle([x - 22 * s, cy - 120 * s, x + 22 * s, cy + 110 * s], radius=8, fill=c + (alpha,))
        d.polygon([(x - 22 * s, cy - 120 * s), (x + 22 * s, cy - 120 * s), (x, cy - 175 * s)], fill=c + (alpha,))
        d.rectangle([x - 22 * s, cy - 40 * s, x + 22 * s, cy + 10 * s], fill=CREAM + (alpha,))


def cta_scene(img, cx, cy, t=1.0):
    ov, d = _ov(img)
    crayons(d, cx - 170, cy, s=.8)
    coin(d, cx + 150, cy - 40, r=70, label="$")
    coin(d, cx + 230, cy + 70, r=52, label="¢")
    return Image.alpha_composite(img, ov)


PROPS = {
    "jar": jar, "tag": tag, "tracker": tracker, "wallet_empty": wallet_empty,
    "calendar": calendar, "split_bar": split_bar, "cta": cta_scene,
}


def budget_card(img, cx, cy, t=1.0, title="October plan (example)", rows=(("Groceries", 100, 100), ("Gas", 100, 100), ("Fun money", 40, 28)), highlight=2, foot=None):
    """Screenshot-style family budget card. rows = (label, budget, spent). Bars animate with t."""
    h = 150 + 120 * len(rows) + (70 if foot else 0)
    box = [cx - 420, cy - h / 2, cx + 420, cy + h / 2]
    img = card(img, box, fill=CREAM)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([box[0], box[1], box[2], box[1] + 100], radius=40, fill=SAGE_D + (255,))
    d.rectangle([box[0], box[1] + 60, box[2], box[1] + 100], fill=SAGE_D + (255,))
    f = font(F_BOLD, 40); tw = d.textlength(title, font=f)
    d.text((cx - tw / 2, box[1] + 26), title, font=f, fill=CREAM + (255,))
    y = box[1] + 130
    for i, (lab, bud, spent) in enumerate(rows):
        hl = i == highlight
        d.text((box[0] + 40, y), lab, font=font(F_BOLD, 38), fill=(TERRA if hl else INK) + (255,))
        left = bud - spent
        rt = f"${left} left" if hl else f"${bud}"
        fr = font(F_XB if hl else F_SEMI, 38); rw = d.textlength(rt, font=fr)
        d.text((box[2] - 40 - rw, y), rt, font=fr, fill=(TERRA if hl else SAGE_D) + (255,))
        bx0, bx1 = box[0] + 40, box[2] - 40
        d.rounded_rectangle([bx0, y + 58, bx1, y + 80], radius=11, fill=(225, 230, 215, 255))
        p = ease(t) * spent / bud
        if p > 0:
            d.rounded_rectangle([bx0, y + 58, bx0 + (bx1 - bx0) * p, y + 80], radius=11, fill=(TERRA if hl else SAGE) + (255,))
        y += 120
    if foot:
        fs = font(F_BOLD, 36); tw = d.textlength(foot, font=fs)
        d.text((cx - tw / 2, y + 4), foot, font=fs, fill=INK + (255,))
    return img


def coin_jar_line(img, cx, cy, t=1.0, start=0.0, end=1.0, goal_label="$15 goal", amount_from=0.0, amount_to=15.0, day_from=0, day_to=60):
    """Jar with a drawn goal line; coin fill rises from start->end fraction; live $ and day counter pill."""
    w, h = 320, 420
    x0, y0, x1, y1 = cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0)); d = ImageDraw.Draw(ov)
    d.rounded_rectangle([x0 + 34, y0 - 50, x1 - 34, y0 + 8], radius=14, fill=BROWN + (255,))
    d.rounded_rectangle([x0, y0, x1, y1], radius=50, fill=(255, 255, 255, 60))
    frac = start + (end - start) * ease(t)
    fill_top = y1 - 20 - (h - 60) * frac
    if frac > 0:
        d.rounded_rectangle([x0 + 14, fill_top, x1 - 14, y1 - 14], radius=36, fill=GOLD + (230,))
        for k in range(int((y1 - fill_top) / 40)):
            yy = y1 - 40 - k * 40
            for xx in (x0 + 70, cx, x1 - 70):
                d.ellipse([xx - 26, yy - 12, xx + 26, yy + 12], outline=(190, 140, 50, 255), width=3)
    d.rounded_rectangle([x0, y0, x1, y1], radius=50, outline=(255, 255, 255, 240), width=7)
    gy = y0 + 40
    for xx in range(int(x0 - 20), int(x1 + 20), 30):
        d.line([xx, gy, xx + 16, gy], fill=TERRA + (255,), width=6)
    d.text((x1 + 30, gy - 24), goal_label, font=font(F_XB, 42), fill=TERRA + (255,))
    img = Image.alpha_composite(img, ov)
    d = ImageDraw.Draw(img)
    amt = amount_from + (amount_to - amount_from) * ease(t)
    day = int(round(day_from + (day_to - day_from) * ease(t)))
    pill(d, cx - 150, y1 + 40, f"Day {day}", size=40, bg=INK)
    pill(d, cx + 130, y1 + 40, f"${amt:,.2f}", size=40, bg=TERRA)
    return img


def swap_card(img, cx, cy, old, new, t=1.0):
    """Old phrase (struck through) -> new phrase. Screenshot-chat style."""
    img = bubble(img, cx - 40, cy - 150, old, w=820, size=46, fill=SAND, tail="left")
    d = ImageDraw.Draw(img)
    fo = font(F_BOLD, 46)
    # strike line across the old bubble center
    d.line([cx - 400, cy - 150, cx + 320, cy - 150], fill=TERRA + (230,), width=8)
    if t > 0.25:
        a = int(255 * min(1, (t - .25) / .2))
        img = bubble(img, cx + 40, cy + 120, new, w=820, size=46, fill=CREAM, tail="right", alpha=a)
        d = ImageDraw.Draw(img)
        check(d, cx + 420, cy + 40, r=40, alpha=a)
    return img
