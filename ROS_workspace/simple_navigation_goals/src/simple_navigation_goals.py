#!/usr/bin/env python

#IMPORTS
import roslib; roslib.load_manifest('simple_navigation_goals')

#--packages
import rospy
import tf
import math
import actionlib  #CLIENT API: http://www.ros.org/doc/api/actionlib/html/classactionlib_1_1simple__action__client_1_1SimpleActionClient.html#a186f5d08f708c020b5f321bec998caff
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

#--state vars
corner_detector_request = corner_detectorRequest()
corner_detector_response = 0
hector_heading_deg = 0 
hector_pos_x = 0
hector_pos_y = 0

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

#INIT NODE & ACTIONLIB
#--Init node
rospy.init_node('move_base_client_py')

#--Subscribers
rospy.Subscriber("map", OccupancyGrid, map_callback)
rospy.Subscriber("map_metadata", MapMetaData, map_metadata_callback)
rospy.Subscriber("slam_out_pose", PoseStamped, slam_out_pose_callback)


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

goal.target_pose.pose.position.x = 1.0
goal.target_pose.pose.position.y = 0.0 
quat = tf.transformations.quaternion_from_euler(0, 0, 0) #was 0, 0, math.pi
goal.target_pose.pose.orientation = Quaternion(*quat)

client.send_goal(goal)  
client.wait_for_result() 




