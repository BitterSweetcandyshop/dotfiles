# Hey
So you're here for a more indepth thing? There's not a lot more, but enjoy I suppose :3.

## Music
#### Why so many players?
> I use all of them equally, I mainly use tidal for download due to it supportign higher-quality downloads then spotify's 320mp3

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

### art_updater
> a while loop I run in the background that checks for updates in tthe current song, if there is a song change, it'll fetch the new cover art. This is done with playerctl_out. If there isn't a change it passes `continue` to help save on cpu/ram.
### The Eww Vizualizers
> Sorry to inform you, it's just glava made to look like an eww widget. The configs are glava/eww_left and glava/ eww_right
>
> In .scripts/misc/center.sh and close.sh I do pkill glava each time since glava will just spawn more processes instead of overriding the old oness.
>
> There is also a delay after pkill in center.sh, why? no idea. If you can explain this to me, that would be great.
### Juuzou Mohawk Vizualizer
> I found out that the "circle" mod is just an arc that stretches almost 360%, I did some divison on the arc length and messed with the circle config to get the position right. Honestly, I only use it for demos honestly, it eats too much cpu/ram when I'm on discord or working on tidal-hifi css.

## Tidal-Hifi and DiscordCanary (electron)
> Glasscord is an electron tool that allows electron processes to have a transparent window. Also comes with a css injector
### Kernel-Mod on Tidal WIP
Kernel mod is an electron modifer that allows for plugins and the sort to be applied, I have hopes of injecting a download button, song.link button, and song importer eventually.

## Wallpaper
It's just Juuzou (they're a guy, idk y ppl care), it's on my github I have gotten dms about this, it's literaly on the repo already, just download it.

## Catppuccin
### Ratppuccin
Okay, I just like rats, I put one in my neofetch and the slight transparent effect, someone called it ratppuccin, I laughed, so I kept it. it's only one letter and still gives proper credit to catppuccin since they don't have any transparent schemes.
### Usage
> these are form before the did the "falvours" thing.
- catppuccin.rasi, rofi, altered to be transparnet
- catppuccin.conf, conky, altered to be transparent
- catppuccin.yml, alacritty, started my interest in catppuccin, altered to be transparent
- catppuccin.css, nothing it's horribly sorted and done... I use it in discoord