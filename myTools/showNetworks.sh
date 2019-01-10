#!/bin/bash

while [ 1 ]
do
  nmcli dev wifi &
  TASK_PID=$!
  sleep 5
  kill $TASK_PID
  clear
done
