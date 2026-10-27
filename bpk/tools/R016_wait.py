from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to use a one-night wait rule for wants.
def s1(img, t): return calendar(img, 540, 1200, label="WAIT", day="24h")
def s2(img, t): return tag(img, 540, 1200, text="$15", sub="toy (example)", angle=-6)
def s3(img, t):
    img = calendar(img, 330, 1200, label="TONIGHT", day="?")
    return bubble(img, 760, 1160, '"Still want it?"', w=400, size=46)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R016_wait", "music": {"style": "lofi", "seed": 1616}, "scenes": [
    {"dur": 4.0, "instant": True, "text": "Can your kid wait *24 hours?*", "size": 84,
     "sub": "Impulse buys start *young.*", "sub_size": 60, "draw": s1},
    {"dur": 2.6, "text": "\"I need it *NOW!*\"", "size": 90, "draw": s2},
    {"dur": 2.8, "text": "Rule: wants wait *one night.*", "size": 84, "draw": s3},
    {"dur": 2.6, "text": "Comment *BOOK.* Teach the wait *now.*", "size": 82, "draw": s6},
]}
