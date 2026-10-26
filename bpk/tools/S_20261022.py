from props import *
def a(img): return phone(img, 540, 1180, rows=(("800 coins", "$9.99"),))
def b(img): return meter(img, 540, 1200, start=0, end=0, t=1)
STORIES = [
  {"id": "S20261022a", "kicker": "NEW AT NOON", "text": "Game coins feel *free* to your kid?", "size": 84,
   "sub": "Here's what they really cost.", "draw": a},
  {"id": "S20261022b", "kicker": "TONIGHT 7:30 PM", "text": "$10 in their game wallet. Gone by Friday?", "size": 80,
   "sub": "Two rules that fix it.", "draw": b},
]
