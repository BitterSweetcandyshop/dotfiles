# spotify tidal-hifi and mpd only atm

from time import sleep
import subprocess
import requests
import shutil
import os

def no_cover():
    shutil.copy(f"/home/{os.getlogin()}/.scripts/resources/no_cover.jpg", f"/home/{os.getlogin()}/.scripts/resources/cover.png")

while True:
    source = open(f"/home/{os.getlogin()}/.scripts/music/source.txt").read().replace("\n", "")
    last = open(f"/home/{os.getlogin()}/.scripts/resources/current.txt", "r").read()

    check_life = (subprocess.run(["playerctl", "status", "-p", source], capture_output=True)).stdout
    # only check while player active
    if len(check_life) <= 3 or str(check_life)[2:-3] == "Stopped":
        no_cover()
        continue

    # only update if it's a different track... smart ikr lmao
    layz_title = str(subprocess.run(["playerctl", "metadata", "title", "-p", source], capture_output=True).stdout)[2:-3]
    if (last == layz_title) and (os.path.exists(f"/home/{os.getlogin()}/.scripts/resources/cover.png")):
        continue
    elif (not last == layz_title):
        last = open(f"/home/{os.getlogin()}/.scripts/resources/current.txt", 'w')
        last.write(layz_title)
        last.close()

    art_path = subprocess.run(["python", f"/home/{os.getlogin()}/.scripts/music/playerctl_out.py", "metadata", "artUrl"], capture_output=True)
    if art_path.stderr:
        continue

    if not len(str(art_path.stdout)[2:-3].replace("file://", "")): 
        no_cover()
        continue

    if source == "mpd":
        shutil.copy(str(art_path.stdout)[2:-3].replace("file://", ""), f"/home/{os.getlogin()}/.scripts/resources/cover.png")

    if source == "spotify":
        try:
            cover_web = requests.get(str(art_path.stdout)[2:-3])
            cover = open(f"/home/{os.getlogin()}/.scripts/resources/cover.png", "wb")
            cover.write(cover_web.content)
            cover.close()
        except:
            if not str(check_life)[2:-3] == "Playing":
                no_cover()
            continue

    if source == "tidal-hifi":
        try:
            tidal_data = requests.get('http://localhost:47836/current').json()
            cover_web = requests.get(tidal_data["image"])
            cover = open(f"/home/{os.getlogin()}/.scripts/resources/cover.png", "wb")
            cover.write(cover_web.content)
            cover.close()
        except:
            try:
                shutil.copy( tidal_data["icon"], f"/home/{os.getlogin()}/.scripts/resources/cover.png")
            except:
                if not str(check_life)[2:-3] == "Playing":
                    no_cover()
                continue
    
    # increase this if your cpu starts to hate you
    sleep(1)