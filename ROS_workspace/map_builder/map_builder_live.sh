#!/bin/bash

#NOTES
#Will ask for password for sudo
#Do not forget the & after an xterm command
#Relies on the followign files:
#   - ../hector_launchers/l2.launch
#   - ../rviz_configs/hector_mapping_demo.vcg
#   kinect_srv_server.py in kinect_node package
#   map_builder.py in map_builder package

echo "***Kill anything that's already running"
killall roscore
killall hokuyo_node

echo "***setting Lidar port permissions.."
sudo chmod a+rw /dev/ttyACM1

echo "***Starting roscore"
xterm -e roscore &

echo "***sleep a bit to wait for roscore"
sleep 5

echo "***Setting hokuyo_node port"
rosparam set hokuyo_node/port /dev/ttyACM1 

echo "***set rosparam to get rid of annoying warning"
rosparam set use_rep_117 true 

echo "***Running hokuyo_node"
xterm -e rosrun hokuyo_node hokuyo_node & 

sleep 3

echo "***Starting rviz"
#xterm -e rosrun rviz rviz -d ../rviz_configs/map_builder_config.vcg &
xterm -e rosrun rviz rviz -d ../rviz_configs/hector_mapping_demo.vcg &

echo "***Launching kinect and map builder"
roslaunch map_builder_live.launch
