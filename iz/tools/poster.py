"""Build the updated Impact Zero poster: no release date, no $6.99 -> 'OUT NOW ON iPHONE' + '$2.99'."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import sys

SRC_POSTER = sys.argv[1]
SRC_BG = sys.argv[2]
OUT = sys.argv[3]

F = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"

p = Image.open(SRC_POSTER).convert("RGB")
W, H = p.size  # 1206 x 2104
bg = Image.open(SRC_BG).convert("RGB")
bg = bg.resize((W, int(bg.height * W / bg.width)))
# patch the bottom 480 px with clean starfield from the key art (flip so cubes don't repeat obviously)
patch_h = 470
import random
random.seed(7)
patch = Image.new("RGB", (W, patch_h), (2, 2, 6))
pd = ImageDraw.Draw(patch)
for _ in range(90):
    x, y = random.randint(0, W), random.randint(0, patch_h)
    r = random.choice([1, 1, 2, 2, 3])
    pd.ellipse([x - r, y - r, x + r, y + r], fill=(255, 255, 255))
# a couple of faint red streaks like the key art
for _ in range(4):
    x, y = random.randint(60, W - 60), random.randint(20, patch_h - 40)
    pd.line([(x, y), (x - 40, y + 70)], fill=(170, 30, 30), width=3)
patch = patch.filter(ImageFilter.GaussianBlur(0.6))
# continue the blue glow blob from the key art across the seam
blob = Image.new("RGB", (W, patch_h), (0, 0, 0))
ImageDraw.Draw(blob).ellipse([1010, -90, 1190, 90], fill=(40, 40, 200))
blob = blob.filter(ImageFilter.GaussianBlur(45))
patch = Image.blend(patch, Image.eval(patch, lambda v: v), 0)  # no-op keep type
from PIL import ImageChops
patch = ImageChops.add(patch, blob)
mask = Image.new("L", (W, patch_h), 255)
md = ImageDraw.Draw(mask)
for y in range(80):
    md.line([(0, y), (W, y)], fill=int(255 * y / 80))
p.paste(patch, (0, H - patch_h), mask)

def hex_box(draw_img, cx, cy, w, h, color=(120, 200, 255)):
    """Draw a glowing hexagonal frame like the original poster."""
    glow = Image.new("RGBA", draw_img.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    k = h // 2
    pts = [(cx - w // 2 + k, cy - h // 2), (cx + w // 2 - k, cy - h // 2), (cx + w // 2, cy),
           (cx + w // 2 - k, cy + h // 2), (cx - w // 2 + k, cy + h // 2), (cx - w // 2, cy)]
    gd.polygon(pts, fill=(0, 0, 0, 170), outline=color + (255,), width=5)
    glow_only = Image.new("RGBA", draw_img.size, (0, 0, 0, 0))
    ImageDraw.Draw(glow_only).polygon(pts, outline=color + (255,), width=9)
    glow_only = glow_only.filter(ImageFilter.GaussianBlur(14))
    draw_img.alpha_composite(glow_only)
    draw_img.alpha_composite(glow)

pr = p.convert("RGBA")
hex_box(pr, W // 2, H - 335, 1000, 120)
hex_box(pr, W // 2, H - 170, 700, 150)
d = ImageDraw.Draw(pr)

def text_glow(img, xy, txt, font, fill, glow=(80, 180, 255)):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    ld.text(xy, txt, font=font, fill=glow + (255,), anchor="mm")
    layer = layer.filter(ImageFilter.GaussianBlur(10))
    img.alpha_composite(layer)
    ImageDraw.Draw(img).text(xy, txt, font=font, fill=fill, anchor="mm")

text_glow(pr, (W // 2, H - 335), "OUT NOW ON iPHONE", ImageFont.truetype(F, 70), (225, 240, 255))
text_glow(pr, (W // 2, H - 172), "$2.99", ImageFont.truetype(F, 120), (255, 255, 255))
pr.convert("RGB").save(OUT, quality=94)
print("saved", OUT)
