#killall roscore

#xterm -e roscore &

xterm -e roslaunch MASTER_stage.launch &

sleep 1

rosrun command command_node.py &

#must be the same as in command node! ROTATION_TIME_SECS
sleep 30

xterm -e rosrun corner_detector occupancyGrid_parserv4.7.py 
#xterm -e rosrun map_builder map_builder.py &
