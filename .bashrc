#
# ~/.bashrc
#
export PATH="$PATH:$HOME/bin"

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

cat ~/.config/neofetch/text_art.txt | tail -n12

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '
#PS1="$(neofetch --stdout)"
PS2='$$ '

# Created by `pipx` on 2022-01-06 22:29:43
export PATH="$PATH:/home/bittersweet/.local/bin"
export PATH=$PATH:/home/bittersweet/.spicetify
