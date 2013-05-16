echo "setting Lidar port permissions.."
sudo chmod a+rw /dev/ttyACM$1

echo "Setting hokuyo_node port"
rosparam set hokuyo_node/port /dev/ttyACM$1 

echo "set use_rep_117 to get rid of annoying warning"
rosparam set use_rep_117 true 

echo "Running hokuyo_node"
xterm -e rosrun hokuyo_node hokuyo_node & 