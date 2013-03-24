#!/usr/bin/env python
import roslib; roslib.load_manifest('map_builder')
import rospy
from nav_msgs.msg import OccupancyGrid
import sys

class mapPublisher:
    def __init__(self):
	rospy.init_node("map_publisher")
	#print "Node initiated"
	self.pub = rospy.Publisher("map", OccupancyGrid)
	#print "publisher created"
	self.initGrid()

    def initGrid(self):
	self.occupancy_grid = []
	i = 0
	for i in range(398 * 798):
	    self.occupancy_grid.append(0)

    def run(self):
	#frequency = rospy.Rate(10)
	while not rospy.is_shutdown():
	    self.initGrid()
	    self.pub.publish(self.occupancy_grid)
	    print "Occupancy Grid sent"
	    #frequency.sleep()


if __name__ == '__main__':
    print "Program Started"
    try:
	mapPub = mapPublisher()
	#print "Object created"
	mapPub.run()
	print "shutDown!"
	print rospy.is_shutdown()
    except KeyboardInterrupt:
	sys.exit(0)
