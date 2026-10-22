from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to make a digital purchase feel real by paying once in counted cash.
def d1(img): return phone(img, 540, 900, rows=(("Skin", "$4.99"), ("Coin pack", "$9.99")), tap=True, t=1, w=520, h=640)
def d2(img):
    img = phone(img, 330, 960, rows=(("Skin", "$4.99"),), w=420, h=620)
    return cash_stack(img, 790, 980, bills=5, label="$5", sub="in bills")
def d3(img):
    img = cash_stack(img, 360, 980, bills=5, label="Count it")
    return bubble(img, 760, 900, '"Still want it?"', w=420, size=48)
def d4(img):
    img = cta_scene(img, 540, 1010)
    d = ImageDraw.Draw(img); pill(d, 540, 1170, "Comment BOOK", size=56, bg=TERRA)
    return img
SPEC = {"id": "C003_tap", "slides": [
    {"text": "One tap doesn't feel like *spending.*", "size": 80, "swipe": True,
     "sub": "So does your kid know it is?", "draw": d1},
    {"kicker": "THE TRUTH", "text": "Every tap is *real dollars.*", "size": 78,
     "sub": "$4.99 is five bills from your wallet. So how do they feel that?", "draw": d2},
    {"kicker": "TRY THIS ONCE", "text": "Make them pay in *counted cash.*", "size": 78,
     "sub": "Count it out, hand it over, then ask: still worth it?", "draw": d3},
    {"text": "Their money habits start *now.*", "size": 82,
     "sub": "Comment *BOOK* for the Money Smart Kids Coloring Book link, before the next tap.", "draw": d4},
]}
