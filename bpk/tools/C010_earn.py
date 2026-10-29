from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to offer one small paid extra job so their kid feels what a dollar costs.
def d1(img):
    return tag(img, 540, 930, text="$5", sub="just handed over", faded=True, angle=-6, w=380, h=200)
def d2(img):
    img = wishlist(img, 540, 900, items=(("Sort recycling", "$2"), ("Wash the car", "$5")), title="Extra jobs (example)", foot="Paid on payday", hw=420)
    d = ImageDraw.Draw(img); pill(d, 540, 1150, "Comment BOOK", size=56, bg=TERRA)
    return img
SPEC = {"id": "C010_earn", "slides": [
    {"text": "Has your kid ever *earned* a dollar?", "size": 76, "swipe": True,
     "sub": "A dollar handed over and a dollar earned feel different to a kid.", "draw": d1},
    {"kicker": "THE FIX", "text": "Add one small *paid* job.", "size": 82,
     "sub": "Beyond family chores. Comment *BOOK* to teach what a dollar costs.", "draw": d2},
]}
