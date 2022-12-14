#!/usr/bin/env python
import roslib; roslib.load_manifest('map_builder')
import rospy

#import message types
from std_msgs.msg import *
from nav_msgs.msg import *
from geometry_msgs.msg import *

#import math tools
from numpy import *
import math

#import service data type
from kinect_node.srv import *

# the occupancy grid is 2.5 x 2.5 cm
kinect_grid_size = 10 #cm
occupancy_grid_size = 2.5 #cm

class mapBuilder:
    def __init__(self):
        rospy.init_node("map_builder")
        rospy.Subscriber("map", OccupancyGrid, self.mapCallback)   #subscribe to "/map" to get map from hector_mapping
        rospy.Subscriber("slam_out_pose", PoseStamped, self.poseCallback)   #get the position of the robot
        self.pub = rospy.Publisher("global_map", OccupancyGrid)
        self.obstacle_list = [[2,2],[20,20],[50,50]]
        self.map = None
        self.occupancy_grid = []
		self.angle = 0.0
		self.isLocalized = False
		self.rate = rospy.Rate(0.5)	#period = 2s

    def run(self):
        #rospy.spin()
	
	while not rospy.is_shutdown():
	    rospy.wait_for_service('kinect_service')
	    try:
		self.request = rospy.ServiceProxy('kinect_service', KinectData)
		self.kinect_data = self.request(0)		#Send a request (containing any int) and get response
		self.kinectCallback()
		'''
		print "Height: %d" % self.response.height
		print "Width: %d" % self.response.width
		print self.response.data
		'''
	    except rospy.ServiceException, e:
		print "Service failed: %s" % e
	    self.rate.sleep()	# Alan, make don't omit this line... sleep is needed to make programs work - Seb
		

    def mapCallback(self, grid):
	print "in mapCallback"
        self.map = grid
        self.occupancy_grid = [grid.data[i] for i in range(len(grid.data))]     #Damn cool way by Seb_The_Guru to create a list out of a tuple - Alan
        
	self.getMapParameters()
        # Add all found kinect obstacles to occupancy list
        # The coordinates in obstacle_list are in occupancyGrid coordinates
        for obstacle in self.obstacle_list:
            self.insertValueInOccupancyGrid(obstacle[0], obstacle[1], 100)
        self.map.data = self.occupancy_grid #Change the occupancy grid to the updated one
        self.pub.publish(self.map)
	
	#print self.obstacle_list

    #Retrieve position data
    def poseCallback(self, pose):
	#print "in poseCallback"
		self.isLocalized = True
        self.position = pose
        self.x_position = self.position.pose.position.x
        self.y_position = self.position.pose.position.y
        #print "Current position:" 
        #print self.x_position, self.y_position
        #print self.position.pose.orientation	
        w = self.position.pose.orientation.w
        z = self.position.pose.orientation.z
		self.angle = math.copysign(2 * math.acos(w) * 180 / math.pi, z)    #True angle calculated using quaternion
		
		#Pose from CMs to cell coordinates
		#WORKS IF map.origin has not been reset (which we might do)
		middlePCoord = self.map.width / 2 #assume width = height
		self.x_coords_on_grid = middleCoord + self.x_position/self.map.resolution
		self.y_coords_on_grid = middleCoord + self.y_position/self.map.resolution
		
		
	#print "Angle: %f" %self.angle #math.copysign(2 * math.acos(w) * 180 / math.pi, z)    #True angle calculated using quaternion


    def getMapParameters(self):
        self.map_height = self.map.info.height  #the height of occupancy gird
        self.map_width = self.map.info.width    #the width of occupancy grid
        self.map_resolution = self.map.info.resolution



    def insertValueInOccupancyGrid(self, x_coord, y_coord, val):
        square_size = 6
        #for i in range(square_size):
        #    for ii in range(square_size):
        #        self.occupancy_grid[(y_coord -3+i) * self.map_width + (x_coord -3+ii)] = val

	self.occupancy_grid[(y_coord ) * self.map_width + (x_coord)] = val

    def kinectCallback(self):
	# the grid is a one d array 
	#print "kinectCallback called"
	if (self.isLocalized == False):
		return None
	print "kinectCallback Running"
        grid   = self.kinect_data.data
	height = self.kinect_data.height
	width  = self.kinect_data.width
	

	for i in range(length):
		row_number = int(i/width)
		element_in_row = i % width
		y = 40 - row_number		# the top row (row[0]) is far away  -- 400 m away 
		x = element_in_row - 14		# 30 elements per row ; element 14 is at the center
		if (grid[i] == 100):
			self.addCoordinates(x, y)

    def addCoordinates(self, x, y):
	# x and y are coordinates on the kinect's frame of reference. 
	# the grid size is the kinect_grid_size --> 10 cm at the moment
	# ie: the kinect is the origin and the y axis points straight forward
	# this functions needs to transfer the kinect obstacle coordinates in the global coordinate frame given by hector_mapping
	
	position_vector = [x,y] 
	#print "addCoordinates" , position_vector
	# rotate the vector to make it match the robot's heading
	position_vector = self.rotateVector2D(position_vector , self.angle)
	
	# account for the different dimention of the kinect grid and the occupancy grid we use
	occupancy_grid_units_per_kinect_units = kinect_grid_size / occupancy_grid_size
	position_vector[0] = 	int (  position_vector[0] * occupancy_grid_units_per_kinect_units   )
	position_vector[1] = 	int (  position_vector[1] * occupancy_grid_units_per_kinect_units   )

	# add the global position of the robot
	position_vector[0] += int( 1024 + self.x_position/2.5 )
	position_vector[1] += int( 1024 + self.x_position/2.5 )
	#print "before addedCoordinates" , [position_vector[0],position_vector[1]]
	#
	if ([position_vector[0],position_vector[1]] not in self.obstacle_list):
        	self.obstacle_list.append([position_vector[0],position_vector[1]])
		print "addedCoordinates" , [position_vector[0],position_vector[1]]
	# *****	
	# *****	We will later need to adjust for the fact that the kinect is not necessarily placed 		
	# ***** at the same place as what is considered to be the robot's centre. 
	# ***** For example, it my be 25 cm at the back. We would then need to remove 50 to the position_vector[1] 
	# *****



    #Rotate a coordinate ector
    def rotateVector2D(self, vector, angle):
        rotated_vect = []
        rotated_vect.append(  vector[0]*math.cos(angle)  - math.sin(angle)             )
        rotated_vect.append(  vector[1]*math.sin(angle)  + vector[1]*math.cos(angle)   )
        return rotated_vect


if __name__ == "__main__":
    try:
        builder = mapBuilder()
        builder.run()


    except KeyboardInterrupt:
        sys.exit(0)
