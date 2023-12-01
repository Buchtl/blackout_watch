#!/bin/bash
sudo systemctl stop blackout_watch_heartbeat.service
sudo systemctl stop blackout_watch_server.service
sudo rm /etc/systemd/system/blackout_watch_heartbeat.service
sudo rm /etc/systemd/system/blackout_watch_server.service
sudo systemctl daemon-reload

