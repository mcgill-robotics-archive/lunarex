if [ $# -ne 2 ]
    then
        echo "Need 2 args"
        exit 1
fi

killall roscore
killall hokuyo_node
killall python

echo "Starting roscore"
xterm -e roscore &

sleep 5

echo "setting Lidar port permissions.."
sudo chmod a+rw /dev/ttyACM$1

echo "Setting hokuyo_node port"
rosparam set hokuyo_node/port /dev/ttyACM$1 

echo "set use_rep_117 to get rid of annoying warning"
rosparam set use_rep_117 true 

echo "Running hokuyo_node"
xterm -e rosrun hokuyo_node hokuyo_node & 

echo "***Starting rosserial and binding to /dev/ttyACM(PORT)"
xterm -e rosrun rosserial_python serial_node.py /dev/ttyACM$2 &

echo "setting sim time to FALSE"
rosparam set use_sim_time false

echo "starting hector"
#xterm -e roslaunch lunarex_2dnav/hector_launchers/hector_mapping_live_noNav.launch &
xterm -e roslaunch lunarex_2dnav/hector_launchers/simple_hector.launch &

sleep 2

echo "Starting command node"
xterm -e rosrun command command_node_noNav.py &

#echo "Starting move_base"
#xterm -e roslaunch lunarex_2dnav/move_base.launch &

#echo "recording ros bag"
#xterm -e rosbag record corners tf &

#must be the same as in command node! ROTATION_TIME_SECS
sleep 60

xterm -e rosrun corner_detector occupancyGrid_parserv4.7.py &

#rosrun rviz rviz -d lunarex_2dnav/costmaps.vcg
