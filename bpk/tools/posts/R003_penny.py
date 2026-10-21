from props import *
from PIL import ImageDraw
# OUTCOME: By the end, parents will be able to show their kid how tiny daily coins add up to a real goal.

def s1(img, t):
    img = jar(img, 360, 1230, coins=1)
    ov = Image.new("RGBA", img.size, (0,0,0,0)); d = ImageDraw.Draw(ov); coin(d, 760, 1180, r=95, label="1¢")
    return Image.alpha_composite(img, ov)
def s2(img, t):
    ov = Image.new("RGBA", img.size, (0,0,0,0)); d = ImageDraw.Draw(ov); coin(d, 360, 1220, r=130 - 30*t, label="1¢")
    img = Image.alpha_composite(img, ov)
    return tag(img, 760, 1200, text="$15", sub="their goal", faded=True)
def s3(img, t):
    return coin_jar_line(img, 470, 1190, t=0, start=0, end=0, amount_to=0, day_to=0)
def s4(img, t):
    return coin_jar_line(img, 470, 1190, t=min(1, t*1.15), start=0, end=.5, amount_from=0, amount_to=7.5, day_from=0, day_to=30)
def s5(img, t):
    img = coin_jar_line(img, 470, 1190, t=min(1, t*1.3), start=.5, end=1, amount_from=7.5, amount_to=15, day_from=30, day_to=60)
    if t > .8:
        d = ImageDraw.Draw(img); check(d, 470, 1190, r=70, alpha=int(255*min(1,(t-.8)/.1)))
    return img
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img

SPEC = {"id": "R003_penny", "music": {"style": "playful", "seed": 303}, "scenes": [
    {"dur": 5.2, "instant": True, "text": "\"A penny saved is a penny earned.\"", "size": 82,
     "sub": "So why do kids *ignore* it?", "sub_size": 54, "draw": s1},
    {"dur": 6.0, "text": "One coin feels like *nothing* to a kid.", "size": 74,
     "sub": "So how do you make it count?", "sub_size": 48, "draw": s2},
    {"dur": 6.8, "kicker": "TRY THIS", "text": "Save *25¢* a day. Mark a goal line on the jar.", "size": 68,
     "sub": "How long until it's real money?", "sub_size": 46, "draw": s3},
    {"dur": 6.0, "text": "Day 7: *$1.75.* Day 30: *$7.50.*", "size": 76,
     "sub": "Watch the line get closer.", "sub_size": 48, "draw": s4},
    {"dur": 5.2, "text": "Day 60: *$15.* Goal hit.", "size": 80,
     "sub": "Same coins they used to ignore.", "sub_size": 48, "draw": s5},
    {"dur": 8.0, "text": "Want them practicing this on *paper*?", "size": 74,
     "sub": "Comment *BOOK* for the *Money* *Smart* *Kids* *Coloring* *Book* link. Follow for more.", "sub_size": 48, "draw": s6},
]}
