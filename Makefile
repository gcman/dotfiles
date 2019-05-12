default: install-yay install-packages link-config enable-services

install-yay:
  ./install-yay.sh

install-packages:
  yay -S `cat packages.txt`

link-config:
  stow --restow `ls -d */`

enable-services:
  systemctl --user enable checkmail.timer
  systemctl --user start checkmail.timer
