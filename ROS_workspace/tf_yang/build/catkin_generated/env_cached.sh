#!/usr/bin/env sh
# generated from catkin/cmake/templates/env.sh.in

if [ $# -eq 0 ] ; then
  /bin/echo "Entering environment at '/home/voidknight/fuerte_workspace/sandbox/robot_setup_tf/build/catkin_generated', type 'exit' to leave"
  . "/home/voidknight/fuerte_workspace/sandbox/robot_setup_tf/build/catkin_generated/setup_cached.sh"
  "$SHELL" -i
  /bin/echo "Exiting environment at '/home/voidknight/fuerte_workspace/sandbox/robot_setup_tf/build/catkin_generated'"
else
  . "/home/voidknight/fuerte_workspace/sandbox/robot_setup_tf/build/catkin_generated/setup_cached.sh"
  exec "$@"
fi
