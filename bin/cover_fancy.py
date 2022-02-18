#!/usr/bin/env python3.10
while True: 
    from PIL import Image, ImageFont, ImageDraw, ImageFilter, ImageEnhance
    import subprocess
    import shutil
    import time

    # Get the path from music database and copy it to eww images folder
    cover_path = subprocess.run(['mpc', 'current', '-f', "%file%"], stdout=subprocess.PIPE)
    cover_path = "/home/bittersweet/Music/" + "/".join(str(cover_path.stdout)[2:-3].split("/")[:-1]) + "/cover.jpg"
    try:
        shutil.copy(cover_path, "/home/bittersweet/.config/eww/images/cover.jpg")
    except:
        shutil.copy("/home/bittersweet/.config/eww/images/image.jpg", "/home/bittersweet/.config/eww/images/cover.jpg")

    # Get the cover ready
    cover = Image.open("/home/bittersweet/.config/eww/images/cover.jpg")
    darkener = ImageEnhance.Brightness(cover)
    cover = darkener.enhance(0.5)
    cover = cover.filter(ImageFilter.GaussianBlur(30))
    cover = cover.resize((3840, 2160))
    cover_editable = ImageDraw.Draw(cover)

    # Get the Song Name and Font
    song_name = subprocess.run(['mpc', 'current'], stdout=subprocess.PIPE)
    try: 
        artist_name, song_name = str(song_name.stdout)[2:-3].split(" - ")
    except:
        artist_name, song_name = "Nothing Playing", ""
    title_font = ImageFont.truetype("/home/bittersweet/.fonts/PressStart2P-Regular.ttf", 60)

    # Modify the cover
    cover_mini = Image.open("/home/bittersweet/.config/eww/images/cover.jpg")
    cover_mini.thumbnail((350, 350))

    cover_editable.text((1800,850), song_name.replace("(Explicit)", ""), (237, 230, 211), font=title_font)
    cover_editable.text((1800,920), artist_name, (237, 230, 211), font=title_font)
    cover.paste(cover_mini, (1400, 850))
    cover.save("/home/bittersweet/.config/eww/images/cover_fancy.jpg")

    subprocess.run(['feh', '--bg-scale', '/home/bittersweet/.config/eww/images/cover_fancy.jpg'])

    time.sleep(1)