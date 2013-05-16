#!/usr/bin/env python
import sys
sys.path.append("~/McGill_LunarEx_2013/ROS_workspace/")
sys.path.append("/home/ernie/McGill_LunarEx_2013/ROS_workspace")
sys.path.append("/home/lunarex/McGill_LunarEx_2013/ROS_workspace")


#IMPORTS
import roslib; roslib.load_manifest('command')

#--packages
import rospy
import tf
import math	#for cos, sin, pi
import actionlib  #CLIENT API: http://www.ros.org/doc/api/actionlib/html/classactionlib_1_1simple__action__client_1_1SimpleActionClient.html#a186f5d08f708c020b5f321bec998caff
import time
import coord

#--messages
from std_msgs.msg import UInt32
from std_msgs.msg import UInt8
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
from corner_detector.msg import Corners

#GLOBAL VARS
#--constants
DIG_HEIGHT_CMD = 200 #what command should be sent to the suspension LAs to correspond to digging - is 255 all the way down?
TRAVEL_HEIGHT_CMD = 0 # what command should be sent to the suspension LAs to correspond to travelling - is 0 all the way up?
DIG_DURATION = 2 # number of circles to trace while digging - half a circle counts as 1 it's really the number of times the robot faces backwards
SUSP_SLEEP_TIME = 2000 # how much time (milliseconds) to leave to allow the suspension linear actuators to actuate

ARENA_WIDTH = 3.88
ARENA_LENGTH = 7.38
MINING_BOUNDARY_LOCATION = 4.44  # distance of boundary to lunabin

MC_WIDTH = 2.33
MC_LENGTH = 7.55

STARTING_POS_ARENA_COORDS = [(0.97, 0.75), (2.91, 0.75)]
ROTATION_TIME_SECS = 60
LOCALIZATION_ANG_SPEED = 1.4
VELOCITY_PUB_TIME_MSECS = 100 #how often to send cmd_vels
GOAL_DISTANCE_TOLERANCE = 0.2 #in m
GOAL_ANGLE_TOLERANCE =  1 #in degrees 
NAV_ANGULAR_ROTATION = 1.4
NAV_LINEAR_SPEED = 1.5

#--state vars
#----corners
LR_corner = [-1, -1]
RR_corner = [-1, -1]
LF_corner = [-1, -1]
RF_corner = [-1, -1]
mapRes = -1
mapWidth = -1
mapHeight = -1
startedLeft = True 

#----pose-related
hector_heading_deg = 0 
hector_pos_x = 0
hector_pos_y = 0
slam_out_pose= PoseStamped()

#----actuators
auger_speed = 0 #current speed: 0-255
suspension_pos = 0

#----control
#cmd-vel state var?

#INFO: logging stuff to rosout
#rospy.logerr / logwarn / loginfo

#CALLBACKS
def corners_callback(data):
	print("In corners callback")
	global LR_corner
	global RR_corner
	global LF_corner
	global RF_corner
	global mapRes
	global mapWidth
	global mapHeight
	global startedLeft

	LR_corner = data.LR_corner
	RR_corner = data.RR_corner
	LF_corner = data.LF_corner
	RF_corner = data.RF_corner
	mapRes = data.resolution
	mapWidth = data.width
	mapHeight = data.height
	startedLeft = data.left

def slam_out_pose_callback(data):
	global slam_out_pose
	slam_out_pose=data

#HELPERS

#SUBROUTINES
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
		Therefore DIG_RADIUS should be 1.75/2 = 0.875 m
		This is also the ackerman radius

	Arclength is defined as Length = R*theta
	Differentiate both sides, linear velocity = R*Angular velocity

	R is given above (DIG_RADIUS). We want to be able to calibrate linear velocity (along with suspension height) to maximize flow rate and avoid choking the auger. Therefore angular velocity is a function of the other two parameters:

	AngVel = LinVel/DIG_RADIUS
	
	'''
 	#-- parameters
	DIG_RADIUS = 0.875 #defines circular path for digging
	START_X = 3.88/2 	#middle of lunarena width
	START_Y = 7.38 - 2*DIG_RADIUS - 0.22	#offset from far wall by digCircle and safety factor
	START_ANG = -90.0 	#set the heading to face right
	DIG_SPEED = 1 #m/s linear component of velocity - free to choose it to maximize flow rate and avoid choking; ang speed with accomodate

	#-- go to the starting point
	goal.target_pose.pose.position.x = START_X
	goal.target_pose.pose.position.y = START_Y
	arenaGoalAngle = coord.arenaAngle2mobileAngle(START_ANG * math.pi/180.0, slam_out_pose, LR_corner, RR_corner, RF_corner, LF_corner)
	quat = tf.transformations.quaternion_from_euler(0, 0,arenaGoalAngle) 
	goal.target_pose.pose.orientation = Quaternion(*quat)
	

	client.send_goal(goal)  # Sends the goal to the action server.
	client.wait_for_result() # Waits for the server to finish performing the action.

	#-- turn on auger
	setAugerSpeed(255)	#call custom method
	
	#-- lower suspension to appropriate height
	susp_LA_pub.publish(DIG_HEIGHT_CMD)	# Send suspension info
	time.sleep(SUSP_SLEEP_TIME)	#wait to actuate

	#-- Drive in circles
	circlesCompleted = 0
	alreadyIncremented = False
	
	while circlesCompleted < DIG_DURATION:	#abort once circlesCompleted == DIG_DURATION			
		linVelObject = Velocity(DIG_SPEED, 0.0, 0.0)		#create the object
		angVelObject = Velocity(0.0, 0.0, DIG_SPEED/DIG_RADIUS)	#see docstring for geometry explanation		
		pub_vel.publish(linVelObject, angVelObject)  #   Send Twist message to /cmd_vel topic

		#--Count number of circles
		if hector_heading_deg > 178.00 and not alreadyIncremented:
			circlesCompleted += 1
			alreadyIncremented = True
		if hector_heading_deg > -160 and hector_heading_deg < 0:
			alreadyIncremented = False	#reset

	#-- Stop locomotion
	pub_vel.publish(Velocity(0.0, 0.0, 0.0), Velocity(0.0, 0.0, 0.0))
	
	#-- lift suspension
	susp_LA_pub.publish(TRAVEL_HEIGHT_CMD)	# Send suspension info
	time.sleep(SUSP_SLEEP_TIME)	#wait to actuate

	#-- stop auger
	setAugerSpeed(0);

	'''
	Obsolete algorithms for digging circle

	# drive through circular waypoints for a discrete parametrizable number of times
	#for theta in range(0,DIG_DURATION*2*math.pi, 0.1)	#range(start, end, step)
	#	goal.target_pose.pose.position.x = digCenterX + DIG_RADIUS*math.cos(theta)
	#	goal.target_pose.pose.position.y = digCenterY + DIG_RADIUS*math.sin(theta)
	#	time.sleep(500) #milliseconds
		#WILL THIS LOOP HANG UP THE WHOLE ROBOT WHILE DIGGING???

	#alternative circling loop
		# send new goal once first goal is reached
		#this wouldnt send constant velocity though - disadvantage
		
	'''				

def setAugerSpeed(desiredSpeed):
	# smoothly changes auger speed from current to desired (0-255)
	INCREMENT = 10
	TIME_BETWEEN_AUGER_INCREMENTS = 100 #milliseconds
	# auger_speed needs to be global
	
	if auger_speed < desiredSpeed:
		while auger_speed < desiredSpeed:
			#speed up
			auger_speed  = auger_speed + INCREMENT
			auger_speed = min(auger_speed, 255)	#saturate
			auger_Speed_pub.publish(auger_speed)
			time.sleep(TIME_BETWEEN_AUGER_INCREMENTS) #milliseconds
			
	elif auger_speed > desiredSpeed:
		while auger_speed > desiredSpeed:
			#slow down
			auger_speed = auger_speed - INCREMENT
			auger_speed = max(auger_speed, 0) #saturate
			auger_Speed_pub.publish(auger_speed)
			time.sleep(TIME_BETWEEN_AUGER_INCREMENTS) #milliseconds

def goTo(x,y,theta):
	# send a specified goal in a compact form
	# All three parameters in Arena coordinates

	print("In goTO with heading: " +str(coord.quatToDegrees(slam_out_pose)))

	nextGoal = coord.arena2mobile((x,y), slam_out_pose, LR_corner, RR_corner, RF_corner, LF_corner, mapRes, mapWidth)
	
	print("Next goal is: " + str(nextGoal))

	nextGoalAngle = math.atan2(nextGoal[1], nextGoal[0]) * 180.0/math.pi
	currentAngle = coord.quatToDegrees(slam_out_pose)
	
	print currentAngle, nextGoalAngle

	currentTime = int(time.time()*1000.0)
	pubTime = currentTime
	while( abs(currentAngle - nextGoalAngle) > GOAL_ANGLE_TOLERANCE):
		currentTime = int(time.time()*1000.0)
		currentAngle = coord.quatToDegrees(slam_out_pose)
		#if(currentAngle > nextGoalAngle):
		if(currentTime - pubTime > VELOCITY_PUB_TIME_MSECS):
			pubTime = int(time.time()*1000.0)
			pub_vel.publish(Velocity(0, 0, 0), Velocity(0, 0, NAV_ANGULAR_ROTATION))

	nextGoal = coord.arena2mobile((x,y), slam_out_pose, LR_corner, RR_corner, RF_corner, LF_corner, mapRes, mapWidth)
	nextGoalDistance = math.sqrt(nextGoal[0]*nextGoal[0] + nextGoal[1]*nextGoal[1])

	currentTime = int(time.time()*1000.0)
	pubTime = currentTime
	while(nextGoalDistance > GOAL_DISTANCE_TOLERANCE):
		print nextGoalDistance
		#add rate to avoid overloading rosserial
		currentTime = int(time.time()*1000.0)
	
		if(currentTime - pubTime > VELOCITY_PUB_TIME_MSECS):
			pubTime = int(time.time()*1000.0)
			pub_vel.publish(Velocity(NAV_LINEAR_SPEED, 0, 0), Velocity(0, 0, 0))
			nextGoal = coord.arena2mobile((x,y), slam_out_pose, LR_corner, RR_corner, RF_corner, LF_corner, mapRes, mapWidth)
			nextGoalDistance = math.sqrt(nextGoal[0]*nextGoal[0] + nextGoal[1]*nextGoal[1])

class Velocity:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z	

#----------------------------------------------------------------------#
#-----------------------START EXECUTION--------------------------------#
#----------------------------------------------------------------------#

#INIT NODE & ACTIONLIB
#--Init node
rospy.init_node('command')

#--Subscribers
rospy.Subscriber("slam_out_pose", PoseStamped, slam_out_pose_callback)
rospy.Subscriber("corners", Corners, corners_callback)

#--Publishers
auger_Speed_pub = rospy.Publisher("auger_speed", UInt8)
susp_LA_pub = rospy.Publisher("susp_pos", UInt8)	# publish suspension info
pub_vel = rospy.Publisher("cmd_vel", Twist)	# publish velocities

#START MOTION

#Perform rotation
print("Started rotation.")
rotationStartTime = int(time.time()*1000.0)
currentTime = rotationStartTime
lastPubTime = rotationStartTime

while(currentTime - rotationStartTime < ROTATION_TIME_SECS*1000.0):
	currentTime = int(time.time()*1000.0)
	if(currentTime - lastPubTime > VELOCITY_PUB_TIME_MSECS):
		pub_vel.publish(Velocity(0, 0, 0), Velocity(0, 0, LOCALIZATION_ANG_SPEED))
		lastPubTime = int(time.time()*1000.0)

#perform stop
pub_vel.publish(Velocity(0, 0, 0), Velocity(0, 0, 0))

print("Ended rotation. Now waiting for good corners")

#Get corners
while(mapRes == -1): #means callback has not happened
	print("mapRes still default")
	time.sleep(2)

print("Got good corners.")

print("Returning: LR=" +str(LR_corner) +", RR=" +str(RR_corner)
		+ ", LF=" +str(LF_corner) + ", RF=" +str(RF_corner))

goTo(3.40, 4.38, 0)

#EXCAVATE
#excavate()

#Return home and dump
#goTo(MC_WIDTH/2.0, 0.9, 0)	#need to callibrate y position so as not to bump into wall or obstacle
goTO(1.7, 4.5)
#goTo(ARENA_WIDTH/2.0, 0.9, math.pi)	#spin around

