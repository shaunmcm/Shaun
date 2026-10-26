from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to run a $3 grocery-store game that makes their kid separate needs from wants.
def d1(img):
    return wishlist(img, 540, 930, items=(("Milk", "need"), ("Bread", "need"), ("Candy", "want")), title="Grocery list", foot="Aisle 5")
def d2(img):
    img = cash_stack(img, 300, 860, bills=3, label="$3 budget")
    img = wishlist(img, 760, 850, items=(("Apples", "need"), ("Gum", "want")), title="Their job", foot="1 want that fits", hw=280)
    d = ImageDraw.Draw(img); pill(d, 540, 1130, "Comment BOOK", size=56, bg=TERRA)
    return img
SPEC = {"id": "C004_aisle", "slides": [
    {"text": "Rich habits don't start with a paycheck. They start in *aisle 5.*", "size": 76, "swipe": True,
     "sub": "The grocery store is your kid's first money classroom.", "draw": d1},
    {"kicker": "THE FIX", "text": "Hand them *$3* and the list.", "size": 80,
     "sub": "Needs go in the cart first. Then they pick one want that still fits. Comment *BOOK* before your next store run.", "draw": d2},
]}
