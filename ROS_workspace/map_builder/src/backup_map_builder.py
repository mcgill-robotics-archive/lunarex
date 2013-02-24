#!/usr/bin/env python
import roslib; roslib.load_manifest('map_builder')
import rospy
from std_msgs.msg import *
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped
from numpy import *
import math

class mapBuilder:
    def __init__(self):
        rospy.init_node("map_builder")
        rospy.Subscriber("map", OccupancyGrid, self.mapCallback)   #subscribe to "/map" to get map from hector_mapping
        rospy.Subscriber("slam_out_pose", PoseStamped, self.poseCallback)   #get the position of the robot
        self.pub = rospy.Publisher("global_map", OccupancyGrid)
        self.obstacle_list = [[2,2],[20,20],[50,50]]
        self.map = None
        self.occupancy_grid = []

    def run(self):
        rospy.spin()

    def mapCallback(self, grid):
        self.map = grid
        self.occupancy_grid = [grid.data[i] for i in range(len(grid.data))]
        self.getMapParameters()
        # Add kinect obstacles to occupancy list
        # assuming obstacle_list are in occupancyGrid coordinates
        for obstacle in self.obstacle_list:
            self.insertValueInOccupancyGrid(obstacle[0], obstacle[1], 100)
        self.map.data = self.occupancy_grid #Change the occupancy grid to the updated one
        self.pub.publish(self.map)

    #Retrieve position data
    def poseCallback(self, pose):
        self.position = pose
        self.x_position = self.position.pose.position.x
        self.y_position = self.position.pose.position.y
        print "Current position:"
        print self.x_position
        print self.y_position
        print self.position.pose.orientation
        w = self.position.pose.orientation.w
        z = self.position.pose.orientation.z
        print math.copysign(2 * math.acos(w) * 180 / math.pi, z)    #True angle calculated using quaternion

    def addCoordinates(x, y):
        self.obstacle_list.append([x,y])

    #Rotate a coordinate ector
    def rotateVector2D(vector, angle):
        rotated_vect = []
        rotated_vect.append( vector[0]*math.cos(angle) - math.sin(angle) )
        rotated_vect.append( vector[1]*math.sin(angle)  + vector[1]*math.cos(angle) )
        return rotated_vect

    def getMapParameters(self):
        self.map_height = self.map.info.height  #the height of occupancy gird
        self.map_width = self.map.info.width    #the width of occupancy grid
        self.map_resolution = self.map.info.resolution

    def processMap(self):
        pass    #implent later

    def insertValueInOccupancyGrid(self, x_coord, y_coord, val):
        square_size = 6
        for i in range(square_size):
            for ii in range(square_size):
                
                self.occupancy_grid[(y_coord -3+i) * self.map_width + (x_coord -3+ii)] = val

if __name__ == "__main__":
    try:
        builder = mapBuilder()
        builder.run()
    except KeyboardInterrupt:
        sys.exit(0)
