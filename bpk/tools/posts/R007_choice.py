from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to let their kid make a real trade-off ($20, two $15 toys) by asking "which one, and why?" instead of choosing for them.
def s1(img, t):
    img = tag(img, 330, 1180, text="$15", sub="toy A", angle=-8)
    return tag(img, 760, 1180, text="$15", sub="toy B", angle=6)
def s2(img, t):
    img = tag(img, 300, 1100, text="$15", sub="toy A", angle=-8, w=280)
    img = tag(img, 780, 1100, text="$15", sub="toy B", angle=6, w=280)
    return cash_stack(img, 540, 1400, t=t, bills=4, label="$20 to spend")
def s3(img, t):
    img = bubble(img, 540, 1080, '"Which one, and why?"', w=700, size=60)
    return tag(img, 540, 1370, text="$15", sub="their pick", angle=-4, w=300)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R007_choice", "music": {"style": "piano", "seed": 707}, "scenes": [
    {"dur": 2.8, "instant": True, "text": "Choices at 6 become habits at *26.*", "size": 88, "draw": s1},
    {"dur": 2.8, "text": "$20. Two $15 toys. *Only one* fits.", "size": 84, "draw": s2},
    {"dur": 3.2, "text": "Don't choose for them. Ask: *which one, why?*", "size": 78, "draw": s3},
    {"dur": 3.2, "text": "Comment *BOOK.* Teach money before money teaches *them.*", "size": 74, "draw": s6},
]}
