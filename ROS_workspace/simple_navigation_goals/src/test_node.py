#!/usr/bin/env python

#IMPORTS
import roslib; roslib.load_manifest('simple_navigation_goals')

#--packages
import rospy
import tf
from tf.transformations import euler_from_quaternion
import math

#--messages
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import PoseStamped

#--state
slam_out_pose=PoseStamped()

#CALLBACKS
def slam_out_pose_callback(data):
	slam_out_pose=data
	angles = euler_from_quaternion([slam_out_pose.pose.orientation.x,slam_out_pose.pose.orientation.y, slam_out_pose.pose.orientation.z, slam_out_pose.pose.orientation.w])
	print('rotation: ',[(180.0/math.pi)*i for i in angles])
	#print(angles[2])

rospy.init_node('get_hector_angle')

rospy.Subscriber("slam_out_pose", PoseStamped, slam_out_pose_callback)

rospy.spin()


