#!/usr/bin/env python
import roslib; roslib.load_manifest('kinect_node')

from kinect_node.srv import *
import rospy
import sys
import numpy as np


def handle_service(req):
    print "Returning kinect data matrix"
    kinect_matrix = np.array(createMap(), np.int32)
    return KinectDataResponse(kinect_matrix.shape[0], kinect_matrix.shape[1], np.reshape(kinect_matrix, -1))

def service_server():
    s = rospy.Service('kinect_service', KinectData, handle_service)
    print "Test Server Ready."
    rospy.spin()

def createMap():
    map = [  [  0 for i in range(30)]for ii in range(40)]
    return map

if __name__ == "__main__":
    try:
	rospy.init_node("kinect_srv_server")
	service_server()
    except KeyboardInterrupt:
	sys.exit(0)
