from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to split gift money into save and spend before the shopping trip.
def s1(img, t): return wallet_empty(img, 540, 1220, t)
def s2(img, t): return cash_stack(img, 540, 1230, t=t, bills=5, label="$50 birthday money (example)")
def s3(img, t): return split_bar(img, 540, 1220, t=t, parts=(("Save", 25, SAGE_D), ("Spend", 25, TERRA)), total=50)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R018_birthday", "music": {"style": "playful", "seed": 1818}, "scenes": [
    {"dur": 4.0, "instant": True, "text": "Birthday money gone in *one day?*", "size": 84,
     "sub": "Where did it *go?*", "sub_size": 60, "draw": s1},
    {"dur": 2.6, "text": "$50 to *$0* by dinner.", "size": 90, "draw": s2},
    {"dur": 2.8, "text": "Split it *first:* save half, spend half.", "size": 80, "draw": s3},
    {"dur": 2.6, "text": "Comment *BOOK* before the next *party.*", "size": 82, "draw": s6},
]}
