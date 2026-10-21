"""Plain Story frames (1080x1920). Text in y 300-900, prop 1000-1450, CTA pill near bottom (above reply bar)."""
import os, sys, importlib.util
from PIL import ImageDraw
from style import *

def render(st, out_dir="out"):
    img = background()
    if st.get("draw"): img = st["draw"](img)
    d = ImageDraw.Draw(img)
    brand_tag(d)
    y = 340
    if st.get("kicker"): y = pill(d, W//2, y, st["kicker"], size=36, bg=TERRA) + 30
    y = text_block(d, st["text"], W//2, y, st.get("size", 84), 920)
    if st.get("sub"): text_block(d, st["sub"], W//2, y + 30, 52, 900, color=SAGE_D, path=F_BOLD)
    pill(d, W//2, 1560, "Money Smart Kids Coloring Book · link in bio", size=36, bg=SAGE_D)
    p = os.path.join(out_dir, st["id"] + ".jpg"); img.convert("RGB").save(p, quality=92); return p

if __name__ == "__main__":
    s = importlib.util.spec_from_file_location("m", sys.argv[1]); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    for st in m.STORIES: print(render(st))
