from props import *
def a(img): return bubble(img, 540, 1200, '"You\'re too young for money talk."', w=860, size=56, fill=SAND)
def b(img): return bubble(img, 540, 1200, '"Fine, I\'ll pay for it."', w=760, size=64, fill=SAND)
STORIES = [
  {"id": "S20261024a", "kicker": "NEW AT NOON", "text": "What does your kid hear when you say this?", "size": 80, "sub": "And what to say instead.", "draw": a},
  {"id": "S20261024b", "kicker": "TONIGHT 7:30 PM", "text": "What does your kid learn from this?", "size": 80, "sub": "The $3 lesson that saves them later.", "draw": b},
]
