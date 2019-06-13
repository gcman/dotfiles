#!/bin/sh
unset services
declare -a services=( 'mpd.service' 'syncthing.service' 'automount.service' 'inkscapefigures.service' 'inkscapewatch.service' 'checkmail.timer' 'syncmedia.timer' )
for service in $services; do
    for action in "enable" "start"; do
        systemctl --user $action $service
    done
done
