#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import Int8

def callback(data):
    rospy.loginfo(rospy.get_name() + ": I heard %s" % data.data)

#Unrequired comment made from Hadi's Laptops
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("Pubsub", Int8, callback)
    rospy.spin()


if __name__ == '__main__':
    try:
        listener()
    except KeyboardInterrupt:
        sys.exit(0)
