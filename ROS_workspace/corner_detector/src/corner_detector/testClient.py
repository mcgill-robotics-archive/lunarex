#IMPORTS
import rosbag
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Int8
import numpy as np
import roslib.message
import math
import struct
import geometry_msgs.msg
import nav_msgs.msg
import std_msgs.msg
from pylab import *
import matplotlib.gridspec as gridspec

#BAG SETUP
bag = rosbag.Bag('/home/ernie/Dropbox/LunarEx2012-2013/Software Team/ROS/Bags/localization_feb10.bag')
##DO NOT USE THIS BAG. IT SUCKS. bag = rosbag.Bag('/home/ernie/Dropbox/LunarEx2012-2013/Software Team/ROS/Bags/2013-03-19-14-26-50.bag') #shitty

#DO NOT USE THIS BAG. IT SUCKS. bag = rosbag.Bag('/home/ernie/Dropbox/LunarEx2012-2013/Software Team/ROS/Bags/2013-03-19-14-21-47.bag') #shitty

#bag = rosbag.Bag('/home/ernie/Dropbox/LunarEx2012-2013/Software Team/ROS/Bags/2013-02-20-21-37-14.bag') # awesome stage bag
#bag = rosbag.Bag('/home/ernie/Dropbox/LunarEx2012-2013/Software Team/ROS/Bags/2013-03-19-14-19-48.bag')

