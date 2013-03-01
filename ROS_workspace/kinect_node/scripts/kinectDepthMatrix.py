#!/usr/bin/env python
'''
The convention in Python is to describe what this module (program) does here.
'''


import roslib; roslib.load_manifest('ros_node') #add directory
import rospy
from sensor_msgs.msg import Image		#takes image from sensor_imgs module
import numpy as np

import pprint

pp = pprint.PrettyPrinter(indent=4)


def depthMatrixReshape(msg):
    '''
    Takes X (step) and Y (row) values and shapes the 1D depth values into a 2D depth array
    '''
    rowRank = msg.height
    columnRank = msg.width
    print columnRank, rowRank
    array_sum = 0
    array_dim = 0
    #depthArray = [[0 for j in range(columnRank)] for i in range(rowRank)]
    depthArray = np.empty((rowRank, columnRank),dtype = "object")

    for i in xrange(rowRank):
        for j in xrange(columnRank):
            depthArray[i][j]=msg.data[i*columnRank+j]

    for i in xrange(rowRank):
       for j in xrange(columnRank):
            depthArray[i][j] =  int(ord(depthArray[i][j]))
	    array_sum += int(1000/(-0.0030711016 * depthArray[i][j] + 3.3309495161))
	    array_dim += 1

    #print depthArray
    print "Average: %d" % (array_sum / array_dim)


rospy.init_node('depthListener', anonymous=True)
rospy.Subscriber('/camera/depth/image_raw', Image, depthMatrixReshape)
rospy.spin()



# A Couple Notes by Nick
#Can you please rename this module to something more specific?
#make sure you use consistent indentation in python
#please add comments to clarify how this module works.
