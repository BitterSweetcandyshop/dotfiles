#!/bin/bash

# The name of polybar bar which houses the main spotify module and the control modules.
PARENT_BAR="middle"
PARENT_BAR_PID=$(pgrep -a "polybar" | grep "$PARENT_BAR" | cut -d" " -f1)

PLAYER=`cat ~/.scripts/music/source.txt`

PLAYERCTL_STATUS=$(playerctl --player=$PLAYER status 2>/dev/null)
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    STATUS=$PLAYERCTL_STATUS
else
    STATUS="No player is running"
fi

if [ "$1" == "--status" ]; then
    echo "$STATUS"
else
    if [ "$STATUS" = "Stopped" ]; then
        echo ""
    elif [ "$STATUS" = "Paused"  ]; then
        echo ""
    elif [ "$STATUS" = "No player is running"  ]; then
        echo "$STATUS"
    else
        echo ""
    fi
fi

