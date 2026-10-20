from props import *
from PIL import ImageDraw

def s1(img, t):
    img = jar(img, 360, 1250, t=1, coins=3, label="")
    img = tag(img, 760, 1180, text="$30", sub="skateboard", faded=True)
    return img

def s2(img, t):
    img = tag(img, 540, 1230, text="$30", sub="someday?", faded=True, angle=-8 + 4 * t)
    return img

def s3(img, t):
    return tracker(img, 540, 1145, t=t, start=0, end=0, show_count=False)

def s4(img, t):
    return tracker(img, 540, 1145, t=min(1, t * 1.15), start=0, end=12)

def s5(img, t):
    img = tracker(img, 540, 1145, t=min(1, t * 1.25), start=12, end=30)
    if t > .82:
        d = ImageDraw.Draw(img); check(d, 832, 812, r=54, alpha=int(255 * min(1, (t - .82) / .1)))
    return img

def s6(img, t):
    return cta_scene(img, 540, 1250, t)

SPEC = {"id": "R001_seeit", "music": {"style": "pluck", "seed": 101}, "scenes": [
    {"dur": 4.0, "instant": True, "text": "Your kid gives up on saving after *3 days*?", "size": 86,
     "sub": "Make the goal something they can *see*.", "draw": s1},
    {"dur": 4.4, "text": "To a kid, *$30 someday* can feel invisible.", "size": 80,
     "sub": "No visible progress, so they stop.", "draw": s2},
    {"dur": 5.6, "kicker": "TRY THIS", "text": "Draw the goal. Split it into *30 boxes*.", "size": 74,
     "sub": "One box for every $1.", "sub_size": 46, "draw": s3},
    {"dur": 6.6, "text": "Each $1 saved = they *color one box*.", "size": 74,
     "sub": "Watch $0 turn into $12.", "sub_size": 46, "draw": s4},
    {"dur": 5.8, "text": "The goal gets *closer* every week.", "size": 74,
     "sub": "Progress they can see keeps them saving.", "sub_size": 46, "draw": s5},
    {"dur": 5.0, "text": "Want more money activities to *color together*?", "size": 72,
     "sub": "Find our kids' money activity & coloring book. *Link* *in* *bio.*", "sub_size": 46, "draw": s6},
]}
