#!/bin/bash

echo "***Kill roscore if already running"
killall roscore

echo "***Starting roscore"
xterm -e roscore &

echo "***Sleep while roscore starts"
sleep 5

echo "***Starting rosserial and binding to /dev/ttyACM1"
xterm -e rosrun rosserial_python serial_node.py /dev/ttyACM0 &

echo "***Publish arduino feedback"
xterm -e rostopic echo /arduino_feeback &
