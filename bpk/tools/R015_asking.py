from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to answer "can I have it?" with "add it to your wish list" instead of shutting it down.
def s1(img, t): return bubble(img, 540, 1200, '"Stop asking for stuff!"', w=760, size=56, fill=SAND)
def s2(img, t): return tag(img, 540, 1200, text="I want...", sub="(keep it secret)", faded=True)
def s3(img, t): return wishlist(img, 540, 1220, items=(("Lego set", "$25"), ("Slime kit", "$8")), title="My wish list", foot="Pick one on payday", hw=380)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R015_asking", "music": {"style": "piano", "seed": 1515}, "scenes": [
    {"dur": 3.4, "instant": True, "text": "\"Stop asking for stuff.\"", "size": 86,
     "sub": "What do they *hear?*", "sub_size": 60, "draw": s1},
    {"dur": 2.6, "text": "They hear: wanting is *bad.*", "size": 86, "draw": s2},
    {"dur": 3.0, "text": "Say: *add it* to your wish list.", "size": 80, "draw": s3},
    {"dur": 3.0, "text": "Comment *BOOK* before the next *\"can I?\"*", "size": 70, "draw": s6},
]}
