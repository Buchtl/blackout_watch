#!/bin/bash

python3 /home/pi/blackout_watch/startup/main.py
# Keeping service busy
# shellcheck disable=SC2164
cd /home/pi/blackout_watch/watcher_scripts
./blackout_watch_heartbeat.sh