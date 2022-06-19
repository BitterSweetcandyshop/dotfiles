import shutil
import sys
import os

# Home directory
home = f"/home/{os.getlogin()}/"
# Programs to allow backup
backup_following = ['conky', 'dunst', 'eww', 'polybar', 'neofetch', 'rofi', 'cava', 'alacritty', 'picom']
# Dict of program name (used above) and path
book = {
    'conky': {'type': 'dir', 'path': '.config/conky'},
    'dunst': {'type': 'dir', 'path': '.config/dunst'},
    'eww': {'type': 'dir', 'path': '.config/eww'},
    'polybar': {'type': 'dir', 'path': '.config/polybar'},
    'neofetch': {'type': 'dir', 'path': '.config/neofetch'},
    'rofi': {'type': 'dir', 'path': '.config/rofi'},
    'cava': {'type': 'dir', 'path': '.config/cava'},
    'mpDris2': {'type': 'dir', 'path': '.config/mpDris2'},
    'powercord': {'type': 'dir', 'path': '.config/powercord/src/Powercord/themes/Bloop/bloop-config.css'},
    'alacritty': {'type': 'file', 'path': '.config/alacritty.yml'},
    'bettlerlockscreenrc': {'type': 'file', 'path': '.config/betterlockscreenrc'},
    'picom': {'type': 'file', 'path': '.config/picom.conf'},
}

theme_now = open("resources/themes/theme_now.txt", "r").read()
print("Current theme: " + theme_now)

action = input("What action, new themes run backup <(b)ackup/(a)pply>: ").lower()
if not (action == "b" or "backup" or "a" or "apply"):
    print("Invalid choice.")
    exit()

theme = input("What is the theme to use for this action?: ").lower()
if not os.path.exists(f"resources/themes/{theme}/.exsits"):
    make_theme_confirm = input("Theme does not exsist. Create new theme? (y/n): ")
    if make_theme_confirm == "n":
        exit()
    elif make_theme_confirm == "y":
        os.mkdir(f"resources/themes/{theme}/")
        fp = open(f"resources/themes/{theme}/.exsits", 'x')
        fp.close()
        print(f"Made new theme '{theme}'.")
    else:
        print("Invalid choice.")
        exit()


for program in backup_following:
    source = home + book[program]["path"]
    dest = f"resources/themes/{theme}/{program}"
    if book[program]["type"] == "dir":
        if os.path.exists(dest): shutil.rmtree(dest)
        shutil.copytree(source, dest)
    if book[program]["type"] == "file":
        if os.path.exists(dest):  os.remove(dest)
        shutil.copy(source, f"resources/themes/{theme}/")
    print("copied " + program)
