#!/bin/bash

#LUNABOTICS PRESENTATION DEMO

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

sleep 5

echo "***Starting STAGE"
xterm -e roslaunch lunarex_stage/stageLaunchV2.launch &

echo "***Starting rosserial and binding to /dev/ttyACM(PORT)"
xterm -e "rosrun rosserial_python serial_node.py /dev/ttyACM$1 & read -sn 1 -p "i"" &

echo "***Starting hector mapping"
xterm -e roslaunch lunarex_2dnav/hector_launchers/simple_hector.launch &

echo "***Starting RVIZ"
xterm -e rosrun rviz rviz -d rviz_configs/hector_mapping_demo.vcg &

echo "***Starting the command node"
rosrun command command_node_noNav.py &

sleep 50

echo "***starting corner detecotr"
xterm -e  rosrun corner_detector occupancyGrid_parserv4.9.py &
wait
