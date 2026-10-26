from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to set one fixed payday and amount so their kid can plan.
def d1(img):
    img = calendar(img, 330, 940, label="PAYDAY?", day="?")
    return bubble(img, 770, 880, '"Maybe Friday?"', w=420, size=46, fill=SAND)
def d2(img):
    img = calendar(img, 330, 860, label="EVERY FRIDAY", day="$5")
    img = bubble(img, 770, 820, '"I can plan now!"', w=420, size=46)
    d = ImageDraw.Draw(img); pill(d, 540, 1100, "Comment BOOK", size=56, bg=TERRA)
    return img
SPEC = {"id": "C007_payday", "slides": [
    {"text": "\"I'll give you money when I have it.\"", "size": 78, "swipe": True,
     "sub": "No payday means no plan. Kids can't save for money that might not come.", "draw": d1},
    {"kicker": "THE FIX", "text": "Pick one *payday.* Write it down.", "size": 80,
     "sub": "Same day, same amount, every week. Now they can plan. Comment *BOOK* before next payday.", "draw": d2},
]}
