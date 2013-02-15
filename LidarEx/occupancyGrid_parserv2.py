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
bag = rosbag.Bag('localization_feb10.bag')

#RETRIEVING MAP META DATA
mapWidth=0
mapHeight=0 
mapRes = 0 #the length of each cell
for topic, msg, t in bag.read_messages(topics=['/map_metadata']):
	mapWidth = msg.width
	mapHeight=msg.height
	mapRes = msg.resolution
	break

print("META: map width = "+str(mapWidth)+" height=" +str(mapHeight)+" and res= "+str(mapRes) )


#COLLECTING OCCUPANCY GRID
occupancyGrid = np.empty((mapWidth,mapHeight),dtype='int')
gridData = []
msg = OccupancyGrid()
for topic, msg, t in bag.read_messages(topics=['/map']):
	gridData = msg.data

occupancyGrid = np.reshape(gridData,(1024,1024))

#DEFINING HOUGH MATRIX
Rres = mapRes #r bucket resolution
Rrank = (int)(math.sqrt(2)*max(mapWidth, mapHeight)/Rres) #nb of R buckets
Tres = 1
Trank = 180/1

H = [[0 for T in xrange(Trank)] for R in xrange(Rrank)] 

#PLACING POINTS INTO THE MATRIX
for i in range(0,len(occupancyGrid)):
	for j in range(0,len(occupancyGrid[i])):
		if(occupancyGrid[i][j]==100):
			for t in range(0, Trank):	
				pointR = i*mapRes*math.cos(math.radians(t)) + j*mapRes*math.sin(math.radians(t))
				#print(i, j, t, pointR)
				H[int(pointR/Rres)][t]+=1
				
Harray = np.asarray(H)
#a,b = np.unravel_index(Harray.argmax(), Harray.shape)			
#print(a, b)	

#print Harray.argsort()[-4:][::-1]
print(Sorted(H[0][]
				
