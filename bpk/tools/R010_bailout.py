from props import *
from PIL import ImageDraw
# OUTCOME: Parents will understand why letting a small money mistake stand ($3 now) protects their kid from big ones later.
def s1(img, t): return bubble(img, 540, 1200, '"Fine, I\'ll pay for it."', w=760, size=64, fill=SAND)
def s2(img, t):
    img = wallet_empty(img, 330, 1200)
    return cash_stack(img, 780, 1230, t=t, bills=5, label="refilled")
def s3(img, t):
    img = tag(img, 320, 1200, text="$3", sub="lesson today", angle=-6)
    return tag(img, 760, 1200, text="$3,000", sub="lesson at 25", faded=True, angle=6, w=380)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R010_bailout", "music": {"style": "lofi", "seed": 1010}, "scenes": [
    {"dur": 4.0, "instant": True, "text": "\"Fine, I'll pay for it.\"", "size": 90,
     "sub": "What does your kid *learn?*", "sub_size": 60, "draw": s1},
    {"dur": 2.6, "text": "Money runs out? *Someone refills it.*", "size": 82, "draw": s2},
    {"dur": 2.8, "text": "Let small ones sting: *$3 lesson now.*", "size": 80, "draw": s3},
    {"dur": 2.6, "text": "Comment *BOOK* before the next *refill.*", "size": 80, "draw": s6},
]}
