#!/bin/bash

#RUN AS SUDO!

echo "setting Lidar port permissions.."
chmod a+rw /dev/ttyACM0

echo "Starting roscore"
xterm -e roscore

echo "Setting hokuyo_node port"
rosparam set hokuyo_node/port /dev/ttyACM0 



