#!/bin/bash
sudo cp *.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable blackout_watch_hearbeat.service
sudo systemctl enable blackout_watch_server.service
sudo systemctl start blackout_watch_hearbeat.service
sudo systemctl start blackout_watch_server.service