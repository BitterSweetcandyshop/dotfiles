import subprocess
import sys
import os

home = "/home/" + os.getlogin()
dir = sys.argv[1]


res = str(subprocess.run(['du', '-hc', f'{home}{dir}'], capture_output=True)).split("\\n")[-2].split('\\t')[0]

if dir.__contains__("Hentai"):
    res = str(int(res[:-1])/2) + "G"

print(res)