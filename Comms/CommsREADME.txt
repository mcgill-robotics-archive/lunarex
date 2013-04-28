On the server side, simply run "rosrun lx_server ros_server.py" (after running "roscore" of course)

2. On the client side, run GUIMain.java and:

    a) Click "SPACE" to connect to the server (Right now the ip address it connects to is the ip address of the netbook. If the ip address of the server changes, simply change the "ipAdressString" variable at line 11 in GUIMain.java)

    b) To change the linear velocity, keep "Q" pressed, and use "UP" and "DOWN" to change

    c) To change the angular velocity, keep "W" pressed, and use "LEFT" and "RIGHT" to change

    ** By keep both "Q" and "W" pressed, you can change both the linear and angular velocity; but in this way (only) "RIGHT" key does not work and I don't know why... so for now I suggest changing linear and angular velocities separately... **

    ** For data sent to /cmd_vel, the linear velocity ranges from -2.56 to 2.54 (m/s I guess?)  and the angular velocity range from -2.56 to 2.54 rad/s. So the robot should not be moving fast right now and the change of velocities should be smooth enough. **

    d) By Pressing "S", you can stop the robot right away.

3. To play with the simulation robot in stage, keep the client and server running, and then simply go to ROS_workspace/lunarex_stage and run "roslaunch stageLaunchV2.launch"

----IMPORT CLIENT INTO ECLIPSE----------

in git repo, go to comms / client

start eclipse with a different workspace from comms/client (any other path should work)

file > import > existing projects into workspace > select root directory:
enter comms/client path

if there are JRE issues:
go to Project > properties > java build path >
remove anything with errors
click add library > JRE system librar

//FOR ERNEST LAPTOP
click search, select /usr/lib/jvm/
add the jre that was found. It is 1.7


AFTER PULL FROM GIT

1) Right click Client project > Properties > Java Build path
2) Libraries tab: delete the one with the error
add the right one from test project (jinput.jar_
3) Project: -delete the one w/error
- add test project
