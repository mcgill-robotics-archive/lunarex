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
	self.header = header()
	self.info = info()
	self.initGrid()

    def initGrid(self):
	self.occupancy_grid = []
	i = 0
	for i in range(398 * 798):
	    self.occupancy_grid.append(0)
	self.info.resolution = 0.01
	self.info.width = 398
	self.info.height = 798
	self.header.frame_id = "/map"

    def run(self):
	frequency = rospy.Rate(10)
	while not rospy.is_shutdown():
	    self.initGrid()
	    self.pub.publish(self.header, self.info, self.occupancy_grid)
	    self.update()
	    print "Occupancy Grid sent"
	    frequency.sleep()

    def update(self):
	self.header.stamp = rospy.get_rostime()

class header:
    def __init__(self):
	self.seq = 123467
	self.stamp = rospy.get_rostime
	self.frame_id = ""

class info:
    def __init__(self):
	self.map_load_time = rospy.get_rostime() 
	self.resolution = 0.0
	self.width = 0
	self.height = 0
	self.origin = origin()

class origin:
    def __init__(self):
	self.position = position()
	self.orientation = orientation()

class position:
    def __init__(self):
	self.x = 0
	self.y = 0
	self.z = 0

class orientation:
    def __init__(self):
	self.x = 0
	self.y = 0
	self.z = 0
	self.w = 1


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
