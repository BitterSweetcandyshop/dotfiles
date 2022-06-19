# spotify tidal-hifi and mpd only atm
from urllib.request import urlopen
from time import sleep
import subprocess
import requests
import shutil
import os

# increase this if your cpu starts to hate you,
#the internet check is 2 seconds max, so without internet
#that's a garunteed 2 second delay.
delay = 2

def no_cover():
    print("No cover update")
    shutil.copy(f"/home/{os.getlogin()}/.scripts/resources/no_cover.jpg", f"/home/{os.getlogin()}/.scripts/resources/cover.png")

def lrcdl():
    print("Fetching lyrics")
    try:
        subprocess.run(["python", f"/home/{os.getlogin()}/.scripts/music/lrcdl.py"])
    except:
        pass


# without femdom mommy taking care of me, we know there isn't internet!
#kinky~
def is_internet_porn():
    print("Checking for internet")
    try:
        requests.get("https://google.com")
        return True
        print("There is internet")
    except:
        return False
        print("There is no internet")
        

while True:
    # don't question it,  but just on each loop check for internet
    femdom = is_internet_porn()
    source = open(f"/home/{os.getlogin()}/.scripts/music/source.txt").read().replace("\n", "")
    last = open(f"/home/{os.getlogin()}/.scripts/resources/current.txt", "r").read()

    check_life = (subprocess.run(["playerctl", "status", "-p", source], capture_output=True)).stdout
    # only check while player active
    if len(check_life) <= 3 or str(check_life)[2:-3] == "Stopped":
        no_cover()
        sleep(delay)
        continue
    

    # only update if it's a different track... smart ikr lmao
    layz_title = str(subprocess.run(["playerctl", "metadata", "title", "-p", source], capture_output=True).stdout)[2:-3]
    if (last == layz_title) and (os.path.exists(f"/home/{os.getlogin()}/.scripts/resources/cover.png")):
        sleep(delay)
        continue
    elif (not last == layz_title):
        last = open(f"/home/{os.getlogin()}/.scripts/resources/current.txt", 'w')
        last.write(layz_title)
        last.close()

    art_path = subprocess.run(["python", f"/home/{os.getlogin()}/.scripts/music/playerctl_out.py", "metadata", "artUrl"], capture_output=True)
    if art_path.stderr:
        sleep(delay)
        continue
    

    # makes sure the artUrl is valid
    if not len(str(art_path.stdout)[2:-3].replace("file://", "")): 
        no_cover()
        sleep(delay)
        continue
    

    if source == "mpd":
        print("Mpd update")
        try:
            shutil.copy(str(art_path.stdout)[2:-3].replace("file://", ""), f"/home/{os.getlogin()}/.scripts/resources/cover.png")
            if femdom:
                lrcdl()
        except:
            if not str(check_life)[2:-3] == "Playing":
                no_cover()
        print("Mpd update done")

    # save some cpu ig since this runs A LOT
    if femdom:
        # om checking spotify, good thing this comment is here!
        if source == "spotify" or "ncspot":
            print("Spotify update")
            try:
                cover_web = requests.get(str(art_path.stdout)[2:-3])
                cover = open(f"/home/{os.getlogin()}/.scripts/resources/cover.png", "wb")
                cover.write(cover_web.content)
                cover.close()
                lrcdl()
            except:
                if not str(check_life)[2:-3] == "Playing":
                    no_cover()
            print("Spotify update done")

        # usesless comment to just let you know we're checking tidal for art now
        if source == "tidal-hifi":
            print("Tidal update")
            try:
                # good thing it's localhost so we can just spam it
                tidal_data = requests.get('http://localhost:47836/current').json()
                cover_web = requests.get(tidal_data["image"])
                cover = open(f"/home/{os.getlogin()}/.scripts/resources/cover.png", "wb")
                cover.write(cover_web.content)
                cover.close()
                lrcdl()
            except:
                try:
                    shutil.copy(tidal_data["icon"], f"/home/{os.getlogin()}/.scripts/resources/cover.png")
                    lrcdl()
                except:
                    if not str(check_life)[2:-3] == "Playing":
                        no_cover()
            print("Tidal update done")

    sleep(delay)