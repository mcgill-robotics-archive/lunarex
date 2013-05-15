killall roscore

echo "Starting roscore"
xterm -e roscore &

sleep 5

echo "setting Lidar port permissions.."
sudo chmod a+rw /dev/ttyACM0

echo "Setting hokuyo_node port"
rosparam set hokuyo_node/port /dev/ttyACM0 

echo "set use_rep_117 to get rid of annoying warning"
rosparam set use_rep_117 true 

echo "Running hokuyo_node"
xterm -e rosrun hokuyo_node hokuyo_node & 

sleep 3

echo "setting sim time to FALSE"
rosparam set use_sim_time false

echo "starting hector"
#xterm -e roslaunch lunarex_2dnav/hector_launchers/hector_mapping.launch &
roslaunch lunarex_2dnav/hector_launchers/hector_mapping_live.launch
#xterm -e roslaunch lunarex_2dnav/hector_launchers/simple_hector.launch &


#echo "Starting move_base"
#xterm -e roslaunch lunarex_2dnav/move_base.launch &

#sleep 1

#echo "Starting command node"
#xterm -e rosrun command command_node.py &

#must be the same as in command node! ROTATION_TIME_SECS
#sleep 30

#xterm -e rosrun corner_detector occupancyGrid_parserv4.7.py 