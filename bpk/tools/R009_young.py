from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to replace "you're too young for money talk" with a tiny real-money task (counting the change).
def s1(img, t): return bubble(img, 540, 1200, '"You\'re too young for money talk."', w=860, size=56, fill=SAND)
def s2(img, t):
    img = wallet_empty(img, 540, 1200)
    return img
def s3(img, t):
    img = bubble(img, 540, 1060, '"Help me count the change?"', w=760, size=56)
    ov = Image.new("RGBA", img.size, (0,0,0,0)); d = ImageDraw.Draw(ov)
    n = int(1 + 3 * min(1, t * 1.5))
    for i in range(n): coin(d, 360 + i * 120, 1350, r=48, label=["25¢","25¢","10¢","5¢"][i])
    return Image.alpha_composite(img, ov)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R009_young", "music": {"style": "piano", "seed": 909}, "scenes": [
    {"dur": 4.0, "instant": True, "text": "\"You're too young for money talk.\"", "size": 82,
     "sub": "What do they *hear?*", "sub_size": 60, "draw": s1},
    {"dur": 2.6, "text": "They hear: money isn't for *me.*", "size": 84, "draw": s2},
    {"dur": 2.6, "text": "Try: \"Help me count the *change.*\"", "size": 82, "draw": s3},
    {"dur": 2.8, "text": "Their money habits start now. Comment *BOOK.*", "size": 78, "draw": s6},
]}
