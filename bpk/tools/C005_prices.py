from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to start sharing real prices with their kid, one price tag at a time.
def d1(img):
    img = tag(img, 330, 960, text="$ ?", sub="toy", faded=True, angle=-8)
    return tag(img, 760, 960, text="$ ?", sub="groceries", faded=True, angle=6)
def d2(img):
    img = tag(img, 330, 830, text="$4.29", sub="cereal (example)", angle=-6, w=360)
    img = bubble(img, 770, 790, '"A lot or a little?"', w=440, size=46)
    d = ImageDraw.Draw(img); pill(d, 540, 1100, "Comment BOOK", size=56, bg=TERRA)
    return img
SPEC = {"id": "C005_prices", "slides": [
    {"text": "\"Don't worry about what it costs.\"", "size": 80, "swipe": True,
     "sub": "Kids who never see prices grow into adults who never check them. So what should they see?", "draw": d1},
    {"kicker": "THE FIX", "text": "Read one real *price tag* together.", "size": 80,
     "sub": "Say it out loud, then ask: \"Is that a lot or a little?\" Comment *BOOK* before your next shopping trip.", "draw": d2},
]}
