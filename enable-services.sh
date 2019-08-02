#!/bin/sh
unset services
declare -a services=( 'mpd' 'syncthing' 'automount' 'inkscapefigures' 'inkscapewatch' 'checkmail.timer' 'syncmedia.timer' 'bat-shutdown.timer' )
for service in $services; do
    for action in "enable" "start"; do
        systemctl --user $action $service
    done
done
