killall roscore

xterm -e roscore &

sleep 3

xterm -e roslaunch MASTER.launch &

sleep 1

xterm -e rosrun command command_node.py &

sleep 12

xterm -e rosrun corner_detector occupancyGrid_parserv4.6.py &

sleep 5

xterm -e rosrun map_builder map_builder.py &
 
sleep 2

xterm -e rosrun kinect_node kinect_srv_server_prototype.py

