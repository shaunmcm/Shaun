from props import *
def a(img):
    img = tag(img, 330, 1200, text="$15", sub="toy A", angle=-8)
    return tag(img, 760, 1200, text="$15", sub="toy B", angle=6)
def b(img): return bubble(img, 540, 1200, '"Buy me that!"', w=600, size=72, fill=SAND)
STORIES = [
  {"id": "S20261023a", "kicker": "NEW AT NOON", "text": "Choices at 6 become habits at 26.", "size": 84,
   "sub": "$20, two $15 toys. What do you do?", "draw": a},
  {"id": "S20261023b", "kicker": "TONIGHT 7:30 PM", "text": "Broke habits start in the checkout line.", "size": 80,
   "sub": "One question that changes it.", "draw": b},
]
