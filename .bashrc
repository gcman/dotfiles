# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

if [ -d ~/bin ]; then
    PATH=$PATH:~/bin
fi

if [ -d ~/.local/bin ]; then
    PATH=$PATH:~/.local/bin
fi

HISTSIZE=-1
HISTFILESIZE=-1

export ALTERNATE_EDITOR=""
export EDITOR="emacsclient -n -a emacs"         # $EDITOR opens in terminal
export VISUAL="emacsclient -n -a emacs"         # $VISUAL opens in GUI mode

export MPD_HOST="localhost"
export MPD_PORT="6601"
