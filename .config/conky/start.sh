#!/bin/bash
# db_sizes in the conks folder requires editing

pkill conky
conky -c ~/.config/conky/conks/music.conf &
#conky -c ~/.config/conky/conks/cover.conf &
#conky -c ~/.config/conky/conks/torrentfreak.conf &
conky -c ~/.config/conky/conks/catppuccin.conf &
conky -c ~/.config/conky/conks/ret.conf &