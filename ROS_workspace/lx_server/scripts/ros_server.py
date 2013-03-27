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

pub = None
pub_vel = None

COM='/dev/ttyACM0'
BAUD=115200

class Data:
    def __init__(self,x,y,theta):
        self.x=x
        self.y=y
        self.theta=theta

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
            #self.node_init()
            # self.request is the client connection
            try:
                for i in range(0,5):
                    data = self.request.recv(1)
                    self.datalist.append(data)

		'''
                while(len(self.datalist) > 0):
                    data_in = self.datalist.pop()

                    if(ord(data_in) == 1):
                        self.currentState.x+=1
                    elif(ord(data_in) == 2):
                        self.currentState.x-=1
                    elif(ord(data_in) == 4):
                        self.currentState.y+=1
                    else:
                        self.currentState.y-=1
                    self.count+=1
		    self.processVel(data_in)
                    if(not rospy.is_shutdown()&len(data_in)>0):
                        try:
                            rospy.loginfo(ord(data_in))
                            pub.publish(ord(data_in))
                        except rospy.ROSInterruptException:
                            print 'Error in ROS node'
		'''
		print 'data received: '
		print self.datalist(1)
		self.linearVelocity = Velocity((float)(ord(self.datalist(1))/10), 0.0, 0.0)
		self.angularVelocity = Velocity(0.0, 0.0, (float)(ord(self.datalist(2))/10))
		if not rospy.is_shutdown():
            try:
                pub_vel.publish(self.linearVelocity, self.angularVelocity)
                self.datalist = []
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
    server = Server((HOST, PORT), Handler)
    pub = rospy.Publisher("commands", std_msgs.msg.Int8)
    pub_vel = rospy.Publisher("cmd_vel", geometry_msgs.msg.Twist)	# publish velocities
    rospy.init_node(NODE_NAME)
    # terminate with Ctrl-C
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(0)

