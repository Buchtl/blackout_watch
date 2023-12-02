#!/bin/bash

python3 /home/pi/blackout_watch/startup/main.py
# Keeping service busy
cd /home/pi/blackout_watch/watcher_scripts
./blackout_watch_heartbeat.sh