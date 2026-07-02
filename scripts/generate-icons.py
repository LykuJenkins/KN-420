#!/usr/bin/env python3
"""Generate PNG icons from the SVG source for PWA + Android."""
from PIL import Image, ImageDraw
import os
import math

REPO_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ICONS_DIR = os.path.join(REPO_DIR, 'icons')
os.makedirs(ICONS_DIR, exist_ok=True)

SIZES = [16, 32, 36, 48, 72, 96, 144, 180, 192, 512]

def make_icon(size, output_path):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    margin = int(size * 0.05)
    radius = int(size * 0.225)
    draw.rounded_rectangle(
        [margin, margin, size - margin, size - margin],
        radius=radius,
        fill=(15, 20, 16, 255)
    )

    cx, cy = size // 2, size // 2
    petal_len = int(size * 0.225)
    petal_wid = int(size * 0.074)
    petal_offset = int(size * 0.215)
    for i in range(7):
        angle = i * (360 / 7)
        petal = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        pdraw = ImageDraw.Draw(petal)
        pdraw.ellipse(
            [cx - petal_wid, cy - petal_offset - petal_len,
             cx + petal_wid, cy - petal_offset + petal_len],
            fill=(74, 222, 128, 255)
        )
        petal = petal.rotate(angle, center=(cx, cy))
        img = Image.alpha_composite(img, petal)

    r = int(size * 0.047)
    d2 = ImageDraw.Draw(img)
    d2.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(163, 230, 53, 255))
    img.save(output_path, 'PNG')
    print(f"  {output_path} ({size}x{size})")

print("Generating PNG icons...")
for size in SIZES:
    make_icon(size, os.path.join(ICONS_DIR, f'icon-{size}.png'))

# Special filenames
make_icon(180, os.path.join(ICONS_DIR, 'apple-touch-icon.png'))

# favicon.ico
ico_sizes = [16, 32, 48]
ico_images = []
for s in ico_sizes:
    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, s, s], radius=max(1, int(s*0.2)), fill=(15, 20, 16, 255))
    d.ellipse([int(s*0.2), int(s*0.2), int(s*0.8), int(s*0.8)], fill=(74, 222, 128, 255))
    ico_images.append(img)
ico_images[0].save(os.path.join(REPO_DIR, 'favicon.ico'), format='ICO', sizes=[(s, s) for s in ico_sizes])
print(f"  favicon.ico")
print("\nDone.")
