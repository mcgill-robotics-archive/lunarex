#!/usr/bin/env python
import roslib; roslib.load_manifest('map_builder')
import rospy
import std_msgs
import nav_msgs

class mapBuilder:
    def __init__(self):
        rospy.init_node("map_builder")
        rospy.subsriber("map", nav_msgs.OccupancyGrid, self.callback)   #subscribe to "/map" to get map from hector_mapping
        self.pub = rospy.publisher("global_map", nav_msgs.OccupancyGrid)
        self.obstacle_list = []
        self.lidar_map = None
        self.new_map = None
        
    def run(self):
        rospy.spin()
        
    def callback(self, grid):
        self.lidar_map = grid
        self.new_map = self.lidar_map
        pub.publish(self.new_map)
        
    def addCoordinates(x, y):
        self.obstacle_list.append([x,y])
        
    def rotateVector2D(vector, angle):
        rotated_vect = []
        rotated_vect.append( vector[0]*math.cos(angle) - math.sin(angle) )
        rotated_vect.append( vector[1]*math.sin(angle)  + vector[1]*math.cos(angle) )
        return rotated_vect
        
if __name__ == "__main__":
    try:
        builder = mapBuilder()
        builder.run()
    except KeyboardInterrupt:
        sys.exit(0)