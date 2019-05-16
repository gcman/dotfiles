default: install-yay install-packages link-config enable-services

install-yay:
  ./install-yay.sh

install-packages:
  yay -S `cat packages.txt`

link-config:
  stow --restow .

enable-services:
	systemctl --user enable mpd.service
	systemctl --user start mpd.service
  systemctl --user enable checkmail.timer
  systemctl --user start checkmail.timer
	systemctl --user enable syncthing.service
  systemctl --user start syncthing.service
