killall roscore
killall hector_mapping
killall python
killall xterm

xterm -e roscore &
sleep 5

xterm -e  roslaunch lunarex_stage/stageLaunchV2.launch &
sleep 2
#xterm -e  rosrun rviz rviz -d rviz_configs/hector_mapping_demo.vcg &
xterm -e  rosrun command findInitialHeading.py &
xterm -e rosrun command command_node_noNav_withBackup.py &

#wait to be backed out of corner & facing far to start hector
sleep 10
xterm -e  roslaunch lunarex_2dnav/hector_launchers/simple_hector.launch &

#wait for rotation to gather good map
sleep 50
xterm -e  rosrun corner_detector occupancyGrid_parserv4.9.py

wait
