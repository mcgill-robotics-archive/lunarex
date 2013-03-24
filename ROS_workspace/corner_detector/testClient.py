#!/usr/bin/env python
import roslib; roslib.load_manifest('corner_detector')

import sys

import rospy
from corner_detector.srv import *

#IMPORTS
import rosbag
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Int8
import numpy as np
import roslib.message
import math
import struct
import geometry_msgs.msg
import nav_msgs.msg
import std_msgs.msg
from pylab import *
import matplotlib.gridspec as gridspec

#BAG SETUP
bag = rosbag.Bag('/home/ernie/Dropbox/LunarEx2012-2013/Software Team/ROS/Bags/localization_feb10.bag')

request = corner_detectorRequest()

for topic, msg, t in bag.read_messages(topics=['/map_metadata']):
	request.map_meta = msg
	break

for topic, msg, t in bag.read_messages(topics=['/map']):
	request.map = msg

rospy.wait_for_service('corner_detector_srv')
print("done waiting for corner_detector service")
try:
	corner_det = rospy.ServiceProxy('corner_detector_srv', corner_detector)
	response = corner_det(request)
	print(response.lower_left)
	print(response.lower_right)
	print(response.top_left)
	print(response.top_right)
except rospy.ServiceException, e:
	print "Service call failed: %s"%e
