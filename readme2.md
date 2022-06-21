# Hey
So you're here for a more indepth thing? There's not a lot more, but enjoy I suppose :3.

## Contact
> Sorted for best to worst

- Discord:      BitterSweet#1337
- Reddit:       BitterSweetcandyshop
- Telegram:     BitterSweetcandyshop
- Matrix:       bittersweetcandyshop
- Revolt:       BitterSweetcandyshop
- Divolt:       BitterSweet

## Music
#### Why is it all music based?
> Idk I like music spam and hoarding.
#### Why so many players?
> I use all of them equally, I mainly use qobuz/tidal for download due to it supporting higher-quality downloads then spotify's 320mp3

### Audio Source control
> This is the reason everything relies on the .scripts folder, I update source.txt with the current player I want to focus on and then use `playerctl -p $(cat ~/.scripts/music/source.txt)` or `python ~/.scripts/music/playerctl_out.py arg1 arg2`
>
> The arrows on polybar, modm+AudioNext/Prev, eww audio_source, `~/.scripts/music/music_source.py <next/back>`
#### playerctl_out
> so I don't have to type mpris: or xesm: or the source, this makes getting the artUrl easier due to how many music players I use in special cases when just `playerctl` isn'tthe best option (like in art_updater.py).
>
> - usage: `playerctl_out.py metadata artUrl` will return the artUrl from any instance
>
> if you use `title` it will return a trimmed title that I use for eww, but may have applications else where
> yes I plan on making eww use zscroll eventualy

### art_updater and lrcdl.py
> a while loop I run in the background that checks for updates in the current song, if there is a song change, it'll fetch the new cover art. This is done with playerctl_out. If there isn't a change it passes `continue` to help save on cpu/ram.
>
> art_updater will also run an api call to your lyrcsapi vercel app to fetch the current lyrics and format it to a usable .lrc file (saved in ~/.lyrics) which is then read by conky every .2 seconds to porvide lyrics, this suprisingly uses less cpu then most processes. I do have detection to not re-download lyrics over and over.  **MAKE A ~/.lyrics FOLDER**
> this somehow is not as cpu intensive as you would think due to sleep calls and avoiding redundancies.

### The Eww Vizualizers
> Sorry to inform you, it's just glava made to look like an eww widget. The configs are glava/eww_left and glava/ eww_right
>
> In .scripts/misc/center.sh and close.sh I do pkill glava each time since glava will just spawn more processes instead of overriding the old oness.
>
> There is also a delay after pkill in center.sh, why? no idea. If you can explain this to me, that would be great.
### Juuzou Mohawk Vizualizer
> Toggle in .xmonad/xmonad.hs
>
> I found out that the "circle" mod is just an arc that stretches almost 360%, I did some divison on the arc length and messed with the circle config to get the position right. Honestly, I only use it for demos honestly, it eats too much cpu/ram when I'm on discord or working on tidal-hifi css.

### Bottom left graph Vizualizer
> Toggle in .xmonad/xmonad.hs
>
> Like the juuzou visualizer, glava is known for eating some cpu so if you're on a laptop or something with limited cpu you now know.

## Tidal-Hifi and DiscordCanary (electron)
> Glasscord is an electron tool that allows electron processes to have a transparent window. Also comes with a css injector. **THIS ABSOULTELY FUCKS APP PREFORMANCE AND CPU** 
>
>I only really have it on for showcasing; disable in ~/.config/glasscord json iirc.

### Kernel-Mod on Tidal WIP
>Kernel mod is an electron modifer that allows for plugins and the sort to be applied, I have hopes of injecting a download button, song.link button, and song importer eventually.

## Wallpaper
> It's just Juuzou (they're a guy, idk y ppl care), it's on my github I have gotten dms about this, it's literaly on the repo already, just download it.

## Catppuccin
### Ratppuccin
> Okay, I just like rats, I put one in my neofetch and the slight transparent effect, someone called it ratppuccin, I laughed, so I kept it. it's only one letter and still gives proper credit to catppuccin since they don't have any transparent schemes.

### Usage
> these are form before the did the "falvours" thing.
- catppuccin.rasi, rofi, altered to be transparnet
- catppuccin.conf, conky, altered to be transparent
- catppuccin.yml, alacritty, started my interest in catppuccin, altered to be transparent
- catppuccin.css, nothing it's horribly sorted and done... I use it in discoord

## FAQ
### What do I do after I make the vercel app?
> Navigate to the ~/.scripts/music/lrcdl.py and I have put more information there for you in comments

### Where can I get the wallpaper?
> *It's in the wallpapers folder.*

### Why isn't juuzou dynamic?
> You have to go to `.scripts/music/art_updater` and change `is_bittersweet` to `True`, Make sure though to fix `.scripts/music/dynamic_wallpaper.py`

### Why do you like rats?
> They are suprisingly rather clean animals and are smart. I happen to also like how the RAT tool works well with one of my favourite animals

### Is there backups?
> There isn't even an install script, no it does not make a backup.

### Can you make me a rice?
> To the two people who asked me this, what the fuck? You use linux, you should know how to do some of this stuff. Most of my code is shit anyhow just make it yourself damn.

## No One Asked Questions:
> You know what else is c=8? MY MOM