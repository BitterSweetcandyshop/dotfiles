#!/usr/bin/env python3.10

# dumb ass credit title I was told I should start using smh
# A BitterSweet
#       ▄▄█▀▀▀▄█                      ▀██             ▄█▀▀▀▄█  ▀██
#     ▄█▀     ▀   ▄▄▄▄   ▄▄ ▄▄▄     ▄▄ ██   ▄▄▄▄ ▄▄▄  ██▄▄  ▀   ██ ▄▄     ▄▄▄   ▄▄▄ ▄▄▄
#     ██         ▀▀ ▄██   ██  ██  ▄▀  ▀██    ▀█▄  █    ▀▀███▄   ██▀ ██  ▄█  ▀█▄  ██▀  ██
#     ▀█▄      ▄ ▄█▀ ██   ██  ██  █▄   ██     ▀█▄█   ▄     ▀██  ██  ██  ██   ██  ██    █
#      ▀▀█▄▄▄▄▀  ▀█▄▄▀█▀ ▄██▄ ██▄ ▀█▄▄▀██▄     ▀█    █▀▄▄▄▄█▀  ▄██▄ ██▄  ▀█▄▄█▀  ██▄▄▄▀
#                                           ▄▄ █                                 ██
#                                            ▀▀                                 ▀▀▀▀
#                                                                                     script
#reddit: BitterSweetcandyshop
#github: BitterSweetcandyshop
#discord: BitterSweet#1337
#revolt: @BitterSweet
#matrix: bittersweetcandyshop

# IMPORTANT IMPORTANT IMPORTANT IMPORTANT
# You MUST check the directories n' shit bfore running this!
# YOU MUST HAVE THE COVER ART IN THE SAME DIRECTORY AS THE SONG FILE
# THIS USES MPC URIs

# I'd think this would kill my cpu but it didn't somehow, idek
# Uses mpc uris, cope with it
# check the imports to make sure you have enything

from PIL import Image, ImageFont, ImageDraw, ImageFilter, ImageEnhance
from tabulate import tabulate
from pynput import mouse
from time import sleep
import subprocess
import shutil
import os

# yes the location of the '/' matters here bc I'm too lazy to code a handler for it
## IMPORTANT
music_dir = "/Music/"
cover_art_name = "/cover.jpg"
nothing_playing_cover = "/.config/eww/images/image.jpg"
# Where to store the cover art that will be used, copies from music_dir/cover_art_name
store_cover = "/.config/eww/images/cover.png"

## Misc
username = "/home/" + os.getlogin() # If you get an error try changing this to your /home/"username".
# "none": Don't show feats
# "normal": Show it by song name
# "newline": show it on a different line
feat_style = "normal"
show_explicit = False

## Progress Bar
show_progress = True # Show progress bar and time thing
pixels_per_percent = 7.5 # For each percent of the song, move this many pixels
update_time = 0.5 # .5 = ~2secs | 1 = ~5secs | below .3 may have image tearing issues
# hex (0xHEXHEX), rgb[a] (R, G, B, [A]), string "red"
progress_color = (255, 255, 255)

## Album Arr
border_radius = 7
click_pause = False # STUPID - If you click on mini album art, pause music (yes, even through windows)

## Fonts
title_font = ImageFont.truetype(username + "/.fonts/PressStart2P-Regular.ttf", 60)
small_font = ImageFont.truetype(username + "/.fonts/PressStart2P-Regular.ttf", 30)
# hex (0xHEXHEX), rgb[a] (R, G, B, [A]), string "red"
font_color = (255, 255, 255)

## Background ( Wallpaper)
# "album": use the cover art and apply blur
# file path: use the provided image and do cool shit
background = "/Wallpapers/cat_juzo.png"
blur_amount = 15 # mixes box and gaus blur for best result
dimmness = 0.9 # 0 = more dim | 1 = normal | < 1 = brighter

## Queue - this totally breaks with unkown characters btw, idgaf, why enabe this?
# False: Don't show next song(s)
# "next": Only show next song
# "queue": Show next five songs (does not work with random mode, honestly shitty)
future = False


# that magical line where you can't do 
#shit below here unless you're smart or something broke

saved_song = str(subprocess.run(["mpc", "current"], stdout=subprocess.PIPE).stdout)


# Album click
def on_click(x, y, button, pressed):
    if pressed:
        if (1399 < x < 1750) and (849 < y < 1220):
            subprocess.run(["mpc", "toggle"])
        return True

if click_pause:
    listener = mouse.Listener(on_click=on_click)
    listener.start()

def add_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

while True:

    # Get the path from music database and copy it to eww images folder
    cover_path = subprocess.run(['mpc', 'current', '-f', "%file%"], stdout=subprocess.PIPE)
    cover_path = music_dir + "/".join(str(cover_path.stdout)[2:-3].split("/")[:-1]) + cover_art_name
    if background == "album":
        background = cover_path
    try:
        shutil.copy(username + cover_path, username + store_cover)
    except:
        shutil.copy(username + nothing_playing_cover, username + store_cover)

    # Get the cover ready
    cover = Image.open(username + background)
    darkener = ImageEnhance.Brightness(cover)
    cover = darkener.enhance(dimmness)
    cover = cover.filter(ImageFilter.BoxBlur(blur_amount/2))
    cover = cover.filter(ImageFilter.GaussianBlur(blur_amount))
    cover = cover.resize((3840, 2160))

    # Is paused?
    try:
        paused = str(subprocess.run(["mpc"], stdout=subprocess.PIPE).stdout).split("\\n")[1].split(" ")[0][1:-1]
    except:
        paused = False

    # Get Progress
    try:
        progress = str(subprocess.run(["mpc"], stdout=subprocess.PIPE).stdout).split("\\n")[1].split(" ")
        # mpc bullshit
        if paused == "paused":
            progress_percent = int(progress[6][1:-2]) * pixels_per_percent
            progress_fancy = progress[5]
        else:
            progress_percent = int(progress[5][1:-2]) * pixels_per_percent
            progress_fancy = progress[4]
    except:
        progress_percent = 1
        progress_fancy = "0:00/0:00"

    # Get the Song Name, Artist, Feat., and remove explicit
    song_name = subprocess.run(['mpc', 'current'], stdout=subprocess.PIPE)
    try: 
        artist_name, song_name = str(song_name.stdout)[2:-3].split(" - ")
        if not show_explicit:
            song_name = song_name.replace("(Explicit)", "")
        try:
            song_name, feat = song_name.split("(feat.")[0], "(feat." + song_name.split("(feat. ")[1][:-1] + ")"
        except:
            feat = ""
    except:
        artist_name, song_name, feat = "Nothing Playing", "", ""

    # Modify the mini cover
    cover_mini = Image.open(username + "/.config/eww/images/cover.png")
    cover_mini.thumbnail((350, 350))
    cover_mini = add_corners(cover_mini, border_radius)

    # Modify mini cover if paused
    if paused == "paused":
        darkener = ImageEnhance.Brightness(cover_mini)
        cover_mini = darkener.enhance(0.75)
        ImageDraw.Draw(cover_mini).text((175, 195), "||", font=title_font, fill=font_color, anchor="mm")
        ImageDraw.Draw(cover_mini).text((175, 155), "||", font=title_font, fill=font_color, anchor="mm")
    
    # Progress bar
    if progress_percent and show_progress:
        ImageDraw.Draw(cover).line([(1800, 1175), ((1800 + 100*pixels_per_percent), 1175)], width=5)
        ImageDraw.Draw(cover).line([(1800, 1175), ((1800 + progress_percent), 1175)], width=50, fill=progress_color)
        ImageDraw.Draw(cover).text(((1800 + 100*pixels_per_percent), 1100), progress_fancy, font=small_font, anchor="rm")

    # Add Artist, Title, Mini Cover
    if feat_style == "normal":
        song_name = song_name + feat
        ImageDraw.Draw(cover).text((1800,920), artist_name, font=title_font, fill=font_color)
        pass
    elif feat_style == "newline":
        ImageDraw.Draw(cover).text((1800,920), feat, font=small_font, fill=font_color)
        ImageDraw.Draw(cover).text((1800,970), artist_name, font=title_font, fill=font_color)
    elif feat_style == "none":
        ImageDraw.Draw(cover).text((1800,920), artist_name, font=title_font, fill=font_color)
    ImageDraw.Draw(cover).text((1800,850), song_name, font=title_font, fill=font_color)
    cover.paste(cover_mini, (1400, 850))

    # Add Queue
    if future == "queue":
        song_name = str(subprocess.run(['mpc', 'current'], stdout=subprocess.PIPE).stdout)[2:-3]
        playlist = str(subprocess.run(["mpc", "playlist"], stdout=subprocess.PIPE).stdout).split(song_name + "\\n")
        try:
            playlist = playlist[1].replace("\\n\"", "").split("\\n")[:5]
        except:
            playlist = playlist[0][2:-2].split("\\n")[:5]
            pass

        for index, song in enumerate(playlist):
            try: 
                playlist[index] = [song.split(" - ")[0], song.split(" - ")[1].replace(" (Explicit)", "")]
                if len(playlist[index][1]) > 14:
                    playlist[index][1] = playlist[index][1][:12] + "..."
                if len(playlist[index][0]) > 14:
                    playlist[index][0] = playlist[index][0][:12] + "..."
            except:
                pass
            
        playlist_formatted = tabulate(playlist, headers=["Artist", "Title"], tablefmt="github")

        ImageDraw.Draw(cover).text((3840, 2150), playlist_formatted, font=small_font, anchor="rd")
    elif future == "next":
        nextup = str(subprocess.run(["mpc", "queued"], stdout=subprocess.PIPE).stdout)[2:-3]
        if len(nextup) < 3:
            nextup = "Nothing"
        if not show_explicit:
            nextup = nextup.replace("(Explicit)", "")
        ImageDraw.Draw(cover).text((3830, 2150), ("Next: " + nextup), font=small_font, anchor="rd")


    # Set as wallpaper
    cover.save(username + "/.config/eww/images/cover_fancy.png")
    subprocess.run(['feh', '--bg-scale', username + "/.config/eww/images/cover_fancy.png"])

    # pywal update
    def update_change():
        # wal
        subprocess.run(["wal", "-c"])
        subprocess.run(["wal", "-i", (username + "/.config/eww/images/cover.png"), "-n", "-q", "-s"])
        # discord
        pywalCSS = open(username + "/.cache/wal/colors.css").read()
        discord = open(username + "/.config/powercord/src/Powercord/themes/Bloop/bloop-config.css").read()
        with open(username + "/.config/powercord/src/Powercord/themes/Bloop/bloop-pywal.css", "w") as fp:
            fp.write("\n\n".join([discord, pywalCSS]))
        # cli-visualizer
        shutil.copy(username + "/.cache/wal/colors", username + "/.config/vis/colors/pywal")

    song = str(subprocess.run(["mpc", "current"], stdout=subprocess.PIPE).stdout)
    if not song == saved_song:
        saved_song = song
        update_change()


    sleep(update_time) # Just under a second for time bar accuracy