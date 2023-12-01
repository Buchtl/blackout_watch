#!/bin/bash
sudo cp blackout_watch.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable blackout_watch.service
sudo systemctl start blackout_watch.service