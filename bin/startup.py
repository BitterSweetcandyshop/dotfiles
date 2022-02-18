from PIL import Image, ImageFont, ImageDraw, ImageFilter, ImageEnhance
from pynput import keyboard
import subprocess
import textwrap
import time

plain_wallpaper = "/home/bittersweet/Wallpapers/Plain-Black-Wallpaper.webp"
save_path = "/home/bittersweet/Wallpapers/wall_editied.jpg" # Must end in a slash(/)
welcome_text = "Hello BitterSweet"
font_main = ImageFont.truetype("/home/bittersweet/.fonts/PressStart2P-Regular.ttf", 80)
font_small = ImageFont.truetype("/home/bittersweet/.fonts/PressStart2P-Regular.ttf", 30)

def update_wallpaper():
  wallpaper.save(save_path)
  subprocess.run(['feh', '--bg-scale', save_path])

def on_press(key):
    try:
        k = key.char
    except:
        k = key.name
    if k == "media_play_pause":
      time.sleep(0.01)
      subprocess.run(["mpc", "play"])
      wallpaper = Image.open(plain_wallpaper).resize((3840, 2160))
      wallpaper_textable = ImageDraw.Draw(wallpaper)
      wallpaper_textable.text((1920, 1130), "Let's Begin, Shall We?", font=font_main, anchor="mm")
      wallpaper.save(save_path)
      subprocess.run(['feh', '--bg-scale', save_path])
      time.sleep(2)
      subprocess.run(["python", "/home/bittersweet/bin/cover_fancy.py"])
      return False

i = 0
while i < (len(welcome_text) + 1):
  wallpaper = Image.open(plain_wallpaper).resize((3840, 2160))
  wallpaper_textable = ImageDraw.Draw(wallpaper)
  wallpaper_textable.text((1920, 1130), welcome_text[:i], font=font_main, anchor="mm")
  update_wallpaper()
  i += 1


wallpaper = Image.open(save_path).resize((3840, 2160))
wallpaper_textable = ImageDraw.Draw(wallpaper)
wallpaper_textable.text((1920, 1210), "Press Play to Begin", font=font_small, anchor="mm")
update_wallpaper()

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()