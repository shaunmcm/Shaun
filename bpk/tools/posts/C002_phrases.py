from props import *
from PIL import ImageDraw
# OUTCOME: By the end, parents will be able to swap 5 everyday money phrases for lines that teach instead of shut down.

def sw(old, new):
    return lambda img: swap_card(img, 540, 920, old, new, t=1)
def d1(img):
    img = bubble(img, 400, 760, '"Money doesn\'t grow on trees."', w=700, size=44, fill=SAND, tail="left")
    img = bubble(img, 640, 930, '"Save it for a rainy day."', w=640, size=44, fill=SAND, tail="right")
    img = bubble(img, 420, 1100, '"Don\'t worry, that\'s my job."', w=700, size=44, fill=SAND, tail="left")
    return img

SPEC = {"id": "C002_phrases", "slides": [
    {"text": "5 money phrases kids hear *every week*.", "size": 78, "swipe": True,
     "sub": "Which one did you grow up with?", "draw": d1},
    {"kicker": "PHRASE 1", "text": "It ends the talk. Try *this* instead:", "size": 70,
     "sub": "Next: the one that makes saving feel pointless.",
     "draw": sw('"Money doesn\'t grow on trees."', '"Let\'s see how many weeks it costs."')},
    {"kicker": "PHRASE 2", "text": "A \"rainy day\" is too *vague* for a kid.", "size": 70,
     "sub": "Next: the one that keeps kids out of money talk.",
     "draw": sw('"Save it for a rainy day."', '"What do you want to save for?"')},
    {"kicker": "PHRASE 3", "text": "Kids learn money by *watching* it happen.", "size": 70,
     "sub": "Next: the one about cards.",
     "draw": sw('"Don\'t worry, that\'s my job."', '"Help me pick the better deal?"')},
    {"kicker": "PHRASE 4", "text": "Cards can look like *free money* to kids.", "size": 70,
     "sub": "Next: the one most families never say out loud.",
     "draw": sw('"Just put it on the card."', '"The card spends money we have to pay."')},
    {"kicker": "PHRASE 5", "text": "Silence teaches that money is *scary*.", "size": 72,
     "sub": "The pattern: every swap turns \"no\" into a lesson.",
     "draw": sw('"We don\'t talk about money."', '"Ask me anything about money."')},
    {"text": "Want them practicing these lessons on *paper*?", "size": 74,
     "sub": "Get the *Money* *Smart* *Kids* *Coloring* *Book*. Link in bio. Follow @kids_and_money_554 for daily lessons.",
     "draw": lambda img: cta_scene(img, 540, 1000)},
]}
