#!/usr/bin/env bash

sudo pacman -Sy git
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..
rm -rf yay
