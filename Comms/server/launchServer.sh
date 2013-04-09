#!/bin/bash

echo "starting roscore"
xterm -e roscore &

echo "wait for roscore to be ready.."
sleep 5

rosrun lx_server ros_server.py
