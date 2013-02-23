#!/usr/bin/env python
'''
The convention in Python is to describe what this module (program) does here.
'''


import roslib; roslib.load_manifest('ros_node') #add directory
import rospy
from sensor_msgs.msg import Image		#takes image from sensor_imgs module
import numpy as np

def depthMatrixReshape(depthValues):
    '''
    Takes X (step) and Y (row) values and shapes the 1D depth values into a 2D depth array
    '''

    x = depthValues.step
    y = depthValues.row
    depthArray = [[0]*x]*y
    depthArray = np.reshape(depthValues.data, (x, y))
    print depthArray


rospy.init_node('depthListener', anonymous=True)
rospy.Subscriber('depth/image_raw', Image, depthMatrixReshape)
rospy.spin()


# A Couple Notes by Nick
#Can you please rename this module to something more specific?
#make sure you use consistent indentation in python
#please add comments to clarify how this module works.
