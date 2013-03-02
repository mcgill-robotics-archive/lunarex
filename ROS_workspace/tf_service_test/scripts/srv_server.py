#!/usr/bin/env python
import roslib; roslib.load_manifest('tf_service_test')

from tf_service_test.srv import *
import rospy
import sys
import numpy as np

test_matrix = np.array([[1,2],[3,4],[5,6]], np.int32)

def handle_service(req):
    print "Returning kinect data matrix"
    return TestSrvResponse(a.shape[0], a.shape[1], np.reshape[a, -1])

def service_server():
    s = rospy.Service('test_service', TestSrv, handle_service)
    print "Test Server Ready."
    rospy.spin()

if __name__ == "__main__":
    try:
	rospy.init_node("test_srv_server")
	service_server()
    except KeyboardInterrupt:
	sys.exit(0)
