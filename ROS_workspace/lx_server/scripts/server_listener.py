#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from std_msgs.msg import Int8

def callback(data):
    rospy.loginfo(rospy.get_name() + ": I heard %s" % data.data)

if __name__ == '__main__':
    try:
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("commands", Int8, callback)
        rospy.spin()
        print "Can you see this line?\n"
    except KeyboardInterrupt:
        sys.exit(0)
