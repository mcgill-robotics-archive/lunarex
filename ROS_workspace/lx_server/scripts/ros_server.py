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

#Don't need these actually
COM='/dev/ttyACM0'
BAUD=115200

#Data package sent fomr this server to the client
class Data:
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

class Handler(SocketServer.BaseRequestHandler):
    def setup(self):
        self.currentState = Data(0.0,0.0,0.0)

        self.initialTime = int(time.time()*1000.0)
        self.currentTime = int(time.time()*1000.0)

        self.request.setblocking(0)

        self.datalist = []
        #self.ser=serial.Serial(COM,BAUD,timeout=1)
        self.count=0

        print str(self.request.getpeername())+" connected"

    def handle(self):
        while(True):
            self.currentTime = int(time.time()*1000.0)
            try:
                self.datalist = self.request.recv(6)
                '''
                # Print Statements just for test
                print 'data received: '
                print (ord)(self.datalist[1])
                print (ord)(self.datalist[2])
                '''

                #Only if data is received will publisher work
                if len(self.datalist) > 0:
                    #Create velocity message
                    linear_vel = (float)((ord)(self.datalist[1]))
                    angular_vel = (float)((ord)(self.datalist[2]))

                    max_speed_linear = 1.8
                    max_speed_angular = 4.0
					#convert back from byte to float
                    linear_vel = linear_vel - 127
                    linear_vel = linear_vel*max_speed_linear/128
                    angular_vel = angular_vel - 127
                    angular_vel = angular_vel*max_speed_angular/128
					
                    self.linearVelocity = Velocity(linear_vel, 0.0, 0.0)     #   Linear Velocity from datalist[1]
                    self.angularVelocity = Velocity(0.0, 0.0, angular_vel)    #   Angular Velocity from datalist[2]

                    #Publish to ros
                    if not rospy.is_shutdown():
                        try:
                            pub_vel.publish(self.linearVelocity, self.angularVelocity)  #   Send Twist message to /cmd_vel topic
                            self.datalist = []  #   And prepare datalist for next input
                        except rospy.ROSInterruptException:
                            print 'Error in ROS node'


            except IOError:
                pass

	    '''
            if((self.currentTime-self.initialTime) > 500):
                dataPacket = json.dumps(vars(self.currentState),sort_keys=True,indent=4)
                self.request.send(dataPacket)
                self.initialTime = self.currentTime
                print dataPacket
	    '''

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
    rospy.init_node(NODE_NAME)

    # terminate with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)

