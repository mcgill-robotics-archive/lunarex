#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import *
import threading

thread_data = None

def callback(data):
    thread_data = data.data
    print "I heard %s" % thread_data

def getData():
    return thread_data

class listenerThread(threading.Thread):
    def __init__(self, NODE_NAME, topic):
        print "Initiating thread...\n"
        self.NODE_NAME = NODE_NAME
        self.topic = topic
        rospy.init_node(self.NODE_NAME, anonymous = True)
        rospy.Subscriber(self.topic, Int8, callback)
        print "ROS subscriber initiated...\n"
        threading.Thread.__init__(self)

    def run(self):
        try:
            print "Currently running ROS subscriber thread...\n"
            rospy.spin()
        except KeyboardInterrupt:
            sys.exit(0)
