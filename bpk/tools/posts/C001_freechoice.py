from props import *
from PIL import ImageDraw

def d1(img):
    img = jar(img, 330, 960, coins=9, label="SAVE")
    img = tag(img, 760, 900, text="$0", sub="on choices", faded=True, angle=6)
    return img
def d2(img):
    img = jar(img, 540, 940, coins=12, label="")
    d = ImageDraw.Draw(img)
    pill(d, 540, 1150, "No choices made = no practice", size=36, bg=INK)
    return img
def d3(img):
    img = card(img, [90, 760, 520, 1180], fill=CREAM); img = card(img, [560, 760, 990, 1180], fill=CREAM)
    d = ImageDraw.Draw(img)
    text_block(d, "*All* save", 305, 800, 48, 380, path=F_XB)
    text_block(d, "Never practices choosing", 305, 900, 38, 360, color=SAGE_D, path=F_BOLD)
    text_block(d, "*All* spend", 775, 800, 48, 380, path=F_XB)
    text_block(d, "Never practices waiting", 775, 900, 38, 360, color=SAGE_D, path=F_BOLD)
    pill(d, 540, 1210, "Kids need reps at both", size=36, bg=SAGE_D)
    return img
def d4(img):
    return split_bar(img, 540, 900, parts=(("Saving goal", 7, SAGE_D), ("Free choice", 3, TERRA)))
def d5(img):
    img = calendar(img, 300, 900, label="1 WEEK LATER", day="7")
    d = ImageDraw.Draw(img); slime(d, 300, 1170, s=.65)
    img = bubble(img, 735, 880, '"Still worth $3?"', w=470, size=46, tail="left")
    img = bubble(img, 735, 1090, '"Would you buy it again?"', w=470, size=40, tail="left")
    return img
def d6(img):
    img = tag(img, 330, 960, text="$3", sub="lesson today", angle=-6)
    img = tag(img, 760, 960, text="$3,000", sub="lesson at 25", faded=True, angle=6, w=380)
    return img
def d7(img):
    return cta_scene(img, 540, 1000)

SPEC = {"id": "C001_freechoice", "slides": [
    {"text": "Making your kid save *every* dollar? Here's what it skips.", "size": 80, "swipe": True,
     "sub": "And a 2-question habit that fixes it.", "draw": d1},
    {"kicker": "WHY IT MATTERS", "text": "Kids learn money by *making choices*.", "size": 74,
     "sub": "If every dollar is locked away, they never practice deciding what's worth it.", "draw": d2},
    {"kicker": "THE MISSING HALF", "text": "Saving is a skill. So is *spending well*.", "size": 74, "draw": d3},
    {"kicker": "TRY THIS", "text": "Give them a small *free choice* share.", "size": 74,
     "sub": "Example: $10 allowance. $7 toward a goal, $3 they can spend on anything.", "draw": d4},
    {"kicker": "THEN ASK", "text": "A week later, ask *two questions*.", "size": 74,
     "sub": "Say they bought $3 of slime. No judging, just curious.", "draw": d5},
    {"kicker": "THE PAYOFF", "text": "Small regrets are *cheap lessons*.", "size": 78,
     "sub": "A $3 \"not worth it\" now teaches what a $3,000 one would later.", "draw": d6},
    {"text": "Want more ways to make money lessons *hands-on*?", "size": 74,
     "sub": "Explore our kids' money activity & coloring book through the link in our bio.", "draw": d7},
]}
