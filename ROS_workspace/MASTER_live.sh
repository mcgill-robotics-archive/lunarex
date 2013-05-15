killall roscore

echo "Starting roscore"
xterm -e roscore &

sleep 5

echo "setting Lidar port permissions.."
sudo chmod a+rw /dev/ttyACM1

echo "Setting hokuyo_node port"
rosparam set hokuyo_node/port /dev/ttyACM1 

echo "Running hokuyo_node"
xterm -e rosrun hokuyo_node hokuyo_node & 

sleep 3

echo "starting hector & move base in launch file"
xterm -e roslaunch MASTER_live.launch &

sleep 1

rosrun command command_node.py &

#must be the same as in command node! ROTATION_TIME_SECS
sleep 30

xterm -e rosrun corner_detector occupancyGrid_parserv4.7.py 