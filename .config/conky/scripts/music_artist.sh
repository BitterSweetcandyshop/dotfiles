#!/bin/bash

# Set the source audio player here.
# Players supporting the MPRIS spec are supported.
# Examples: spotify, vlc, chrome, mpv and others.
# Use `playerctld` to always detect the latest player.
# See more here: https://github.com/altdesktop/playerctl/#selecting-players-to-control
PLAYER=`cat ~/.config/polybar/scripts/source.txt`

# Format of the information displayed
# Eg. {{ artist }} - {{ album }} - {{ title }}
# See more attributes here: https://github.com/altdesktop/playerctl/#printing-properties-and-metadata
FORMAT="{{ artist }}"

PLAYERCTL_STATUS=$(playerctl status --player=$PLAYER 2>/dev/null)
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    STATUS=$PLAYERCTL_STATUS
else
    STATUS=""
fi

if [ "$1" == "--status" ]; then
    echo "$STATUS"
else
    if [ "$STATUS" = "Stopped" ]; then
        echo ""
    elif [ "$STATUS" = "Paused"  ]; then
        playerctl metadata --player=$PLAYER --format="$FORMAT"
    elif [ "$STATUS" = "No player is running"  ]; then
        echo ""
    else
        playerctl metadata --player=$PLAYER --format="$FORMAT"
    fi
fi

