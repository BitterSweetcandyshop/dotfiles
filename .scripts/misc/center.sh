#!/bin/bash
pkill glava &
exec ~/bin/eww open-many blur_full header audio_source home_dir vpn-icon profile incognito-icon power_full reboot_full lock_full suspend_full logout_full player_side screenshot ncmpcpp &
sleep 1
glava -e eww_right.glsl -m bars &
glava -e eww_left.glsl -m bars &
