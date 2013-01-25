#!/usr/bin/env  python
import sys
import rospy
from std_msgs.msg import Int8

_publishing = False
_pub = None
def start_publishing():
    global _pub
    if _pub is not None:
        return
    print "registering onto listenerpublisher"
    _pub = rospy.Publisher("listenerpublisher", Int8)
    
def callback(data):
    print rospy.get_caller_id(), "I heard %s"%data.data
    start_publishing()
    print "publishing", data.data
    _pub.publish((Int8)(data.data))
    
def listener():
    rospy.init_node("listenerpublisher")
    rospy.Subscriber("commands", Int8, callback)
    rospy.spin()
        
if __name__ == '__main__':
    listener()