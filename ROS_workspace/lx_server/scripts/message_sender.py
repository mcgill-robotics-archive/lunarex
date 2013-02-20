#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from sensor_msgs.msg import LaserScan

pub = None

def callback(data):
    pub.publish(data)
    print "sent from base_scan to scan"

if __name__ == '__main__':
    try:
        rospy.init_node("message_sender")
        rospy.Subsriber("base_scan", LaserScan, callback)
        pub = rospy.Publisher("scan", LaseerScan)
        rospy.spin()
    except KeyboardInterrupt:
        sys.exit(0)