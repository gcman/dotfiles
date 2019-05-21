#!/bin/sh

userresources=$HOME/.Xresources
usermodmap=$HOME/.Xmodmap

if [ -f "$userresources" ]; then

    xrdb -merge "$userresources"

fi

if [ -f "$usermodmap" ]; then
    xmodmap "$usermodmap"
fi

export GDK_SCALE=2
export GDK_DPI_SCALE=0.5

dbus-update-activation-environment --systemd DISPLAY
eval $(/usr/bin/gnome-keyring-daemon --start --components=pkcs11,secrets,ssh)
export SSH_AUTH_SOCK

exec i3
