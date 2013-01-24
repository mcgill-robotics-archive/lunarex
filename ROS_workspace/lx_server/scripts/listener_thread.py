#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import String
import threading

thread_data = None

def callback(data):
    thread_data = data.data

def getData():
    return thread_data
    
class listerThread(threading.Thread):
    def __init__(self, NODE_NAME, topic):
        rospy.init_node(NODE_NAME, anonymous = True)
        rospy.Subscriber(topic, Int8, callback)
    
    def run(self):
        rospy.spin()