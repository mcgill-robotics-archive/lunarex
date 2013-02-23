#!/usr/bin/env python
'''
The convention in Python is to describe what this module (program) does here.
'''


import roslib; roslib.load_manifest('') #add directory
import rospy
for sensor_msgs import image		#What does this do? - Nick
import numpy as np

def depthMatrixReshape(depthValues):
    '''
    The convention in Python is to describe how a method works here.
    '''
    
    x = depthValues.step
    y = depthValues.row
    depthArray = [[for i in range(x)] for j in range(y)]
	depthArray = np.reshape(depthValues.data, (x, y))
	 


rospy.init_node('depthListener', anonymous=True)
rospy.Subscriber('depth/image_raw', image, depthMatrixReshape)
rospy.spin()


# A Couple Notes by Nick
#Can you please rename this module to something more specific?
#make sure you use consistent indentation in python
#please add comments to clarify how this module works.