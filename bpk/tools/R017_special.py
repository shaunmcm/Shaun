from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to turn "save it for something special" into one named, priced goal their kid can see.
def s1(img, t): return jar(img, 540, 1230, coins=2, label="SPECIAL?", w=280, h=330)
def s2(img, t): return tag(img, 540, 1200, text="???", sub="vague goal", faded=True)
def s3(img, t): return tracker(img, 540, 1250, t=t, total=30, start=0, end=8, goal="Skateboard", price="$30", cols=6, cell=62)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R017_special", "music": {"style": "piano", "seed": 1717}, "scenes": [
    {"dur": 4.0, "instant": True, "text": "\"Save it for something *special.*\"", "size": 84,
     "sub": "What's *special* to a 6-year-old?", "sub_size": 58, "draw": s1},
    {"dur": 2.6, "text": "Too vague. So they *quit.*", "size": 86, "draw": s2},
    {"dur": 2.8, "text": "Name it, price it, *picture it.*", "size": 84, "draw": s3},
    {"dur": 2.6, "text": "Comment *BOOK.* Give saving a *goal.*", "size": 82, "draw": s6},
]}
