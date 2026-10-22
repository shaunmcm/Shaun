from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to translate game-coin prices into real dollars with their kid.
ROWS = (("800 coins", "$9.99"), ("400-coin skin", "= $5"))
def s1(img, t): return phone(img, 540, 1180, t=t, rows=(("800 coins", "$9.99"),), tap=True)
def s2(img, t):
    img = phone(img, 340, 1180, rows=(("800 coins", "$9.99"),), w=400, h=700)
    return cash_stack(img, 790, 1200, t=t, bills=10, label="$10", sub="real money")
def s3(img, t):
    img = phone(img, 340, 1180, rows=(("400-coin skin", "?"),), w=400, h=700)
    return cash_stack(img, 790, 1200, t=t, bills=5, label="$5", sub="say it out loud")
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R005_coins", "music": {"style": "playful", "seed": 505}, "scenes": [
    {"dur": 2.8, "instant": True, "text": "Game coins feel *free* to your kid?", "size": 86, "draw": s1},
    {"dur": 3.0, "text": "800 coins = *$10* of real money.", "size": 84, "draw": s2},
    {"dur": 3.2, "text": "That 400-coin skin? *$5.* Say it out loud.", "size": 80, "draw": s3},
    {"dur": 3.0, "text": "Their money habits start now. Comment *BOOK.*", "size": 78, "draw": s6},
]}
