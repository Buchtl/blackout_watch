#!/bin/bash
while :
do
	#echo "Press [CTRL+C] to stop.."
	echo "watch_loop started"
  date +"%Y%m%d%H%M" >> /home/$USER/heartbeat.txt
	sleep 60
done