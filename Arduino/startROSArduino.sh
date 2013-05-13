#!/bin/bash

#FIRST AND ONLY ARGUMENT IS THE ACM port number

if [ $# -eq 0 ]
    then
        echo "No arguments provided"
        exit 1
fi

echo "***Kill roscore if already running"
killall roscore

echo "***Starting roscore"
xterm -e roscore &

echo "***Sleep while roscore starts"
sleep 5

echo "***Starting rosserial and binding to /dev/ttyACM(PORT)"
xterm -e rosrun rosserial_python serial_node.py /dev/ttyACM$1 &

echo "***Publish arduino feedback" 
#xterm -e rostopic echo /arduino_feeback &

echo "***legit. Type server when prompted"
