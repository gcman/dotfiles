#!/bin/sh

userresources=$HOME/.Xresources

if [ -f "$userresources" ]; then

    xrdb -merge "$userresources"

fi

dbus-update-activation-environment --systemd DISPLAY
eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
export SSH_AUTH_SOCK

exec i3
