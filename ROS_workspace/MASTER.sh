#xterm -e rosrun command command_node.py &
xterm -e rosrun corner_detector occupancyGrid_parserv4.4.py &
#xterm -e rosrun map_builder map_builder.py &
roslaunch MASTER.launch