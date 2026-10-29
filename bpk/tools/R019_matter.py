from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to replace "money doesn't matter" with "money is a tool" and one real example.
def s1(img, t): return bubble(img, 540, 1200, '"Money doesn\'t matter."', w=720, size=56, fill=SAND)
def s2(img, t): return wallet_empty(img, 540, 1220, t)
def s3(img, t): return budget_card(img, 540, 1240, t=t, title="This week (example)", rows=(("Groceries", 80, 80), ("Gas", 40, 40), ("Fun money", 20, 12)), highlight=2)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R019_matter", "music": {"style": "piano", "seed": 1919}, "scenes": [
    {"dur": 3.6, "instant": True, "text": "\"Money doesn't matter.\"", "size": 88,
     "sub": "What does your kid *hear?*", "sub_size": 60, "draw": s1},
    {"dur": 2.6, "text": "Don't bother *learning it.*", "size": 86, "draw": s2},
    {"dur": 3.2, "text": "Say: money is a *tool.* Watch me.", "size": 78, "draw": s3},
    {"dur": 2.6, "text": "Comment *BOOK.* Start *tonight.*", "size": 80, "draw": s6},
]}
