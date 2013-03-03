#!/usr/bin/env python
import roslib; roslib.load_manifest('tf_service_test')

import sys

import rospy
#from tf_service_test.srv import *
from kinect_node.srv import *
from std_msgs.msg import Int8

import numpy as np


if __name__ == "__main__":
    try:
        rospy.init_node('test_service_client', anonymous = True)
        print "Node Initiated."
        rate = rospy.Rate(1.0)
        print "Rate set."
        while not rospy.is_shutdown():
            print "In loop now."
            #rospy.wait_for_service('test_service')
	    rospy.wait_for_service('kinect_service')
            try:
                #service_resp = rospy.ServiceProxy('test_service', TestSrv)
		service_resp = rospy.ServiceProxy('kinect_service', KinectData)
                response = service_resp(0)  #Send a request
                print "height: %d" % response.height
                print "width: %d" % response.width
                print response.data
            except rospy.ServiceException, e:
                print "Service call failed: %s" % e
                rate.sleep()
    except KeyboardInterrupt:
        sys.exit(0)
