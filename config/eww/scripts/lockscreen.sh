#!/bin/bash
mpc pause &
playerctl pause &
amixer set Master mute &
betterlockscreen -l &
