#!/bin/bash
mpc pause &
eww close-all
playerctl -a pause &
amixer set Master mute &
betterlockscreen -l &
