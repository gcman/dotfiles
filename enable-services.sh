#!/bin/sh
unset services
declare -a services=( 'mpd.service' 'checkmail.timer' 'syncthing.service' 'automount.service' 'inkscapefigures.service' 'inkscapewatch.service' )
for service in $services; do
    for action in "enable" "start"; do
        systemctl --user $action $service
    done
done
