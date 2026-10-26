from props import *
from PIL import ImageDraw
# OUTCOME: Parents will know a common allowance starting point ($1 per year of age, weekly) to adjust for their family.
def s1(img, t):
    img = tag(img, 330, 1200, text="$2?", sub="too little?", faded=True, angle=-8)
    return tag(img, 760, 1200, text="$20?", sub="too much?", faded=True, angle=6)
def s2(img, t): return calendar(img, 540, 1200, label="EVERY WEEK", day="$1")
def s3(img, t): return cash_stack(img, 540, 1230, t=t, bills=8, label="Age 8 = $8 a week")
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R014_amount", "music": {"style": "playful", "seed": 1212}, "scenes": [
    {"dur": 2.6, "instant": True, "text": "How much allowance? Most parents *guess.*", "size": 84, "draw": s1},
    {"dur": 2.8, "text": "Common start: *$1 per year of age.*", "size": 82, "draw": s2},
    {"dur": 4.0, "text": "Age 8 = *$8 a week.* Adjust to your family.", "size": 78, "draw": s3},
    {"dur": 2.6, "text": "Comment *BOOK* before next *payday.*", "size": 82, "draw": s6},
]}
