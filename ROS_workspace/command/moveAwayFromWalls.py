import rospy
from sensor_msgs.msg import LaserScan
import roslib; roslib.load_manifest('command')


def getDistances(data):

	#should extract distances from /scan and return them
	
	# http://www.ros.org/doc/api/sensor_msgs/html/msg/LaserScan.html
	# get distance values for 0, 90, 180 deg.

	#dummy defaults
	rightDistance = data.ranges[0]
	frontDistance = data.ranges[len(data.ranges)/2]
	leftDistance = data.ranges[-1]

	rospy.loginfo( "lfr: " +str(leftDistance) + ' ' + str(frontDistance) + ' ' + str(rightDistance))

	return leftDistance, frontDistance, rightDistance

def scanCallback(data):
	leftDistance, frontDistance, rightDistance = getDistances(data)
	quadrant = determineQuadrant(leftDistance, frontDistance, rightDistance)
	rospy.loginfo(str(quadrant))

def determineQuadrant(leftDistance, frontDistance, rightDistance):
	'''
		Assume we start in the bottom left corner for this description. The code is general and would work in either corner
		Our orientation could be in one of 4 quadrants
		Describe these quadrants with regular math conventions, ie 0 deg. is positive arena x, quandrant number increases CCW

		if we start in the bottom right, then  quadrant 3 is in the corner, increasing CcW
	'''

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


if (__name__ == "__main__"):
	rospy.init_node('initialHeadingCalculator')
	rospy.Subscriber("scan", LaserScan, scanCallback)
	rospy.spin()		
