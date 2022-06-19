# First host a vercel instance of: https://github.com/raitonoberu/lyricsapi
#The above program will run the backened stuff, I just made a wrapper
from urllib.parse import quote
from datetime import datetime
from os import getlogin, path, remove
import subprocess
import requests
import sys

#add the suffix /api/lyrics? the end of your vercel app url
api = "https://lyricsapi-seven.vercel.app/api/lyrics?"

# change source to %any ig
source = open(f"/home/{getlogin()}/.scripts/music/source.txt", "r").read().replace("\n", "")
title = str(subprocess.run(["playerctl", "metadata", "title", "-p", source], capture_output=True).stdout)[2:-3]
artist = str(subprocess.run(["playerctl", "metadata", "artist", "-p", source], capture_output=True).stdout)[2:-3]
lrc_path = f"/home/{getlogin()}/.lyrics/{artist} - {title}.lrc"

if path.exists(lrc_path):
    exit()

file = open(lrc_path, "w")


resp = requests.get(f"{api}name={quote(title + ' ' + artist)}").json()
if not resp:
    print("Not found.")
    file.close()
    remove(lrc_path)
    exit()

lrc = f"[ti:{title}]\n[ar:{artist}]\n"
for line in resp:
    milli = int(line['time'])
    words = line['words']
    time = datetime.fromtimestamp(milli/1000.0)
    #lrc += f"{time}"
    lrc += f"[{time.strftime('%M:%S:%f')[:8]}] {words}\n"

lrc = lrc[:-1]
file.write(lrc)
file.close()