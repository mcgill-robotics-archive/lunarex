#!/usr/bin/env python
import roslib; roslib.load_manifest('tf_service_test')

import sys

import rospy
from tf_service_test.srv import *

import numpy as np


if __name__ == "__main__":
    try:
        rospy.init_node('test_service_client')
        rate = rospy.Rate(1.0)
        while not rospy.is_shutdown:
            rospy.wait_for_service('test_service')
            try:
                service_resp = rospy.ServiceProxy('test_service', TestSrv)
                response = service_resp(0)  #Send a request
                print "height: %d" % response.height
                print "width: %d" % response.width
                print response.kinect_map
            except rospy.ServiceException, e:
                print "Service call failed: %s" % e
                rate.sleep()
    except KeyboardInterrupt:
        sys.exit(0)
