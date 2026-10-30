from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to turn the costume ask into a budget the kid helps plan.
def s1(img, t): return tag(img, 540, 1200, text="$45", sub="example", angle=-6)
def s2(img, t): return bubble(img, 540, 1200, '"Because I said so."', w=640, size=54, fill=SAND)
def s3(img, t): return budget_card(img, 540, 1240, t=t, title="Costume budget (example)", rows=(("Mask", 10, 10), ("Cape", 8, 8), ("Left over", 7, 0)), highlight=2)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R021_costume", "music": {"style": "playful", "seed": 2121}, "scenes": [
    {"dur": 4.0, "instant": True, "text": "\"Why is the costume so *expensive?*\"", "size": 82,
     "sub": "Don't *dodge* it.", "sub_size": 60, "draw": s1},
    {"dur": 2.6, "text": "\"Because I said so\" *teaches nothing.*", "size": 80, "draw": s2},
    {"dur": 2.8, "text": "Set a *$25 budget.* They plan it.", "size": 80, "draw": s3},
    {"dur": 2.6, "text": "Comment *BOOK* before *trick-or-treat.*", "size": 80, "draw": s6},
]}
