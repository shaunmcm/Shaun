from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to give one shared money answer by pointing to the family plan.
def s1(img, t):
    img = bubble(img, 330, 1170, '"Ask your dad."', w=420, size=50, fill=SAND)
    return bubble(img, 760, 1290, '"Ask your mom."', w=420, size=50, fill=SAND, tail="right")
def s2(img, t): return tag(img, 540, 1200, text="Yes? No?", sub="depends", faded=True)
def s3(img, t): return budget_card(img, 540, 1240, t=t, title="Our family plan (example)", rows=(("Treats", 20, 15), ("Toys", 30, 30)), highlight=0)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R020_askdad", "music": {"style": "lofi", "seed": 2020}, "scenes": [
    {"dur": 3.6, "instant": True, "text": "\"Ask your dad.\"", "size": 92,
     "sub": "What does your kid *learn?*", "sub_size": 60, "draw": s1},
    {"dur": 2.6, "text": "The answer *depends who you ask.*", "size": 82, "draw": s2},
    {"dur": 3.2, "text": "One answer: \"Let's check our *plan.*\"", "size": 78, "draw": s3},
    {"dur": 2.6, "text": "Comment *BOOK.* One family, one *plan.*", "size": 80, "draw": s6},
]}
