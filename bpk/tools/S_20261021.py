from props import *
def j(img): return coin_jar_line(img, 470, 1200, t=1, start=0, end=.5, amount_to=7.5, day_to=30)
def b(img): return bubble(img, 540, 1200, '"We can\'t afford it."', w=760, size=64, fill=SAND)
STORIES = [
  {"id": "S20261021a", "kicker": "NEW AT NOON", "text": "\"A penny saved is a penny earned.\"", "size": 80,
   "sub": "So why do kids ignore it? The fix takes 25¢ a day.", "draw": j},
  {"id": "S20261021b", "kicker": "TONIGHT 7:30 PM", "text": "What does your kid hear when you say this?", "size": 80,
   "sub": "And the one line to say instead.", "draw": b},
]
