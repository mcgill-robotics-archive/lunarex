Yang making a change.

Lidar Data is obtained using "rostopic /scan"

ROS needs to be installed with proper drivers for Hokuyo URG-30LX (hokuyo_node)

Representation of data obtained:

# Single scan from a planar laser range-finder

Header header
# stamp: The acquisition time of the first ray in the scan.
# frame_id: The laser is assumed to spin around the positive Z axis
# (counterclockwise, if Z is up) with the zero angle forward along the x axis

float32 angle_min # start angle of the scan [rad]
float32 angle_max # end angle of the scan [rad]
float32 angle_increment # angular distance between measurements [rad]

float32 time_increment # time between measurements [seconds] - if your scanner
# is moving, this will be used in interpolating position of 3d points
float32 scan_time # time between scans [seconds]

float32 range_min # minimum range value [m]
float32 range_max # maximum range value [m]

float32[] ranges # range data [m] (Note: values < range_min or > range_max should be discarded)
float32[] intensities # intensity data [device-specific units]. If your
# device does not provide intensities, please leave the array empty.


Terminal commands to use Lidar:

#dependencies and driver
rosdep install hokuyo_node rviz
rosmake hokuyo_node rviz

# Hokuyo permissions check
ls -l /dev/ttyACM0

# Set lidar to read//write
sudo chmod a+rw /dev/ttyACM0	

# Start roscore in new terminal
roscore

# Enable calibration
rosparam set hokuyo_node/calibrate_time true

# Disable calibration
rosparam set hokuyo_node/calibrate_time false

# Assign the hokuyo	rostopic echo	print messages to screen
	rostopic find	find topics by type
	rostopic hz	display publishing rate of topic    
	rostopic info	print information about active topic
	rostopic list	list active topics
	rostopic pub	publish data to topic
	rostopic type	print topic type

Type rostopic <command> -h for more detailed usage, e.g. 'rostopic echo -h'
_node lidar hardware
rosparam set hokuyo_node/port /dev/ttyACM0 

# Connect to lidar in new terminal
rosrun hokuyo_node hokuyo_node

# View data in rviz
rosrun rviz rviz -d `rospack find hokuyo_node`/hokuyo_test.vcg

# display Raw data from Lidar
rostopic echo /scan

# Special flags for rostopic
# -p : friendly data mode

To output friendly data to command line
rostopic echo -p /scan

-----------------------------
Ernest's additional notes:

run this to dl hokuyo_node
sudo apt-get install ros-fuerte-laser-drivers

$ rospack find [package_name]
$ rosstack find [stack_name]

Important - Environment setup

echo "source /opt/ros/fuerte/setup.bash" >> ~/.bashrc
. ~/.bashrc

OR

source /opt/ros/fuerte/setup.bash


------------------
Live stream readme

Term 1
Run roscore

Term 2
give yourself permission on the port: 
sudo chmod a+rw /dev/ttyACM0

start stream
rosrun hokuyo_node hokuyo_node

Term 3
Echo the stream & pipe it to the liveProcessor:
rostopic echo -p /scan | ./liveProcessor.py

Note: in this case liveProcessor.py was made executable by writing this at the top of the file
#!/usr/bin/env python
and running this
chmod +x liveProcessor.py




