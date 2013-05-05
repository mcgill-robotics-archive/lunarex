#!/usr/bin/env python

#IMPORTS
import roslib; roslib.load_manifest('simple_navigation_goals')

#--packages
import rospy
import tf
import math	#for cos, sin, pi
import actionlib  #CLIENT API: http://www.ros.org/doc/api/actionlib/html/classactionlib_1_1simple__action__client_1_1SimpleActionClient.html#a186f5d08f708c020b5f321bec998caff
import time
from tf.transformations import euler_from_quaternion

#--messages
from move_base_msgs.msg import MoveBaseAction
from move_base_msgs.msg import MoveBaseGoal
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
from corner_detector.srv import *


#GLOBAL VARS
#--constants
DIG_HEIGHT = 200 #what command should be sent to the suspension LAs to correspond to digging - is 255 all the way down?
TRAVEL_HEIGHT = 0 # what command should be sent to the suspension LAs to correspond to travelling - is 0 all the way up?
DIG_DURATION = 2 # number of circles to trace while digging - half a circle counts as 1 it's really the number of times the robot faces backwards


#--state vars
corner_detector_request = corner_detectorRequest()
corner_detector_response = 0
hector_heading_deg = 0 
hector_pos_x = 0
hector_pos_y = 0

auger_speed = 0 #current speed: 0-255

#CALLBACKS
def map_callback(data):
	#rospy.loginfo("In map callback")
	corner_detector_request.map=data

def map_metadata_callback(data):
	#rospy.loginfo("In map metadata callback")
	corner_detector_request.map_meta=data	

def slam_out_pose_callback(data):
	slam_out_pose=data
	hector_headings = euler_from_quaternion([slam_out_pose.pose.orientation.x,slam_out_pose.pose.orientation.y, slam_out_pose.pose.orientation.z, slam_out_pose.pose.orientation.w])
	hector_heading_deg = hector_headings[2]*(180.0/math.pi)
	hector_pos_x = slam_out_pose.pose.position.x #x increases forward (vert) from the robot
	hector_pos_y = slam_out_pose.pose.position.y #y increases left (horiz) from the robot

#HELPERS
def display_corner_detector_output(corner_detector_response):
	rospy.loginfo("Corner detector output")
	rospy.loginfo("Left bottom: "+str(corner_detector_response.left_bottom_corner))
	rospy.loginfo("Right bottom: "+str(corner_detector_response.right_bottom_corner))
	rospy.loginfo("Left top: "+str(corner_detector_response.left_top_corner))
	rospy.loginfo("Right top: "+str(corner_detector_response.right_top_corner))

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
	susp_LA_pub.publish(DIG_HEIGHT)	# Send suspension info
		
	#-- Drive in circles
	circlesCompleted = 0
	alreadyIncremented = False
	
	while circlesCompleted < DIG_DURATION:	#abort once circlesCompleted == DIG_DURATION			
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
	susp_LA_pub.publish(TRAVEL_HEIGHT)	# Send suspension info

	#-- stop auger
	setAugerSpeed(0);

	'''
	Obsolete algorithms for digging circle

	# drive through circular waypoints for a discrete parametrizable number of times
	#for theta in range(0,DIG_DURATION*2*math.pi, 0.1)	#range(start, end, step)
	#	goal.target_pose.pose.position.x = digCenterX + digRadius*math.cos(theta)
	#	goal.target_pose.pose.position.y = digCenterY + digRadius*math.sin(theta)
	#	time.sleep(500) #milliseconds
		#WILL THIS LOOP HANG UP THE WHOLE ROBOT WHILE DIGGING???

	#alternative circling loop
		# send new goal once first goal is reached
		#this wouldnt send constant velocity though - disadvantage
		
	'''				

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


#INIT NODE & ACTIONLIB
#--Init node
rospy.init_node('move_base_client_py')

#--Subscribers
rospy.Subscriber("map", OccupancyGrid, map_callback)
rospy.Subscriber("map_metadata", MapMetaData, map_metadata_callback)
rospy.Subscriber("slam_out_pose", PoseStamped, slam_out_pose_callback)

#--Publishers
auger_Speed_pub = rospy.Publisher("auger_speed", std_msgs.msg.UInt8)
susp_LA_pub = rospy.Publisher("susp_pos", std_msgs.msg.UInt8)	# publish suspension info
pub_vel = rospy.Publisher("cmd_vel", geometry_msgs.msg.Twist)	# publish velocities

#--Init corner detector
# rospy.loginfo("Started waiting for corner detector service")
# rospy.wait_for_service('corner_detector_srv')
# rospy.loginfo("Done waiting for corner detector service")
# corner_detector_proxy = rospy.ServiceProxy('corner_detector_srv', corner_detector)

#--Init actionlib
client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
rospy.loginfo("Started waiting for move_base action server")
client.wait_for_server() #Waits until the action server has started up and started listening for goals.
rospy.loginfo("Done waiting for move_base action server")

#--Creates a goal to send to the action server.
goal = MoveBaseGoal()
goal.target_pose.header.frame_id = "base_link"
goal.target_pose.header.stamp = rospy.get_rostime()

#PERFORM FIRST LOCALIZATION
#--Perform rotation 
goal.target_pose.pose.position.x = 0.0
goal.target_pose.pose.position.y = 0.0 
quat = tf.transformations.quaternion_from_euler(0, 0, math.pi) #was 0, 0, math.pi
goal.target_pose.pose.orientation = Quaternion(*quat)

#--perform first 180deg
client.send_goal(goal)  # Sends the goal to the action server.
client.wait_for_result() # Waits for the server to finish performing the action.

#--perform second 180deg
client.send_goal(goal)  
client.wait_for_result() 

#--TODO Add feedback stuff 

#--Call corner detector service & display results
# corner_detector_response = corner_detector_proxy(corner_detector_request)
# display_corner_detector_output(corner_detector_response)

goal.target_pose.pose.position.x = 4.0
goal.target_pose.pose.position.y = 0.0 
quat = tf.transformations.quaternion_from_euler(0, 0, 0) #was 0, 0, math.pi
goal.target_pose.pose.orientation = Quaternion(*quat)

client.send_goal(goal)  
client.wait_for_result() 










#---------------------------- Nick








						
	
        
        
	
						

