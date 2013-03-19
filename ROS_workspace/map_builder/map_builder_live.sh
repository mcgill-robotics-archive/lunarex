#!/bin/bash

#RUN AS SUDO!

echo "setting Lidar port permissions.."
chmod a+rw /dev/ttyACM0

echo "Starting roscore"
xterm -e roscore

echo "Setting hokuyo_node port"
rosparam set hokuyo_node/port /dev/ttyACM0 

echo "Launching all the ROS stuff.. hokuyo_node, hector_mapping, kinect_srv & map_builder"
roslaunch map_builder_live.launch

echo "Starting rviz"
xterm -e rosrun rviz rviz -d $(find hector_slam_launch)/rviz_cfg/mapping_demo.vcg"

