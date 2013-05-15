#killall roscore

#xterm -e roscore &

xterm -e roslaunch MASTER.launch &

sleep 1

rosrun command command_node.py &

sleep 10

xterm -e rosrun corner_detector occupancyGrid_parserv4.6.py 
#xterm -e rosrun map_builder map_builder.py &

