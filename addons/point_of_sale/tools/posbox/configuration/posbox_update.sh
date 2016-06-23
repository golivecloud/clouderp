#!/usr/bin/env bash

sudo mount -o remount,rw /
sudo git --work-tree=/home/pi/clouderp/ --git-dir=/home/pi/clouderp/.git pull
sudo mount -o remount,ro /
(sleep 5 && sudo reboot) &
