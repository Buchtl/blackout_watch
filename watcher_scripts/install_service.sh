#!/bin/bash
sudo cp *.service /etc/systemd/system/
sudo systemctl daemon-reload
# Enable services
sudo systemctl enable blackout_watch_startup.service
sudo systemctl enable blackout_watch_server.service
#sudo systemctl enable blackout_watch_heartbeat.service
# Start services
sudo systemctl start blackout_watch_startup.service
sudo systemctl start blackout_watch_server.service
#sudo systemctl start blackout_watch_heartbeat.service