def getDistances():

	#should extract distances from /scan and return them
	

	#dummy defaults
	leftDistance = -1
	frontDistance = -1
	rightDistance = -1

	return leftDistance, frontDistance, rightDistance


def moveAwayFromWalls():
	'''
		Assume we start in the bottom left corner for this description. The code is general and would work in either corner
		Our orientation could be in one of 4 quadrants
		Describe these quadrants with regular math conventions, ie 0 deg. is positive arena x, quandrant number increases CCW

		if we start in the bottom right, then the quadrants are mirrord about the y-axis ie quadrant 3 is in the corner, increasing CW



	'''

	leftDistance, frontDistance, rightDistance = getDistances()


	# http://www.ros.org/doc/api/sensor_msgs/html/msg/LaserScan.html
	# get distance values for 0, 90, 180 deg.



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
	for ang in range(360)
		quad = moveAwayFromWalls(i)
		print "angle = " + str(i)
		print "quadrant = " + str(quad)