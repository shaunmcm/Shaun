from props import *
from PIL import ImageDraw
# OUTCOME: Parents will feel the urgency of early money habits and be able to make one digital purchase feel real (pay in counted cash).
def d1(img): return phone(img, 540, 930, rows=(("Skin", "$4.99"), ("Coin pack", "$9.99")), tap=True, t=1, w=500, h=640)
def d2(img):
    img = cash_stack(img, 330, 960, bills=5, label="$4.99 ≈ 5 bills")
    img = bubble(img, 760, 880, '"Still worth it?"', w=420, size=46)
    d = ImageDraw.Draw(img); pill(d, 540, 1210, "Comment BOOK", size=56, bg=TERRA)
    return img
SPEC = {"id": "C003_tap", "slides": [
    {"text": "Money habits are set by *age 7.*", "size": 86, "swipe": True,
     "sub": "Every tap your kid makes today is practice for later. (Cambridge researchers)", "draw": d1},
    {"kicker": "THE FIX", "text": "Make one tap *feel real.*", "size": 82,
     "sub": "Have them pay in counted cash, one bill at a time. Then ask: still worth it? Comment *BOOK* before the next tap.", "draw": d2},
]}
