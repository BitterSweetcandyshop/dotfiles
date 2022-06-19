from os import getlogin, path
import subprocess
import datetime
import pylrc

def lrcdl():
    try:
        subprocess.run(["python", f"/home/{os.getlogin()}/.scripts/music/lrcdl.py"])
    except:
        pass


source = open(f"/home/{getlogin()}/.scripts/music/source.txt", "r").read().replace("\n", "")
title = str(subprocess.run(["playerctl", "metadata", "title", "-p", source], capture_output=True).stdout)[2:-3]
artist = str(subprocess.run(["playerctl", "metadata", "artist", "-p", source], capture_output=True).stdout)[2:-3]
position = str(subprocess.run(["playerctl", "position", "-p", source], capture_output=True).stdout)[2:-3]
lrc_path = f"/home/{getlogin()}/.lyrics/{artist} - {title}.lrc"

if not path.exists(lrc_path):
    exit()

cur_base = str(datetime.timedelta(seconds=(float(position.split('.')[0])))).split(':')
cur_seconds = cur_base[2]
cur_minutes = cur_base[1]

file = open(lrc_path, "r")
lines = file.readlines()
file.close()

file = open(f"/home/{getlogin()}/.scripts/resources/line.txt", "r")
now = file.readlines()[0]
file.close()

for line in lines:
    words = line[11:]
    lrc_seconds = line[4:6]
    lrc_minutes = line[1:3]
    if lrc_minutes == cur_minutes and lrc_seconds == cur_seconds and now != words:
        file = open(f"/home/{getlogin()}/.scripts/resources/line.txt", "w")
        if not len(words) > 0: words = " "
        file.write(words)
        file.close()
        exit()
        
