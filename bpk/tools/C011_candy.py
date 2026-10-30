from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to use post-Halloween candy trading to teach value and trade-offs.
def d1(img):
    return jar(img, 540, 930, coins=0, label="CANDY", w=300, h=360)
def d2(img):
    img = swap_card(img, 540, 880, "2 lollipops", "1 chocolate bar")
    d = ImageDraw.Draw(img); pill(d, 540, 1120, "Comment BOOK", size=56, bg=TERRA)
    return img
SPEC = {"id": "C011_candy", "slides": [
    {"text": "Tomorrow your kid gets a *bag of currency.*", "size": 80, "swipe": True,
     "sub": "Halloween candy is a money lesson hiding in plain sight.", "draw": d1},
    {"kicker": "THE FIX", "text": "Let them *trade.*", "size": 88,
     "sub": "Ask: \"Is that a fair trade? Why?\" That's value and trade-offs. Comment *BOOK* before the candy runs out.", "draw": d2},
]}
