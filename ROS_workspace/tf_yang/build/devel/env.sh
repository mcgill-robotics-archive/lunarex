#!/usr/bin/env sh
# generated from catkin/cmake/templates/env.sh.in

if [ $# -eq 0 ] ; then
  /bin/echo "Entering environment at '/home/voidknight/fuerte_workspace/sandbox/robot_setup_tf/build/devel', type 'exit' to leave"
  . "/home/voidknight/fuerte_workspace/sandbox/robot_setup_tf/build/devel/setup.sh"
  "$SHELL" -i
  /bin/echo "Exiting environment at '/home/voidknight/fuerte_workspace/sandbox/robot_setup_tf/build/devel'"
else
  . "/home/voidknight/fuerte_workspace/sandbox/robot_setup_tf/build/devel/setup.sh"
  exec "$@"
fi
