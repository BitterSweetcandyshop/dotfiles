import subprocess
import sys
import os


source = open(f"/home/{os.getlogin()}/.scripts/music/source.txt").read().replace("\n", "")

if not sys.argv[2]:
    exit()
lookup = sys.argv[2]
cmd = sys.argv[1]


# haha spagetttttiiiiiii code
playerctl = ""
# yes I just say try different things, I'll add mpc probs as a backup for mpd
playerctl = subprocess.run(["playerctl", cmd, f"mpris:{lookup}", "-p", source], capture_output=True)
if not playerctl.stdout:
    playerctl = subprocess.run(["playerctl", cmd, lookup, "-p", source], capture_output=True)
if not playerctl.stdout:
    playerctl = playerctl = subprocess.run(["playerctl", cmd, f"xesam:{lookup}", "-p", source], capture_output=True)

try:
    playerctl = str(playerctl.stdout)[2:-3]
    if lookup == "title" and (len(playerctl) > 20):
        playerctl = playerctl[:10] + "..."
    print(playerctl)
except:
    exit() #just give up smh