#!/bin/bash

#FIRST AND ONLY ARGUMENT IS THE ACM port number

if [ $# -eq 0 ]
    then
        echo "No arguments provided"
        exit 1
fi

echo "***Kill roscore if already running"
killall roscore

echo "***Kill python if already running"
killall python

echo "***Killing avr_dude***"
killall avr_dude

echo "***Starting roscore"
xterm -e roscore &

echo "***Sleep while roscore starts"
sleep 5

echo "***Starting rosserial and binding to /dev/ttyACM(PORT)"
xterm -e "rosrun rosserial_python serial_node.py /dev/ttyACM$1 & read -sn 1 -p "i"" &

sleep 2

echo "***Starting the server***"
xterm -e "rosrun lx_server ros_server_slower.py & read -sn 1 -p "i"" &


sleep 2

echo "***Publish server topics" 
xterm -e sh /home/lunarex/McGill_LunarEx_2013/ROS_workspace/lx_server/scripts/showServerPubs.sh &

sleep 2

echo "***Done" &

read -sn 1 -p "ctrl c to kill errtang"

#ampersand added so that we can kill everything in one ctrl+C
