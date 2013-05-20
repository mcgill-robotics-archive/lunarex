xterm -e roscore &
sleep 5
xterm -e roslaunch lunarex_stage/stageLaunchV2.launch &
xterm -e roslaunch lunarex_2dnav/hector_launchers/simple_hector.launch &
xterm -e rosrun rviz rviz -d ../rviz_configs/hector_mapping_demo.vcg &
sleep 5
xterm -e rostopic pub -r 10 /cmd_vel geometry_msgs/Twist  '{linear:  {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0,y: 0.0,z: -0.15}}' &
# sleep 20
# xterm -e rosrun corner_detector occupancyGrid_parserv4.9.py &
