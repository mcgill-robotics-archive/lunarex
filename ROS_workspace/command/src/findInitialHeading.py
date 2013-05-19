#!/usr/bin/env python

#Meant to be a service that determines if the robot is facing a corner or not based on a single lidar scan

import roslib; roslib.load_manifest('command')
import rospy
from sensor_msgs.msg import LaserScan
from command.srv import *
import time

latestScan = 0

def scanCallback(data):
	global latestScan
	latestScan = data

def getQuadrant(self):
	while(latestScan == 0):
		print("waiting for a scan")
		time.sleep(2)
	'''
		Assume we start in the bottom left corner for this description. The code is general and would work in either corner
		Our orientation could be in one of 4 quadrants
		Describe these quadrants with regular math conventions, ie 0 deg. is positive arena x, quandrant number increases CCW

		if we start in the bottom right, then  quadrant 3 is in the corner, increasing CcW
	'''
	rightDistance = latestScan.ranges[0]
	frontDistance = latestScan.ranges[len(latestScan.ranges)/2]
	leftDistance = latestScan.ranges[-1]

	print( "lfr: " +str(leftDistance) + ' ' + str(frontDistance) + ' ' + str(rightDistance))

	THRESHOLD = 3.0 # meter

	if (frontDistance > THRESHOLD):
		#facing away from walls, Quadtant 1
		#drive forwards
		#publish positive linear command velocity
		quadrant = 1
		pass
	elif (rightDistance > THRESHOLD):
		# quadrant 2
		quadrant = 2
		pass
	elif (leftDistance > THRESHOLD):
		# quadrant 4
		# turn 90 degrees and do it again
		quadrant = 4
		pass
	else:
		# Facing the corner, Quadrant 3
		# back up
		quadrant = 3
		pass

	return quadrant


rospy.init_node('findInitialHeadingServer')
s = rospy.Service('findInitialHeadingService', QuadrantRequest, getQuadrant)
rospy.Subscriber("scan", LaserScan, scanCallback)
print("ready to find the robot's quadrant")
rospy.spin()		
