from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to make saved money visible with a monthly balance check.
def d1(img):
    return tag(img, 540, 930, text="$40", sub="where did it go?", faded=True, angle=-6, w=380, h=200)
def d2(img):
    img = calendar(img, 330, 860, label="ONCE A MONTH", day="$52")
    img = bubble(img, 770, 820, '"It grew!"', w=380, size=48)
    d = ImageDraw.Draw(img); pill(d, 540, 1100, "Comment BOOK", size=56, bg=TERRA)
    return img
SPEC = {"id": "C009_bank", "slides": [
    {"text": "\"Just put it in the bank.\"", "size": 84, "swipe": True,
     "sub": "To a kid, money they never see again isn't saved. It's gone.", "draw": d1},
    {"kicker": "THE FIX", "text": "Show the *balance* once a month.", "size": 80,
     "sub": "Check it together monthly (example: $40, then $52). Comment *BOOK* before next payday.", "draw": d2},
]}
