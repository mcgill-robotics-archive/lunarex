#!/usr/bin/env python
import roslib; roslib.load_manifest('map_builder')
import rospy

#import message types
from std_msgs.msg import *
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped

#import math tools
from numpy import *
import math

#import service data type
from kinect_node.srv import *

# the occupancy grid is 2.5 x 2.5 cm

kinect_grid_size = 10 #cm


class mapBuilder:
    def __init__(self):
        rospy.init_node("map_builder")
        rospy.Subscriber("map", OccupancyGrid, self.mapCallback)   #subscribe to "/map" to get map from hector_mapping
        rospy.Subscriber("slam_out_pose", PoseStamped, self.poseCallback)   #get the position of the robot
        self.pub = rospy.Publisher("global_map", OccupancyGrid)
        self.obstacle_list = {}
        self.map = None
        self.occupancy_grid = []
	self.angle = 0.0
	self.isLocalized = False
	
    def run(self):
        #rospy.spin()
	self.rate = rospy.Rate(0.7)	#period = 3s
	while not rospy.is_shutdown() :
	    rospy.wait_for_service('kinect_service')
	    try:
		# update position
		self.x_position = self.x_position_recent 
		self.y_position = self.y_position_recent
		
		print "Called Kinect"
		# call the kinect service
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
	    except AttributeError:
		pass
	    self.rate.sleep()	# Alan, make don't omit this line... sleep is needed to make programs work - Seb


    def mapCallback(self, grid):
	print "in mapCallback"
        self.map = grid
        self.occupancy_grid = [grid.data[i] for i in range(len(grid.data))]     #Damn cool way by Seb_The_Guru to create a list out of a tuple - Alan

	self.getMapParameters()
        # Add all found kinect obstacles to occupancy list
        # The coordinates in obstacle_list are in occupancyGrid coordinates

	#for obstacle in self.obstacle_list:
        #    self.insertValueInOccupancyGrid(obstacle[0], obstacle[1], 100)

	obstacles = self.obstacle_list.items()
	#print obstacles
	for i in range(len(obstacles)):
		self.insertValueInOccupancyGrid(obstacles[i][0][0], obstacles[i][0][1], obstacles[i][1][0])

        self.map.data = self.occupancy_grid #Change the occupancy grid to the updated one
        self.pub.publish(self.map)
	

	#print self.obstacle_list

    #Retrieve position data
    def poseCallback(self, pose):
	#print "in poseCallback"
	self.isLocalized = True
        self.position = pose
        self.x_position_recent = self.position.pose.position.x # transfered to x_position when kinect is called in order to reduce lag
        self.y_position_recent = self.position.pose.position.y # transfered to y_position when kinect is called in order to reduce lag
        #print "Current position:"
        #print self.x_position, self.y_position
        #print self.position.pose.orientation
        w = self.position.pose.orientation.w
        z = self.position.pose.orientation.z
	self.angle = math.copysign(2 * math.acos(w), z) - math.pi/2   #True angle calculated using quaternion
	#print "Angle: %f" %self.angle #math.copysign(2 * math.acos(w) * 180 / math.pi, z)    #True angle calculated using quaternion


    def getMapParameters(self):
        self.map_height = self.map.info.height  #the height of occupancy gird
        self.map_width = self.map.info.width    #the width of occupancy grid
	self.map_size   =  self.map_width * self.map_height
        self.map_resolution = self.map.info.resolution * 100 # map_resolution is in centimeters
	print self.map_resolution



    def insertValueInOccupancyGrid(self, x_coord, y_coord, val):
        #square_size = 6
        #for i in range(square_size):
        #    for ii in range(square_size):
        #        self.occupancy_grid[(y_coord -3+i) * self.map_width + (x_coord -3+ii)] = val

	if (val<=40):
		return 	
	if (val>80):
		val = 100

	occupancy_grid_units_per_kinect_units = math.ceil( kinect_grid_size / self.map_resolution )
	for x in range(int(x_coord),         int(x_coord + occupancy_grid_units_per_kinect_units)):
		for y in range(int(y_coord), int(y_coord + occupancy_grid_units_per_kinect_units)):

			if (self.occupancy_grid[(y ) * self.map_width + (x)] != 100):
				self.occupancy_grid[(y ) * self.map_width + (x)] = val
	'''
	if (self.occupancy_grid[(y_coord ) * self.map_width + (x_coord)] != 100):
		self.occupancy_grid[(y_coord ) * self.map_width + (x_coord)] = val
	#also insert the top, right and top-right diagonal that were rounded down when coordinates were added
	
	if (self.occupancy_grid[(y_coord+1 ) * self.map_width + (x_coord)] != 100):
			self.occupancy_grid[(y_coord+1 ) * self.map_width + (x_coord)] = val
	
	if (self.occupancy_grid[(y_coord ) * self.map_width + (x_coord+1)] != 100):
			self.occupancy_grid[(y_coord ) * self.map_width + (x_coord+1)] = val
	
	if (self.occupancy_grid[(y_coord+1) * self.map_width + (x_coord+1)] != 100):
		self.occupancy_grid[(y_coord+1 ) * self.map_width + (x_coord+1)] = val
	'''
    def kinectCallback(self):
	# the grid is a one d array
	#print "kinectCallback called"
	if (self.isLocalized == False):
		return None
	print "kinectCallback Running", self.x_position, self.y_position
        grid   = self.kinect_data.data
	height = self.kinect_data.height
	width  = self.kinect_data.width
	length = height*width

	for i in range(length):
		row_number = int(i/width)
		element_in_row = i % width
		y = 40 - row_number		# the top row (row[0]) is far away  -- 400 m away
		x = element_in_row - 14		# 30 elements per row ; element 14 is at the center
		if (grid[i] != -1):
			self.addCoordinates(x, y, grid[i])

    def addCoordinates(self, x, y, val):
	# x and y are coordinates on the kinect's frame of reference.
	# the grid size is the kinect_grid_size --> 10 cm at the moment
	# ie: the kinect is the origin and the y axis points straight forward
	# this functions needs to transfer the kinect obstacle coordinates in the global coordinate frame given by hector_mapping


	print "angle", self.angle
	position_vector = [x,y] #the vector from kinect to obstacle, in kinect units
	print "addCoordinates" , position_vector 
	# rotate the vector to make it match the robot's heading
	position_vector = self.rotateVector2D(position_vector , self.angle)


	# account for the different dimention of the kinect grid and the occupancy grid we use
	occupancy_grid_units_per_kinect_units = kinect_grid_size / self.map_resolution
	position_vector[0] = 	int (  position_vector[0] * occupancy_grid_units_per_kinect_units   )
	position_vector[1] = 	int (  position_vector[1] * occupancy_grid_units_per_kinect_units   )

	# add the global position of the robot
	position_vector[0] += int( self.map_width/2  + (self.x_position * 100 )/  (self.map_resolution)  )  # the position is in meters
	position_vector[1] += int( self.map_height/2 + (self.y_position * 100 )/  (self.map_resolution)  )
	#print "before addedCoordinates" , [position_vector[0],position_vector[1]]
	#

	#round down to the lower even number if not even 
	
	#if(position_vector[0] % 2 !=0):
	#	position_vector[0]-=1
	#if(position_vector[1] % 2 !=0):
	#	position_vector[1]-=1
	
	# round it down to the next multiple of occupancy_grid_units_per_kinect_units  for the average filter
	position_vector[0]-= int( position_vector[0] % occupancy_grid_units_per_kinect_units )
	position_vector[1]-= int( position_vector[1] % occupancy_grid_units_per_kinect_units )

	if ((position_vector[0],position_vector[1]) not in self.obstacle_list):
        	#self.obstacle_list.append([position_vector[0],position_vector[1]])

		self.obstacle_list[(position_vector[0],position_vector[1])] = [val,1]  # [cost value , number of readings there]
	
	#update the average cost value of the location
	else:
		#update the average cost value of the location
		location = self.obstacle_list[(position_vector[0],position_vector[1])]
		location[0] = int(((location[0]+0.0)*(location[1]+0.0) )/((location[1]+1.0)) + (val+0.0)/(location[1]+1.0))
		location[1] +=1
	print "addedCoordinates" , [position_vector[0], position_vector[1]]
	# *****
	# *****	We will later need to adjust for the fact that the kinect is not necessarily placed
	# ***** at the same place as what is considered to be the robot's centre.
	# ***** For example, it my be 25 cm at the back. We would then need to remove 50 to the position_vector[1]
	# *****



    #Rotate a coordinate ector
    def rotateVector2D(self, vector, angle):
        rotated_vect = []
        rotated_vect.append(  vector[0]*math.cos(angle)  - vector[1]*math.sin(angle)             )
        rotated_vect.append(  vector[0]*math.sin(angle)  + vector[1]*math.cos(angle)   )
        return rotated_vect


if __name__ == "__main__":
    try:
        builder = mapBuilder()
        builder.run()


    except KeyboardInterrupt:
        sys.exit(0)
