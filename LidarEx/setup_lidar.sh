# Set lidar to read//write
echo "Setting read/write permissions to Hokuyo URG-30LX LiDAR \n"
sudo chmod a+rw /dev/ttyACM0	
echo "Permissions granted. \n"

# Start roscore in new terminal
echo "Initializing ROScore... \n"
#gnome-terminal -e roscore
echo "ROScore enabled. \n"

# Enable calibration
echo "Pointing hokuyo_node to correct LiDAR port... \n"
rosparam set hokuyo_node/calibrate_time true
rosparam set hokuyo_node/port /dev/ttyACM0 

# Connect to lidar in new terminal
echo "Run the hokuyo_node. \n"
eterm -e rosrun hokuyo_node hokuyo_node

echo "LiDAR ready. \n"
