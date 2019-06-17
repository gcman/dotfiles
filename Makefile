install-yay:
		./install-yay.sh

install-packages:
		yay -S reflector
		sudo reflector --verbose --latest 50 --sort rate --save /etc/pacman.d/mirrorlist
		yay -S - < packages.txt

link-config:
		stow --restow .

tangle:
		find . -type f -name "*.org" -exec em-tangle {} \;

enable-services:
		./enable-services.sh
		systemctl enable suspend@gautam
		systemctl enable resume@gautam
