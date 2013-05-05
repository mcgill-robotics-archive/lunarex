import math	#for sin, cos, pi
import time #for sleep

#necessary global variables

auger_speed = 0 #auger speed - changing this name would be nice
digHeight = 200 #what command should be sent to the suspension LAs to correspond to digging - is 255 all the way down?
travelHeight = 0 # what command should be sent to the suspension LAs to correspond to travelling - is 0 all the way up?
digDuration = 2 # number of circles to trace while digging - half a circle counts as 1 it's really the number of times the robot faces backwards

# ros publishers
auger_Speed_pub = rospy.Publisher("auger_speed", std_msgs.msg.UInt8)
susp_LA_pub = rospy.Publisher("susp_pos", std_msgs.msg.UInt8)	# publish suspension info
pub_vel = rospy.Publisher("cmd_vel", geometry_msgs.msg.Twist)	# publish velocities


def excavate():
	'''
	 This excavate subroutine involves a circular digging pattern:
	 
	 1. go to the starting point
	 2. turn on the auger
	 3. lower suspension to appropriate height
	 4. drive through circular waypoints for a discrete parametrizable number of times
	 5. lift suspension
	 6. stop auger
	'''
	
	'''
	Geometry of the digging circle
	------------------------------


	Mining area dimensions:
	(convention: x is the width, y is the length - lunabin on wall defined by y = 0)
	x width = 3.88 m
	y height = 2.94 m

	Want to leave a buffer, so mining circle should not be greater than 2.5 m in diameter
	This leaves 22 cm from the wall and 22 cm from the edge of the obstacle area.

	This circle should be traced by the outside of the robot. Considering the centre of the robot, subtract half the width on each side of the circle -> subtract the whole width
		2.5 - 0.75 = 1.75m
		Therefore digRadius should be 1.75/2 = 0.875 m
		This is also the ackerman radius

	Arclength is defined as Length = R*theta
	Differentiate both sides, linear velocity = R*Angular velocity

	R is given above (digRadius). We want to be able to calibrate linear velocity (along with suspension height) to maximize flow rate and avoid choking the auger. Therefore angular velocity is a function of the other two parameters:

	AngVel = LinVel/digRadius
	
	'''
	


	#-- parameters
	digRadius = 0.875 #defines circular path for digging
	startX = 3.88/2 	#middle of lunarena width
	startY = 7.38 - 2*digRadius - 0.22	#offset from far wall by digCircle and safety factor
	startAng = -90.0 	#set the heading to face right
	digSpeed = 1 #m/s linear component of velocity - free to choose it to maximize flow rate and avoid choking; ang speed with accomodate

	#-- go to the starting point
	goal.target_pose.pose.position.x = startX
	goal.target_pose.pose.position.y = startY
	goal.target_pose.pose.orientation.w = startAng

	client.send_goal(goal)  # Sends the goal to the action server.
	client.wait_for_result() # Waits for the server to finish performing the action.

	#-- turn on auger
	setAugerSpeed(255)	#call custom method
	
	#-- lower suspension to appropriate height
	susp_LA_pub.publish(digHeight)	# Send suspension info
		
	#-- Drive in circles
	circlesCompleted = 0
	alreadyIncremented = False
	
	while circlesCompleted < digDuration:	#abort once circlesCompleted == digDuration			
		linVelObject = Velocity(digSpeed, 0.0, 0.0)		#create the object
		angVelObject = Velocity(0.0, 0.0, digSpeed/digRadius)	#see docstring for geometry explanation		
		pub_vel.publish(linVelObject, angVelObject)  #   Send Twist message to /cmd_vel topic

		#--Count number of circles
		if heading > 178.00 and not alreadyIncremented:
			circlesCompleted += 1
			alreadyIncremented = True
		if heading > -160 and heading < 0:
			alreadyIncremented = False	#reset

	#-- Stop locomotion
	pub_vel.publish(Velocity(0.0, 0.0, 0.0), Velocity(0.0, 0.0, 0.0))
	
	#-- lift suspension
	susp_LA_pub.publish(travelHeight)	# Send suspension info

	#-- stop auger
	setAugerSpeed(0);

def setAugerSpeed(desiredSpeed);
	# smoothly changes auger speed from current to desired (0-255)
	increment = 10	
	# auger_speed needs to be global
	
	if auger_speed < desiredSpeed:
		while auger_speed < desiredSpeed:
			#speed up
			auger_speed  = auger_speed + increment
			auger_speed = min(auger_speed, 255)	#saturate
			auger_Speed_pub.publish(auger_speed)
			time.sleep(100) #milliseconds
			
	elif auger_speed > desiredSpeed:
		while auger_speed > desiredSpeed:
			#slow down
			auger_speed = auger_speed - increment
			auger_speed = max(auger_speed, 0) #saturate
			auger_Speed_pub.publish(auger_speed)
			time.sleep(100) #milliseconds
						
class Velocity:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z		
        
        
	'''
	Obsolete algorithms for digging circle

	# drive through circular waypoints for a discrete parametrizable number of times
	#for theta in range(0,digDuration*2*math.pi, 0.1)	#range(start, end, step)
	#	goal.target_pose.pose.position.x = digCenterX + digRadius*math.cos(theta)
	#	goal.target_pose.pose.position.y = digCenterY + digRadius*math.sin(theta)
	#	time.sleep(500) #milliseconds
		#WILL THIS LOOP HANG UP THE WHOLE ROBOT WHILE DIGGING???

	#alternative circling loop
		# send new goal once first goal is reached
		#this wouldnt send constant velocity though - disadvantage
		
	'''				
						