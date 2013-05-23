#!/usr/bin/env  python
import SocketServer
import sys
import serial
import json
import time
import select
from threading import Thread

#ROS settings
NODE_NAME = 'ros_lunarex_server'
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import *
from geometry_msgs.msg import *		#mainly use Twist to publish velocities

HOST=''
PORT=5902
BUFFERSIZE=4096

#Publisher
pub_vel = None
dump_LA_pub = None	# For dumping linear actuator
susp_LA_pub = None	# For suspension
door_LA_pub = None
auger_Speed_pub = None

#Subscriber variables
latestPose = Pose()
#global_x = 0.0

#Don't need these actually
COM='/dev/ttyACM0'
BAUD=115200

#Data package sent fomr this server to the client
class PosData:
    def __init__(self,x,y,theta):
        self.x=x
        self.y=y
        self.theta=theta

#Velocity message
class Velocity:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

def posCallback(data):
        latestPose = data.pose;
#        global_x = latestPose.position.x
#        print latestPose.position.x

class Handler(SocketServer.BaseRequestHandler):
    def setup(self):
        self.currentPos = PosData(latestPose.position.x,latestPose.position.y,latestPose.orientation.w)
#        print latestPose.position.x
        self.initialTime = int(time.time()*1000.0)
        self.currentTime = int(time.time()*1000.0)

        self.request.setblocking(0)

        self.datalist = []
        #self.ser=serial.Serial(COM,BAUD,timeout=1)
        self.count=0

        print str(self.request.getpeername())+" connected"

    def handle(self):
        while(True):
            self.currentPos = PosData(latestPose.position.x,latestPose.position.y,latestPose.orientation.w)
            self.currentTime = int(time.time()*1000.0)
            try:
                self.datalist = self.request.recv(6)
                #Only if data is received will publisher work
                if self.datalist[0] != "":
                    self.dump_pos = int((ord)(self.datalist[5]))
                    self.susp_pos = int((ord)(self.datalist[3]))
                    self.door_pos = int((ord)(self.datalist[0]))
                    self.auger_speed = int((ord)(self.datalist[4]))

                    #Create velocity message
                    linear_vel = (float)((ord)(self.datalist[1])) #cast bytes to float
                    angular_vel = (float)((ord)(self.datalist[2]))
                    linear_vel, angular_vel = self.processVel(linear_vel, angular_vel, self.susp_pos)	# Process the input velocity, convert byte to m/s
                    self.linearVelocity = Velocity(linear_vel, 0.0, 0.0)     #   Linear Velocity object from datalist[1]
                    self.angularVelocity = Velocity(0.0, 0.0, angular_vel)    #   Angular Velocity object from datalist[2]
                    

                    if((self.currentTime-self.initialTime) > 100):
                        if not rospy.is_shutdown():
                            try:
                                pub_vel.publish(self.linearVelocity, self.angularVelocity)  #   Send Twist message to /cmd_vel topic
                                dump_LA_pub.publish(self.dump_pos)	# Send dumping info
                                susp_LA_pub.publish(self.susp_pos)	# Send suspension info
                                door_LA_pub.publish(self.door_pos)	# Send door status
                                auger_Speed_pub.publish(self.auger_speed)	# Send auger speed
                            except rospy.ROSInterruptException:
                                print 'Error in ROS nod'
                        self.initialTime = self.currentTime
                    self.datalist = []  #   Prepare datalist for next input

                    # DO NOT DELETE! USED FOR FEEDBACK MECHANISM
                    if((self.currentTime-self.initialTime) > 500):
                        self.currentPos = PosData(latestPose.position.x,latestPose.position.y,latestPose.orientation.w)
                        dataPacket = json.dumps(vars(self.currentPos),sort_keys=True,indent=4)
                        self.request.send(dataPacket)
                        self.initialTime = self.currentTime
                        # print latestPose.position.x
                        # print global_x
                        # print latestPose.position.y
                        # print dataPacket
            except IOError:
                pass

    def processVel(self, linear_vel, angular_vel, susp_pos):
        max_speed_linear = 0.33
        max_speed_angular = 0.65
        if susp_pos > 100:   # large values correspond to mining
            max_speed_linear /=2
            max_speed_angular /=2
    	#convert back from byte to float
    	linear_vel = linear_vel - 127
    	linear_vel = linear_vel*max_speed_linear/128
    	angular_vel = angular_vel - 127
    	angular_vel = angular_vel*max_speed_angular/128

    	return linear_vel, angular_vel

    def byteToBool(self, in_byte):
    	if (int)(in_byte) == 1:
    	    return True
    	return False


    def finish(self):
        self.request.close()

class Server(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True

    def __init__(self, server_address, RequestHandlerClass):
        SocketServer.TCPServer.__init__(self, server_address, RequestHandlerClass)

if __name__ == "__main__":
    #Create socket
    server = Server((HOST, PORT), Handler)

    #Initiate ros node and create publisher
    pub_vel = rospy.Publisher("cmd_vel", geometry_msgs.msg.Twist)	# publish velocities
    dump_LA_pub = rospy.Publisher("dump_pos", std_msgs.msg.UInt8)	# pulish dumping info
    susp_LA_pub = rospy.Publisher("susp_pos", std_msgs.msg.UInt8)	# publish suspension info
    door_LA_pub = rospy.Publisher("door_pos", std_msgs.msg.UInt8)
    auger_Speed_pub = rospy.Publisher("auger_speed", std_msgs.msg.UInt8)
    rospy.Subscriber("slam_out_pose", PoseStamped, posCallback)
    rospy.init_node(NODE_NAME)

    # terminate with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)


