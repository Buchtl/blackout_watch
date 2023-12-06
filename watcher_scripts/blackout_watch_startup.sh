#!/bin/bash

# Some delay because Pi needs to sync his clock
OUTPUT="/home/pi/systime.txt"
echo "before sleep" >> $OUTPUT
date >> $OUTPUT
sleep 30
echo "after sleep" >> $OUTPUT
date >> $OUTPUT

cd /home/pi/blackout_watch/startup/ || exit
python3 main.py
# Keeping service busy
# shellcheck disable=SC2164
cd ../watcher_scripts
./blackout_watch_heartbeat.sh