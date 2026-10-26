from props import *
from PIL import ImageDraw

def tree(img, cx, cy, crossed=1.0):
    ov = Image.new("RGBA", img.size, (0,0,0,0)); d = ImageDraw.Draw(ov)
    d.rounded_rectangle([cx-30, cy, cx+30, cy+220], radius=12, fill=BROWN+(255,))
    for dx, dy, r in [(-110,-20,120),(110,-20,120),(0,-110,140),(0,10,130)]:
        d.ellipse([cx+dx-r, cy+dy-r, cx+dx+r, cy+dy+r], fill=SAGE+(255,))
    for dx, dy in [(-120,-40),(90,-70),(10,-150),(120,30),(-40,20)]:
        bill(d, cx+dx, cy+dy, w=90, h=46, label="$")
    if crossed > 0:
        a = int(255*min(1, crossed))
        d.line([cx-230, cy-260, cx+230, cy+220], fill=TERRA+(a,), width=26)
    return Image.alpha_composite(img, ov)

def weeks(img, cx, cy, t, filled_to=8, total=8, price="$24 toy", per="$3 a week"):
    img = card(img, [cx-420, cy-230, cx+420, cy+260], fill=CREAM)
    d = ImageDraw.Draw(img)
    text_block(d, f"{price} ÷ {per}", cx, cy-200, 52, 780, path=F_XB)
    n = filled_to * ease(t)
    for i in range(total):
        r, c = divmod(i, 4)
        x0, y0 = cx-360 + c*185, cy-90 + r*165
        box = [x0, y0, x0+160, y0+140]
        if i < int(n) or (i == int(n) and n - int(n) > .5):
            d.rounded_rectangle(box, radius=18, fill=[SAGE, TERRA, GOLD, SAGE_D][i % 4]+(255,))
            col = CREAM
        else:
            col = (150,165,140)
        d.rounded_rectangle(box, radius=18, outline=(120,140,110,255), width=4)
        f = font(F_BOLD, 34); lab = f"Wk {i+1}"; tw = d.textlength(lab, font=f)
        d.text((x0+80-tw/2, y0+48), lab, font=f, fill=col+(255,))
    return img

def s1(img, t):
    return tree(img, 540, 1230, crossed=1.0)

def s2(img, t):
    img = bubble(img, 540, 1060, '"Can I have it?"', w=560, size=50, tail="left")
    img = bubble(img, 540, 1290, '"Money doesn\'t grow on trees."', w=760, size=48, fill=SAND, tail="right")
    return img

def s3(img, t):
    img = tag(img, 540, 1230, text="$24", sub="toy", angle=-6, w=420, h=220)
    return img

def s4(img, t):
    return weeks(img, 540, 1180, min(1, t*1.2))

def s5(img, t):
    img = tag(img, 290, 1180, text="$24", sub="toy", angle=-6, w=280)
    d = ImageDraw.Draw(img)
    text_block(d, "=", 540, 1110, 120, 200, path=F_XB)
    img = card(img, [640, 1060, 960, 1300], fill=TERRA)
    d = ImageDraw.Draw(img)
    text_block(d, "8 weeks", 800, 1110, 64, 300, color=CREAM, path=F_XB)
    text_block(d, "of allowance", 800, 1195, 38, 300, color=CREAM, path=F_BOLD)
    return img

def s6(img, t):
    return cta_scene(img, 540, 1250, t)

# OUTCOME: By the end, parents will be able to turn any "can I have it?" into a lesson about what money costs in time.
SPEC = {"id": "R002_trees", "music": {"style": "piano", "seed": 202}, "scenes": [
    {"dur": 4.4, "instant": True, "text": "\"Money doesn't grow on *trees.*\"", "size": 84,
     "sub": "Why does it raise *broke* adults?", "sub_size": 52, "draw": s1},
    {"dur": 5.4, "text": "It ends the talk. Kids learn *nothing*.", "size": 70,
     "sub": "So what do you say *instead?*", "sub_size": 48, "draw": s2},
    {"dur": 5.4, "kicker": "SAY THIS", "text": "\"Let's see how many *weeks* it costs.\"", "size": 74,
     "sub": "How does a kid count that?", "sub_size": 46, "draw": s3},
    {"dur": 4.8, "text": "$24 toy. $3 a week.", "size": 80,
     "sub": "Count the weeks *together*.", "sub_size": 48, "draw": s4},
    {"dur": 5.6, "text": "*8 weeks* of allowance. Still want it?", "size": 74,
     "sub": "Now *they* decide if it's worth it.", "sub_size": 46, "draw": s5},
    {"dur": 7.6, "text": "Want them practicing this on *paper*?", "size": 74,
     "sub": "Get the *Money* *Smart* *Kids* *Coloring* *Book*. Link in bio. Follow for more.", "sub_size": 48, "draw": s6},
]}
