#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /
cd /home/pi/Rover_Code #where the script is
sudo python Main.py #a commnad to run the script
cd /