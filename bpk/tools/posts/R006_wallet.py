from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to set a monthly game-money cap plus a payday wish list.
def s1(img, t): return meter(img, 540, 1180, t=t, start=10, end=0)
def s2(img, t): return meter(img, 540, 1180, t=t, start=0, end=10, title="New rule: $10 cap a month (example)")
def s3(img, t): return wishlist(img, 540, 1200, t=t)
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R006_wallet", "music": {"style": "lofi", "seed": 606}, "scenes": [
    {"dur": 3.2, "instant": True, "text": "$10 in their game wallet. *Gone* by Friday?", "size": 84, "draw": s1},
    {"dur": 2.8, "text": "Set a *$10* monthly cap. Then stop.", "size": 82, "draw": s2},
    {"dur": 2.8, "text": "Wish list first. Buy only *on payday.*", "size": 82, "draw": s3},
    {"dur": 3.2, "text": "Comment *BOOK.* Give them lessons we never *got.*", "size": 76, "draw": s6},
]}
