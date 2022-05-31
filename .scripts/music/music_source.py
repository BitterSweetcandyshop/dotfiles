import subprocess
import sys
import os

if not (len(sys.argv) - 1):
    print("nope")
    exit()

cmd = sys.argv[1] # 1 or -1
use = int
if cmd == "back":
    use = -1
elif cmd == "next":
    use = 1

players = ["mpd", "tidal-hifi", "spotify", "ncspot",  "%any"]
current_source = open(f"/home/{os.getlogin()}/.scripts/music/source.txt", 'r').read().replace("\n", "") or "%any"
writable_source = open(f"/home/{os.getlogin()}/.scripts/music/source.txt", 'w')


print("Current Player: " + current_source)
wanted_index = players.index(current_source) + use
new_index = int
if current_source == players[-1] and cmd == "next":
    new_index = 0
elif current_source == players[0]and cmd == "back":
    new_index = (len(players) - 1)
else:
    new_index = players.index(current_source) + use

writable_source.write(players[new_index])
writable_source.close()


subprocess.run(["notify-send", "Changed Audio Source", players[new_index]])
