#!/bin/bash
mpc pause &
playerctl -a  pause &
amixer set Master mute &
betterlockscreen -l &
