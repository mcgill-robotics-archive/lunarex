#!/usr/bin/env python
import roslib; roslib.load_manifest('map_builder')
import rospy
from std_msgs.msg import *
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import PoseStamped
from numpy import *

class mapBuilder:
    def __init__(self):
        rospy.init_node("map_builder")
        rospy.Subscriber("map", OccupancyGrid, self.mapCallback)   #subscribe to "/map" to get map from hector_mapping
        rospy.Subscriber("slam_out_pose", PoseStamped, self.poseCallback)   #get the position of the robot
        self.pub = rospy.Publisher("global_map", OccupancyGrid)
        self.obstacle_list = [[2,2],[20,20],[50,50]]
        self.map = None

    def run(self):
        rospy.spin()

    def mapCallback(self, grid):
        self.map = grid
        #self.new_map = self.map
        self.getMapParameters()
        self.pub.publish(self.map)
        
    #Retrieve position data
    def poseCallback(self, pose):
        self.position = pose
        self.x_position = self.position.pose.position.x
        self.y_position = self.position.pose.position.y
        print "Current position:" 
        print self.x_position
        print self.y_position

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
        self.map.data[]
    
if __name__ == "__main__":
    try:
        builder = mapBuilder()
        builder.run()
    except KeyboardInterrupt:
        sys.exit(0)
