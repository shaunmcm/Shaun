from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to split chores into unpaid family jobs and paid extra jobs.
def s1(img, t): return bubble(img, 540, 1200, '"I\'ll pay you $5 to clean your room."', w=880, size=54, fill=SAND)
def s2(img, t): return tag(img, 540, 1200, text="$5?", sub="to help at home", faded=True)
def s3(img, t):
    img = wishlist(img, 300, 1200, items=(("Make bed", "free"), ("Set table", "free")), title="Family", foot="Everyone helps", hw=250)
    return wishlist(img, 790, 1200, items=(("Wash car", "$5"), ("Rake yard", "$4")), title="Extra", foot="Earn money", hw=250)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R013_chores", "music": {"style": "pluck", "seed": 1111}, "scenes": [
    {"dur": 4.0, "instant": True, "text": "\"I'll pay you to clean up.\"", "size": 82,
     "sub": "What do they *learn?*", "sub_size": 60, "draw": s1},
    {"dur": 2.6, "text": "Now helping needs a *price tag.*", "size": 82, "draw": s2},
    {"dur": 2.8, "text": "Split it: family jobs *free*, extras *paid.*", "size": 78, "draw": s3},
    {"dur": 2.6, "text": "Comment *BOOK* before money teaches *them.*", "size": 72, "draw": s6},
]}
