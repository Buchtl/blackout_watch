#!/bin/bash
while :
do
	#echo "Press [CTRL+C] to stop.."
	echo "watch_loop started"
  date +"%Y%m%d%H%M" >> /home/$USER/ping.txt
	sleep 60
done