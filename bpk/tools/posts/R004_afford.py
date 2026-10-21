from props import *
from PIL import ImageDraw
# OUTCOME: By the end, parents will know a line that turns "we can't afford it" into a planning lesson.

def s1(img, t):
    return bubble(img, 540, 1200, '"We can\'t afford it."', w=760, size=64, fill=SAND, tail="left")
def s2(img, t):
    return wallet_empty(img, 540, 1220 - 20 * t)
def s3(img, t):
    return swap_card(img, 540, 1220, '"We can\'t afford it."', '"It\'s not in our plan this month."', t=t)
def s4(img, t):
    return budget_card(img, 540, 1190, t=min(1, t*1.2), foot="Toy they want: $30")
def s5(img, t):
    img = budget_card(img, 540, 1190, t=min(1,t*1.5), foot="Toy: $30. Plan it next month?")
    return img
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img

SPEC = {"id": "R004_afford", "music": {"style": "lofi", "seed": 414}, "scenes": [
    {"dur": 3.6, "instant": True, "text": "\"We can't afford it.\"", "size": 96,
     "sub": "What does your kid *hear?*", "sub_size": 60, "draw": s1},
    {"dur": 2.6, "text": "Say: \"It's not in our *plan.*\"", "size": 84, "draw": s3},
    {"dur": 2.8, "text": "Then show the plan: *$12 left.*", "size": 84, "draw": s5},
    {"dur": 2.8, "text": "Comment *BOOK* for the coloring book link.", "size": 76, "draw": s6},
]}
