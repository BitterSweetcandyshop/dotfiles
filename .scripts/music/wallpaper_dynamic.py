# Changes the white in juuzou wallpaper to match album art
from subprocess import run
from PIL import Image
from sys import argv
import numpy as np
from os import remove
import time

fallback = [255, 255, 255] # default
wal = Image.open(f"/home/bittersweet/Wallpapers/favs/cat_juzo.png")


scheme = str(run(['magick', 'convert', '/home/bittersweet/.scripts/resources/cover.png[0]', '-colors', '3', '-unique-colors', 'txt:-'], capture_output=True).stdout)
color = fallback
try:
    color = scheme.split("\\n")[1].split(" ")[1][1:-1].split(",")
except:
    pass
if len(color) < 2: color = fallback

im = wal.convert('RGBA')
data = np.array(im)
red, green, blue, alpha = data.T

target_areas = (red > 25) & (green > 25) & (blue > 35)
correction = (red < 25) & (green < 25) & (blue < 35)

data[..., :-1][target_areas.T] = (color[0], color[1], color[2])
#data[..., :-1][correction.T] = (22, 19, 35)

im2 = Image.fromarray(data)

try:
    remove("/home/bittersweet/.scripts/resources/dynamic_wallpaper.png")
    im2.save("/home/bittersweet/.scripts/resources/dynamic_wallpaper.png")
    run(["feh", "--bg-scale", "/home/bittersweet/.scripts/resources/dynamic_wallpaper.png"])
except:
    pass