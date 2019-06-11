default: install-yay install-packages link-config enable-services

install-yay:
  sudo pacman -Sy git
  git clone https://aur.archlinux.org/yay.git
  cd yay
  makepkg -si
  cd ..
  rm -rf yay

install-packages:
  yay -S `cat packages.txt`

link-config:
  stow --restow .

enable-services:
	for service in 'mpd.service' 'checkmail.timer' 'syncthing.service' 'automount.service' 'inkscapefigures.service' 'inkscapewatch.service'; do
	    for action in "enable" "start"; do
	        systemctl --user $action $service
	    done
	done
