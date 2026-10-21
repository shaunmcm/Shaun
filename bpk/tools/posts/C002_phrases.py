from props import *
# OUTCOME: Parents will be able to swap 2 everyday money phrases for lines that teach instead of shut down.
def sw(old, new): return lambda img: swap_card(img, 540, 900, old, new, t=1)
def d1(img):
    img = bubble(img, 420, 820, '"Money doesn\'t grow on trees."', w=720, size=46, fill=SAND, tail="left")
    img = bubble(img, 640, 1030, '"Save it for a rainy day."', w=660, size=46, fill=SAND, tail="right")
    return img
def d4(img):
    img = cta_scene(img, 540, 1010)
    from PIL import ImageDraw
    d = ImageDraw.Draw(img); pill(d, 540, 1170, "Comment BOOK", size=56, bg=TERRA)
    return img
SPEC = {"id": "C002_phrases", "slides": [
    {"text": "2 money phrases most of us grew up hearing.", "size": 78, "swipe": True,
     "sub": "Are they quietly shutting your kid down?", "draw": d1},
    {"kicker": "PHRASE 1", "text": "It ends the talk. Say *this* instead:", "size": 72,
     "sub": "Now cost has a number. But what about saving?", "draw": sw('"Money doesn\'t grow on trees."', '"Let\'s see how many weeks it costs."')},
    {"kicker": "PHRASE 2", "text": "A \"rainy day\" is too *vague* for a kid.", "size": 72,
     "sub": "A goal they choose makes saving real. Every swap turns \"no\" into a lesson.", "draw": sw('"Save it for a rainy day."', '"What do you want to save for?"')},
    {"text": "Want them practicing these lessons on *paper*?", "size": 76,
     "sub": "Comment *BOOK* for the *Money* *Smart* *Kids* *Coloring* *Book* link. Follow @kids_and_money_554 for daily lessons.", "draw": d4},
]}
