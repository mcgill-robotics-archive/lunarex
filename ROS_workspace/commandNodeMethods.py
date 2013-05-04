import math	#for sin, cos, pi
import time #for sleep

#necessary global variables

currentSpeed = 0 #auger speed - changing this name would be nice
digHeight = 200 #what command should be sent to the suspension LAs to correspond to digging - is 255 all the way down?
travelHeight = 0 # what command should be sent to the suspension LAs to correspond to travelling - is 0 all the way up?
digDuration = 1.5 # number of circles to trace while digging - should be a whole number + 0.5

def excavate():
	# excavation subroutine involves a circular digging pattern
	# first go to the starting point
	# turn on the auger
	# lower suspension to appropriate height
	# drive through circular waypoints for a discrete parametrizable number of times
	# lift suspension
	# stop auger

	#--parameters
	startX = 3.0 	#these positions are arbitrary for now, assume origin in bottom left
	startY = 4.5
	startAng = 0.0 	#set the heading to straight ahead?
	digRadius = 1.3 #defines circular path for digging
	digCenterX = 1.5 #defines circular path for digging
	digCenterY = 4.5 #defines circular path for digging
	#it would be nice to define the starting positions relative to these dig parameters
	
	
	# go to the starting point - upper right

	goal.target_pose.pose.position.x = startX
	goal.target_pose.pose.position.y = startY
	goal.target_pose.pose.orientation.w = startAng

	#turn on auger
	setAugerSpeed(255)
	
	#lower suspension to appropriate height
	# publish suspension height to digHeight here

	# drive through circular waypoints for a discrete parametrizable number of times
	for theta in range(0,digDuration*2*math.pi, 0.1)	#range(start, end, step)
		goal.target_pose.pose.position.x = digCenterX + digRadius*math.cos(theta)
		goal.target_pose.pose.position.y = digCenterY + digRadius*math.sin(theta)
		time.sleep(500) #milliseconds
		#WILL THIS LOOP HANG UP THE WHOLE ROBOT WHILE DIGGING???

	#alternative circling loop
		# send new goal once first goal is reached
		#this wouldnt send constant velocity though - disadvantage
		
	#alternative circling loop
		# publish linear and angular velocities
		# how to know when done though??
		#possibility of incrementing a counter whenever robot is facing backwards

	#lift suspension
	# publish suspension height to travelHeight here

	#stop auger
	setAugerSpeed(0);

def setAugerSpeed(desiredSpeed);
	# smoothly changes auger speed from current to desired (0-255)
	increment = 1	
	# currentSpeed needs to be global
	
	if currentSpeed < desiredSpeed:
		while currentSpeed < desiredSpeed:
			#speed up
			currentSpeed  = currentSpeed + increment
			#publish currentSpeed here	
			time.sleep(100) #milliseconds
			
	elif currentSpeed > desiredSpeed:
		while currentSpeed > desiredSpeed:
			#slow down
			currentSpeed = currentSpeed - increment
			#publish currentSpeed here
			time.sleep(100) #milliseconds
						
						
						