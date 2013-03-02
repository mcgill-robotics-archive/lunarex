#!/usr/bin/env python
import roslib; roslib.load_manifest('lx_server')
import rospy
from sensor_msgs.msg import LaserScan

pub = None

def callback(data):
    if pub <> None:
        data.header.frame_id = "/base_laser_link"
        pub.publish(data)
        #print "sent from base_scan to scan"

if __name__ == '__main__':
    try:
        rospy.init_node("message_sender")
        rospy.Subscriber("base_scan", LaserScan, callback)
        pub = rospy.Publisher("scan", LaserScan)
        rospy.spin()
    except KeyboardInterrupt:
        sys.exit(0)
