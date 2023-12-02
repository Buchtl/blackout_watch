#!/bin/bash

python3 /home/pi/blackout_watch/startup/main.py
# Keeping service busy
while :
do
	echo "startup service alive"
	sleep 60
done