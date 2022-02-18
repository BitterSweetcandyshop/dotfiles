# BitterSweet's Dotfiles
Transparent, Dynamic (Music), Interactive Startup


## What is it?
- Cover_fancy script makes it to change the wallpaper to the current playing song and album art.
> dont't worry I dim it so it's not obnoxious!

- The Startup sequence is a little arcade-like animation that requires you to hit media_play_pause button

- Transparency all over, I suggest also installing Glassit-VSC for VSC.

Also the progress par is pacman for ncmpcpp

## Dependencies
> If you know what you're doing you know you don't actually need all of these.
- mpd
- mpc
- eww
- dunst
- tint2conf (working with eww atm for taskbars)
- rofi
- glasscord
- powercord
- picom
- greenclip
- candy-icons
- alacritty
- ranger
- hi-res music library of album art as /cover.jpg

### Music Library
Okay so I tried making it as friendly as possible, it uses streamrip's defaults and runs on mpc, just download large album art in the same directory for each audio file. Look in `bin/cover_fancy.py` and correct if needed.

## Note
> Yes, I used axarva's dotfiles to learn, I learn by modding best, the dotfiles I have is very different.

### Folder Names
You should know what you're doing before trying to use these, if not just dm BitterSweet#1337 or hop on my sever (in bio)

### Drag and Drop
My dotfiles are not drag and drop, most of the config is fine. below is a list of files that likely (or do) need minor modifications.
- xmonad/xmonad.hs
- bin/startup.py
- bin/cover_fancy