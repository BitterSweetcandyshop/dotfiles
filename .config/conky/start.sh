#!/bin/bash
# db_sizes in the conks folder requires editing

pkill conky
conky -c ~/.config/conky/conks/music.conf &
#conky -c ~/.config/conky/conks/conky_cover.conf &
#conky -c ~/.config/conky/conks/db_sizes.conf &
conky -c ~/.config/conky/conks/torrentfreak.conf &