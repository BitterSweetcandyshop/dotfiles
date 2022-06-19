#!/bin/bash
exec ~/bin/eww close-all &
pkill glava &
sleep 2
glava -e bars_rc.glsl &
