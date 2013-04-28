xterm -e "echo AUGERSPEED; rostopic echo -c auger_speed" &
xterm -e "echo CMD_VEL; rostopic echo -c cmd_vel" &
xterm -e "echo DOOR; rostopic echo -c door_pos "&
xterm -e "echo BUCKET; rostopic echo -c dump_pos" &
xterm -e "echo SUSPENSION; rostopic echo -c susp_pos" &

