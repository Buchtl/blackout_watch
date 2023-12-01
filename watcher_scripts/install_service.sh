#!/bin/bash
sudo blackout_watch.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable blackout_watch.service