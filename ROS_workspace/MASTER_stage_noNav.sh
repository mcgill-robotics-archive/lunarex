killall roscore
killall hector_mapping
killall python

xterm -e roscore &
sleep 5
xterm -e  roslaunch lunarex_stage/stageLaunchV2.launch &
xterm -e  roslaunch lunarex_2dnav/hector_launchers/simple_hector.launch &
xterm -e  rosrun rviz rviz -d rviz_configs/hector_mapping_demo.vcg &
xterm -e  rosrun command findInitialHeading.py &
rosrun command command_node_noNav.py &
#sleep 45
#xterm -e  rosrun corner_detector occupancyGrid_parserv4.9.py
#wait