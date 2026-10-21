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
    img = budget_card(img, 540, 1190, t=1, foot="Plan it for November?")
    return img
def s6(img, t):
    return cta_scene(img, 540, 1250, t)

SPEC = {"id": "R004_afford", "music": {"style": "lofi", "seed": 404}, "scenes": [
    {"dur": 4.4, "instant": True, "text": "\"We can't afford it.\"", "size": 90,
     "sub": "What does your kid *really* hear?", "sub_size": 54, "draw": s1},
    {"dur": 5.0, "text": "Some kids hear: money is *scary*.", "size": 76,
     "sub": "So what do you say instead?", "sub_size": 48, "draw": s2},
    {"dur": 5.0, "kicker": "SAY THIS", "text": "\"It's not in our *plan* this month.\"", "size": 76,
     "sub": "But what plan?", "sub_size": 48, "draw": s3},
    {"dur": 6.0, "text": "Show them the plan.", "size": 84,
     "sub": "Example: $40 fun money, $28 spent.", "sub_size": 48, "draw": s4},
    {"dur": 5.4, "text": "$12 left. The toy is *$30.*", "size": 80,
     "sub": "\"Want to plan it for next month?\"", "sub_size": 48, "draw": s5},
    {"dur": 7.6, "text": "Want them practicing plans on *paper*?", "size": 74,
     "sub": "Get the *Money* *Smart* *Kids* *Coloring* *Book*. Link in bio. Follow for more.", "sub_size": 48, "draw": s6},
]}
