#!/usr/bin/env python
import sys
import os
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
from std_msgs.msg import Bool
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped
from corner_detector.msg import Corners
from command.srv import QuadrantRequest

#GLOBAL VARS
#--constants

#----actuator commands
DIG_HEIGHT_CMD = 150 #what command should be sent to the suspension LAs to correspond to digging - is 255 all the way down?
TRAVEL_HEIGHT_CMD = 0 # what command should be sent to the suspension LAs to correspond to travelling - is 0 all the way up?
DIG_DURATION = 2 # number of circles to trace while digging - half a circle counts as 1 it's really the number of times the robot faces backwards
SUSP_SLEEP_TIME = 4 # how much time (secs) to leave to allow the suspension linear actuators to actuate

#----arena dimensions
ARENA_WIDTH = 3.88
ARENA_LENGTH = 7.38
MINING_BOUNDARY_LOCATION = 4.44  # distance of boundary to lunabin

#----hector speeds
ROTATION_TIME_SECS = 60
LOCALIZATION_ANG_SPEED = 0.1

#----arduino rate
VELOCITY_PUB_TIME_MSECS = 100 #how often to send cmd_vels

#----goTo constants
GOAL_DISTANCE_TOLERANCE = 0.20 #in m
GOAL_ANGLE_TOLERANCE =  0.5 #in degrees 
NAV_ANGULAR_ROTATION = 0.3

NAV_LINEAR_SPEED = 0.15
NAV_LINEAR_SPEED_MINING = 0.0762
NAV_LINEAR_SPEED_NON_MINING = 0.2

Y_THRESH_FOR_REORIENTATION = 0.2
Y_THRESH_FOR_REORIENTATION_MINING = 0.4
Y_THRESH_FOR_REORIENTATION_NON_MINING = 0.2

INITIAL_DRIVE_TIME_MSECS = 5000

#excavation stuff
DIG_RADIUS = 0.8 #defines circular path for digging
START_X = ARENA_WIDTH/2 	#middle of lunarena width
START_Y = ARENA_LENGTH - 2*DIG_RADIUS - 0.9	#offset from far wall by digCircle and safety factor
START_ANG = -90.0 	#set the heading to face right
DIG_SPEED = 0.2 #m/s linear component of velocity - free to choose it to maximize flow rate and avoid choking; ang speed with accomodate

FINAL_LAP_TIME_START = 3*60 #If less than this many seconds remaining, keep digging
FINAL_LAP_TIME_END = 60 #approx time remaining to get back and dump

AUGER_MAX_SPEED = 50
AUGER_MIN_SPEED = 0

#dumping
DUMP_BACKUP_TIME = 4
DUMP_BACKUP_SPEED = 0.1

BUCKET_LIFT_TIME = 10
BUCKET_UP_CMD = 0
BUCKET_DOWN_CMD = 255

DOOR_OPEN_CMD = 255
DOOR_CLOSED_CMD = 0
EMPTYING_TIME = 20

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
hector_pos_x = 0
hector_pos_y = 0
slam_out_pose= PoseStamped()

#----actuators
auger_speed = 0 #current speed: 0-255
suspension_pos = 0

start = False

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

def start_callback(data):
	global start
	start = data
	print(type(data))
	print("In start callback")

def manual_override_callback(data):
	print("in manual override callback")
	if(data.data == True):
		print("killing command node due to manual over-r")
		os._exit(0)		

def setAugerSpeed(desiredSpeed):
	# smoothly changes auger speed from current to desired (0-255)
	INCREMENT = 20
	TIME_BETWEEN_AUGER_INCREMENTS = 0.1 #seconds
	# auger_speed needs to be global
	
	global auger_speed
	if auger_speed < desiredSpeed:
		while auger_speed < desiredSpeed:
			#speed up
			auger_speed  = auger_speed + INCREMENT
			auger_speed = min(auger_speed, 255)	#saturate
			auger_Speed_pub.publish(auger_speed)
			time.sleep(TIME_BETWEEN_AUGER_INCREMENTS) 
			
	elif auger_speed > desiredSpeed:
		while auger_speed > desiredSpeed:
			#slow down
			auger_speed = auger_speed - INCREMENT
			auger_speed = max(auger_speed, 0) #saturate
			auger_Speed_pub.publish(auger_speed)
			time.sleep(TIME_BETWEEN_AUGER_INCREMENTS) 

def spinToHectorAngle(nextGoalAngleHector):
	#print "Spinning to hector angle: " + str(nextGoalAngleHector)
	currentAngle = coord.quatToDegrees(slam_out_pose)
	print "currentAngle: " + str(currentAngle)
	currentTime = int(time.time()*1000.0)
	pubTime = currentTime
	spinSpeed = NAV_ANGULAR_ROTATION
	counter = 0
	while( abs(currentAngle - nextGoalAngleHector) > GOAL_ANGLE_TOLERANCE and counter<=2):
		currentAngle = coord.quatToDegrees(slam_out_pose)
		currentTime = int(time.time()*1000.0)

		# need to turn clockwise
		while (( ((nextGoalAngleHector + 180) % 360) - ((currentAngle + 180) % 360)) %360>180): 
			currentAngle = coord.quatToDegrees(slam_out_pose)
			currentTime = int(time.time()*1000.0)
			if(currentTime - pubTime > VELOCITY_PUB_TIME_MSECS):
				pub_vel.publish(Velocity(0, 0, 0), Velocity(0, 0, -spinSpeed))
				pubTime = int(time.time()*1000.0)
		spinSpeed /= 2

		 # need to turn counter clockwise
		while (( ((nextGoalAngleHector + 180) % 360) - ((currentAngle + 180) % 360)) %360<180): 
			currentAngle = coord.quatToDegrees(slam_out_pose)
			currentTime = int(time.time()*1000.0)
			if(currentTime - pubTime > VELOCITY_PUB_TIME_MSECS):
				pub_vel.publish(Velocity(0, 0, 0), Velocity(0, 0, spinSpeed))
				pubTime = int(time.time()*1000.0)
		spinSpeed /= 2
		counter+=1
	pub_vel.publish(Velocity(0.1, 0, 0), Velocity(0, 0, 0))
	time.sleep(1)
	pub_vel.publish(Velocity(0, 0, 0), Velocity(0, 0, 0))

def goTo(x,y,theta, mining, useTheta):

	# send a specified goal in a compact form
	# All three parameters in Arena coordinates
	print("*******In goTO with heading: " +str(coord.quatToDegrees(slam_out_pose)))
	print("Going to arena pos: x=" +str(x) +" y=" +str(y) +"theta = " +str(theta))

	print("Mining flag is: " +str(mining))

	#set speeds & thresholds according to mode of operation
	if(mining):
		NAV_LINEAR_SPEED = NAV_LINEAR_SPEED_MINING
		Y_THRESH_FOR_REORIENTATION = Y_THRESH_FOR_REORIENTATION_MINING
	else:
		NAV_LINEAR_SPEED = NAV_LINEAR_SPEED_NON_MINING
		Y_THRESH_FOR_REORIENTATION = Y_THRESH_FOR_REORIENTATION_NON_MINING	

	#get X, Y mobile goal
	nextGoal = coord.arena2mobile((x,y), slam_out_pose, LR_corner, RR_corner, RF_corner, LF_corner, mapRes, mapWidth)
	
	print("Next goal is: " + str(nextGoal))
	nextGoalDistance = math.sqrt(nextGoal[0]*nextGoal[0] + nextGoal[1]*nextGoal[1])
	
	correction = False #the first time we execute the while loop body, not a correction
	#While not at goal
	while nextGoalDistance > GOAL_DISTANCE_TOLERANCE :
		#ROTATE TOWARDS GOAL
		nextGoalAngleMobile = math.atan2(nextGoal[1], nextGoal[0]) * 180.0/math.pi
		currentAngle = coord.quatToDegrees(slam_out_pose)
		nextGoalAngleHector = nextGoalAngleMobile + currentAngle + 180
		nextGoalAngleHector = nextGoalAngleHector % 360
		nextGoalAngleHector -= 180
		
		print("nextGoalAngleMobile = " +str(nextGoalAngleMobile) + "currentAngle = " +str(currentAngle) + 
			"nextGoalAngleHector = " +str(nextGoalAngleHector))

		setAugerSpeed(AUGER_MIN_SPEED)
		susp_LA_pub.publish(TRAVEL_HEIGHT_CMD)	
		time.sleep(SUSP_SLEEP_TIME)	#wait to actuate

		spinToHectorAngle(nextGoalAngleHector)

		#back to mining height if in mining mode. start AUGER
		if(mining):
			setAugerSpeed(AUGER_MAX_SPEED)
			susp_LA_pub.publish(DIG_HEIGHT_CMD)
			time.sleep(SUSP_SLEEP_TIME)	#wait to actuate

		print "just turned, current angle is: " + str(coord.quatToDegrees(slam_out_pose))
		#MOVE FORWARD TOWARDS GOAL
		nextGoal = coord.arena2mobile((x,y), slam_out_pose, LR_corner, RR_corner, RF_corner, LF_corner, mapRes, mapWidth)
		
		print("nextGoal after rotation is: x=" +str(nextGoal[0]) +"and y=" +str(nextGoal[1]))
		nextGoalDistance = math.sqrt(nextGoal[0]*nextGoal[0] + nextGoal[1]*nextGoal[1])

		currentTime = int(time.time()*1000.0)
		pubTime = currentTime

		#forward motion
		while(nextGoal[0] > GOAL_DISTANCE_TOLERANCE):
			#add rate to avoid overloading rosserial
			nextGoal = coord.arena2mobile((x,y), slam_out_pose, LR_corner, RR_corner, RF_corner, LF_corner, mapRes, mapWidth)
			
 			currentTime = int(time.time()*1000.0)
		
			if(currentTime - pubTime > VELOCITY_PUB_TIME_MSECS):
				pubTime = int(time.time()*1000.0)
				pub_vel.publish(Velocity(NAV_LINEAR_SPEED, 0, 0), Velocity(0, 0, 0))
 				#("nextGoal during forward movement is: x=" +str(nextGoal[0]) +"and y=" +str(nextGoal[1]))

			#if the y of goal is too big, turn to goal. should only have x component
			# if(abs(nextGoal[1]) > Y_THRESH_FOR_REORIENTATION):
			# 	print("breaking out: Y_THRESH exceeeded: y is " +str(abs(nextGoal[1])))
			# 	nextGoalDistance = math.sqrt(nextGoal[0]*nextGoal[0] + nextGoal[1]*nextGoal[1])
			# 	break
			
			#if our mobile angle is greater than a threshold, break out of here
			nextGoal = coord.arena2mobile((x,y), slam_out_pose, LR_corner, RR_corner, RF_corner, LF_corner, mapRes, mapWidth)
			nextGoalAngleMobile = math.atan2(nextGoal[1], nextGoal[0]) * 180.0/math.pi
			angleThreshForReorientation = math.atan(Y_THRESH_FOR_REORIENTATION/ nextGoal[0])
			angleThreshForReorientation = abs(angleThreshForReorientation)
			angleThreshForReorientation *= 180.0/math.pi
			if(nextGoalAngleMobile > angleThreshForReorientation):
				print("breaking out, nextGoalAngleMobile is greater than " +str(angleThreshForReorientation))
				break

		#future executions of while loop body are corrections
		correction = True

		#if we have overshot in the X, return
		nextGoal = coord.arena2mobile((x,y), slam_out_pose, LR_corner, RR_corner, RF_corner, LF_corner, mapRes, mapWidth)
		if(nextGoal[0] < 0):
			break

	if(mining):
			setAugerSpeed(AUGER_MIN_SPEED)
			susp_LA_pub.publish(TRAVEL_HEIGHT_CMD)	
			time.sleep(SUSP_SLEEP_TIME)	#wait to actuate

	if(useTheta):
		#AT GOAL. NOW FACE REQUEST ARENA ANGLE
		finalHectorAngle = coord.arenaAngle2hectorAngle(theta, LR_corner, RR_corner, RF_corner, LF_corner)
		spinToHectorAngle(finalHectorAngle)

def dumpWithGoTo():
	backup(0.6)
	dump_LA_pub.publish(BUCKET_UP_CMD)
	time.sleep(BUCKET_LIFT_TIME)
	backup(0.5)
	door_LA_pub.publish(DOOR_OPEN_CMD)
	time.sleep(EMPTYING_TIME)
	door_LA_pub.publish(DOOR_CLOSED_CMD)

	goTo(ARENA_WIDTH/2.0, 0.9, 90)	#spin around
	dump_LA_pub.publish(BUCKET_UP_CMD)

#has to be called from x = ARENA_WIDTH/2.0, y = 1
def dump():
	print("dumping")

	print("bucket high")
	dump_LA_pub.publish(BUCKET_UP_CMD)
	time.sleep(BUCKET_LIFT_TIME)

	print("Started backup.")
	dumpStartTime = int(time.time()*1000.0)
	currentTime = dumpStartTime
	lastPubTime = dumpStartTime

	while(currentTime - dumpStartTime < DUMP_BACKUP_TIME*1000.0):
		currentTime = int(time.time()*1000.0)
		if(currentTime - lastPubTime > VELOCITY_PUB_TIME_MSECS):
			pub_vel.publish(Velocity(-DUMP_BACKUP_SPEED, 0, 0), Velocity(0, 0, 0))
			lastPubTime = int(time.time()*1000.0)

	print("Stop")
	pub_vel.publish(Velocity(0, 0, 0), Velocity(0, 0, 0))

	print("open door")
	door_LA_pub.publish(DOOR_OPEN_CMD)
	time.sleep(EMPTYING_TIME)
	door_LA_pub.publish(DOOR_CLOSED_CMD)

def backup(arenaY):
	print("Backing up to: " +str(arenaY))
	nextGoal = coord.arena2mobile((ARENA_WIDTH/2.0,arenaY), slam_out_pose, LR_corner, RR_corner, RF_corner, LF_corner, mapRes, mapWidth)
	nextGoalDistance = nextGoal[0]	#dont want to move horizontally, so send 0 as y and ignore output for y
	print("bakup distance is: " +str(nextGoalDistance))
	currentTime = int(time.time()*1000.0)
	pubTime = currentTime
	while(abs(nextGoalDistance) > GOAL_DISTANCE_TOLERANCE):
		#add rate to avoid overloading rosserial
		
		nextGoal = coord.arena2mobile((ARENA_WIDTH/2.0,arenaY), slam_out_pose, LR_corner, RR_corner, RF_corner, LF_corner, mapRes, mapWidth)

		currentTime = int(time.time()*1000.0)
		if(currentTime - pubTime > VELOCITY_PUB_TIME_MSECS):
			print("publishing negative x vel to backup")
			pubTime = int(time.time()*1000.0)
			pub_vel.publish(Velocity(-NAV_LINEAR_SPEED, 0, 0), Velocity(0, 0, 0))
			nextGoalDistance = nextGoal[0]
			
			print("nextGoal during backward movement is: x=" +str(nextGoal[0]) +"and y=" +str(nextGoal[1]))

def moveAwayFromWalls():
	'''
	call service to get initial discrete heading and drive accordingly
	if can't go forward or backward, turn a bit and try again
	'''
	print("waiting for initial heading service")
	rospy.wait_for_service('findInitialHeadingService')
	headingService = rospy.ServiceProxy('findInitialHeadingService', QuadrantRequest)

	haventMovedYet = True
	while haventMovedYet:
		try:
		  quadrant = headingService().quadrant
		  print quadrant
		except rospy.ServiceException, e:
		  print "Service did not process request: %s"%str(e)
		  return
		if quadrant == 1:
			#drive forwards
			angSpeed = 0
			linSpeed = 0.2
			haventMovedYet = False
		elif quadrant == 2:
			angSpeed = -LOCALIZATION_ANG_SPEED	#cw
			linSpeed = 0
		elif quadrant == 3:
			#drive backwards
			angSpeed = 0
			linSpeed = -0.2
			haventMovedYet = False
		elif quadrant == 4:	
			angSpeed = LOCALIZATION_ANG_SPEED #ccw
			linSpeed = 0.2
		else:
			print "BAD HEADING: " + str(quadrant)
			angSpeed = 0
			linSpeed = 0

		currentTime = int(time.time()*1000.0)
		startTime = currentTime
		pubTime = currentTime
		while (currentTime - startTime) < INITIAL_DRIVE_TIME_MSECS:
			currentTime = int(time.time()*1000.0)
			if(currentTime - pubTime > VELOCITY_PUB_TIME_MSECS):	#publish at 10 hz
				pubTime = int(time.time()*1000.0)	#reset pubtine to current time
				pub_vel.publish(Velocity(linSpeed, 0, 0), Velocity(0, 0, angSpeed))

def elapsedTime(option = None):	#optional arguments could change things
	currentTime = int(time.time())
	elapsedSeconds = currentTime - runStartTime
	elapsedPercent = elapsedSeconds/6.0
	remainingSeconds = 600 - elapsedSeconds
	if option == 'percent':
		return elapsedPercent
	elif option == 'remaining':
		return remainingSeconds
	else:
		return elapsedSeconds

class Velocity:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z	

#----------------------------------------------------------------------#
#-----------------------START EXECUTION--------------------------------#
#----------------------------------------------------------------------#
#--Init node
rospy.init_node('command')

#--Subscribers
rospy.Subscriber("slam_out_pose", PoseStamped, slam_out_pose_callback)
rospy.Subscriber("corners", Corners, corners_callback)
rospy.Subscriber("start", Bool, start_callback)
rospy.Subscriber("manual_override", Bool, manual_override_callback)

#--Publishers
auger_Speed_pub = rospy.Publisher("auger_speed", UInt8)
susp_LA_pub = rospy.Publisher("susp_pos", UInt8)	# publish suspension info
dump_LA_pub = rospy.Publisher("dump_pos", UInt8)
pub_vel = rospy.Publisher("cmd_vel", Twist)	# publish velocities
door_LA_pub = rospy.Publisher("door_pos", UInt8)

#--Get Initial heading and get outa there

#print("Moving away from walls")
#moveAwayFromWalls()

#START MOTION
# print("WAITING FOR START FLAG")

# while(not start):
# 	time.sleep(1)

runStartTime = int(time.time())	# seconds

print("STARTING COMMAND NODE")

#sleep to make sure rosserial has started 
time.sleep(5)

#rosserial has started. go high
susp_LA_pub.publish(TRAVEL_HEIGHT_CMD)	
time.sleep(SUSP_SLEEP_TIME)	#wait to actuate

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

# #Get corners
while(mapRes == -1): #means callback has not happened
	time.sleep(2)

print("Got good corners.")

print("they are: LR=" +str(LR_corner) +", RR=" +str(RR_corner)
		+ ", LF=" +str(LF_corner) + ", RF=" +str(RF_corner))

#go to good startin pos in starting area
#ARGS=X   Y    Theta ,Mining, useTheta
if(startedLeft == True):
	goTo(3.2, 1.0, 90, False, False)	

#go first position in mining area (crosses obstacle area)
goTo(3.5, 5.5, 90, False, False)

#excavateStraight()
#send excavation goals
goals = [(1.0, 5.5, 0), (3.2, 5.5, -90)]
for g in goals:
	goTo(g[0], g[1], g[2], True, False)

#come back
#useTheta must be true because going to dump after
goTo(4.58/2.0, 1.0, 90, False, True)

dump()

#6.69 by 4.58

time.sleep(10000)