from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to show how "only a few dollars" adds up over a month.
def s1(img, t): return tag(img, 540, 1200, text="$3", sub="just $3", faded=True)
def s2(img, t): return calendar(img, 540, 1200, label="EVERY WEEK", day="$3")
def s3(img, t): return cash_stack(img, 540, 1230, t=t, bills=6, label="4 weeks = $12 (example)")
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R022_fewdollars", "music": {"style": "pluck", "seed": 2222}, "scenes": [
    {"dur": 4.0, "instant": True, "text": "\"It's *only* a few dollars.\"", "size": 86,
     "sub": "What does your kid *hear?*", "sub_size": 60, "draw": s1},
    {"dur": 2.6, "text": "Small money *doesn't count.*", "size": 86, "draw": s2},
    {"dur": 2.8, "text": "$3 a week = *$12 a month.*", "size": 78, "draw": s3},
    {"dur": 2.6, "text": "Comment *BOOK.* Make small money *count.*", "size": 80, "draw": s6},
]}
