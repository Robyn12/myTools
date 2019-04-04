#!/bin/bash
clear
while [ 1 ]
do
  nmcli device wifi rescan
  sleep 2
  nmcli -f IN-USE,SSID,BSSID,CHAN,BARS,SECURITY dev wifi &
  TASK_PID=$!
  sleep 15
  kill $TASK_PID
  clear
done
