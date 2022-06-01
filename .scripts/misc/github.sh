#!/bin/bash
# Yes, I use this to update my dotfiles instead of sym links, cope

cp -r ~/.config/conky ~/Documents/development/dotfiles/.config/
echo Conky
cp -r ~/.config/dunst ~/Documents/development/dotfiles/.config/
echo Dunst
cp -r ~/.config/eww ~/Documents/development/dotfiles/.config/
echo Eww
cp -r ~/.config/polybar ~/Documents/development/dotfiles/.config/
echo Polybar
cp -r ~/.config/neofetch ~/Documents/development/dotfiles/.config/
echo Neofetch
cp -r ~/.config/rofi ~/Documents/development/dotfiles/.config/
echo Rofi
cp -r ~/.config/cava ~/Documents/development/dotfiles/.config/
echo Cava
cp -r ~/.config/conky ~/Documents/development/dotfiles/.config/
echo Conky
cp -r ~/.config/mpDris2 ~/Documents/development/dotfiles/.config/
echo mpDris2
cp -r ~/.config/jgmenu ~/Documents/development/dotfiles/.config/
echo Jgmenu

cp -r ~/.config/gtk-2.0 ~/Documents/development/dotfiles/.config/
cp -r ~/.config/gtk-3.0 ~/Documents/development/dotfiles/.config/
echo GTK

cp ~/.config/alacritty.yml ~/Documents/development/dotfiles/.config/alacritty.yml
echo Alacritty
cp ~/.config/betterlockscreenrc ~/Documents/development/dotfiles/.config/betterlockscreenrc
echo BetterLock
cp ~/.config/picom.conf ~/Documents/development/dotfiles/.config/picom.conf
echo Picom

cp ~/.config/powercord/src/Powercord/themes/Bloop/bloop-config.css ~/Documents/development/dotfiles/.config/powercord/src/Powercord/themes/Bloop/bloop-config.css
cp ~/.config/powercord/src/Powercord/themes/Bloop/powercord_manifest.json ~/Documents/development/dotfiles/.config/powercord/src/Powercord/themes/Bloop/powercord_manifest.json
cp ~/.config/powercord/src/Powercord/themes/Bloop/splash.css ~/Documents/development/dotfiles/.config/powercord/src/Powercord/themes/Bloop/splash.css
echo Powercord

cp -r ~/.scripts ~/Documents/development/dotfiles/
echo Scripts

cp ~/.xmonad/xmonad.hs ~/Documents/development/dotfiles/.xmonad/xmonad.hs
echo XMonad

cp -r ~/.config/glava/circle/ ~/Documents/development/dotfiles/.config/glava
cp ~/.config/glava/circle.glsl ~/Documents/development/dotfiles/.config/glava/circle.glsl
cp ~/.config/glava/eww_left.glsl ~/Documents/development/dotfiles/.config/glava/eww_left.glsl
cp ~/.config/glava/eww_right.glsl ~/Documents/development/dotfiles/.config/glava/eww_right.glsl
cp -r ~/.config/glava/rc.glsl ~/Documents/development/dotfiles/.config/glava/rc.glsl
echo Glava

cp ~/bin/inhibit_activate ~/Documents/development/dotfiles/bin/
cp ~/bin/inhibit_deactivate ~/Documents/development/dotfiles/bin/
cp ~/bin/launcher.sh ~/Documents/development/dotfiles/bin/
cp ~/bin/lock.sh ~/Documents/development/dotfiles/bin/
cp ~/bin/Low-battery-sound.flac ~/Documents/development/dotfiles/bin/
cp ~/bin/music_updater.py ~/Documents/development/dotfiles/bin/
cp ~/bin/notieye ~/Documents/development/dotfiles/bin/
cp ~/bin/notipose ~/Documents/development/dotfiles/bin/
cp ~/bin/powermenu.sh ~/Documents/development/dotfiles/bin/
cp ~/bin/spotifystatus ~/Documents/development/dotfiles/bin/
echo Bin
