# ~/.bashrc
#

alias ls='ls --color=auto'

if [ -d ~/.local/bin ]; then
    PATH=$PATH:~/.local/bin
fi

if [ -d ~/bin ]; then
    PATH=$PATH:~/bin
fi

export HISTSIZE=-1
export HISTFILESIZE=-1

export DRIVE_LOC="501b6655-ac04-4e1e-b921-67e8947b2d84"

export ALTERNATE_EDITOR=""
export EDITOR="emacsclient -c -a emacs"         # $EDITOR opens in terminal
export VISUAL="emacsclient -c -a emacs"         # $VISUAL opens in GUI mode

export MPD_HOST="localhost"
export MPD_PORT="6601"
