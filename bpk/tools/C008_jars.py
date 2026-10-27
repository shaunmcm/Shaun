from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to set up save / spend / give jars so saving happens first.
def d1(img):
    return jar(img, 540, 930, coins=3, label="ALL MONEY", w=300, h=360)
def d2(img):
    for x, l, n in ((250, "SAVE", 2), (540, "SPEND", 2), (830, "GIVE", 1)):
        img = jar(img, x, 880, coins=n, label=l, w=220, h=270)
    d = ImageDraw.Draw(img); pill(d, 540, 1130, "Comment BOOK", size=56, bg=TERRA)
    return img
SPEC = {"id": "C008_jars", "slides": [
    {"text": "Your kid's piggy bank has *one slot.* That's the problem.", "size": 76, "swipe": True,
     "sub": "One jar means every dollar is spending money, until it's gone.", "draw": d1},
    {"kicker": "THE FIX", "text": "Use *three jars:* Save, Spend, Give.", "size": 78,
     "sub": "Example: $5 = $2 save, $2 spend, $1 give. Saving happens first. Comment *BOOK* before next payday.", "draw": d2},
]}
