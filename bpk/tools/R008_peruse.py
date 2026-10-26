from props import *
from PIL import ImageDraw
# OUTCOME: Parents will be able to turn "buy me that" into "is it worth it?" with a price-per-use check.
def uses_card(img, cx, cy, item, price, uses, per, hl=False, alpha=255):
    img = card(img, [cx - 220, cy - 190, cx + 220, cy + 190], fill=(SAND if hl else CREAM))
    d = ImageDraw.Draw(img)
    text_block(d, item, cx, cy - 165, 44, 400, path=F_BOLD)
    text_block(d, f"{price} · {uses} uses", cx, cy - 90, 40, 400, color=SAGE_D, path=F_BOLD)
    text_block(d, per, cx, cy - 10, 76, 420, color=(TERRA if hl else SAGE_D), path=F_XB)
    text_block(d, "per use", cx, cy + 90, 36, 400, color=SAGE_D, path=F_BOLD)
    return img
def s1(img, t):
    return bubble(img, 540, 1200, '"Buy me that!"', w=600, size=72, fill=SAND)
def s2(img, t):
    img = tag(img, 540, 1140, text="$12", sub="new toy", angle=-6)
    return bubble(img, 540, 1440, '"How many times will you use it?"', w=860, size=46)
def s3(img, t):
    img = uses_card(img, 300, 1220, "Flashy toy", "$12", 2, "$6", hl=True)
    if t > .35:
        img = uses_card(img, 780, 1220, "Soccer ball", "$20", 40, "50¢")
    return img
def s6(img, t):
    img = cta_scene(img, 540, 1200, t)
    d = ImageDraw.Draw(img); pill(d, 540, 1380, 'Comment BOOK', size=60, bg=TERRA, alpha=int(255*min(1, t*3)))
    return img
SPEC = {"id": "R008_peruse", "music": {"style": "pluck", "seed": 808}, "scenes": [
    {"dur": 2.8, "instant": True, "text": "Broke habits start in the *checkout line.*", "size": 86, "draw": s1},
    {"dur": 3.2, "text": "Ask one question before they *buy:*", "size": 84, "draw": s2},
    {"dur": 3.2, "text": "$12 toy, 2 uses = *$6 a play.*", "size": 84, "draw": s3},
    {"dur": 2.8, "text": "Their money habits start now. Comment *BOOK.*", "size": 78, "draw": s6},
]}
