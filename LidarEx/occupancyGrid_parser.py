import rosbag
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Int8
import numpy as np
import roslib.message
import struct
import geometry_msgs.msg
import nav_msgs.msg
import std_msgs.msg
from pylab import *
import matplotlib.gridspec as gridspec

bag = rosbag.Bag('localization_feb10.bag')
mapSize=1024
occupancyGrid = np.empty((1024,1024),dtype='int')
gridData = []
msg = OccupancyGrid()

for topic, msg, t in bag.read_messages(topics=['/map']):
	gridData = msg.data

occupancyGrid = np.reshape(gridData,(1024,1024))

topCorner = [0,0] 
bottomCorner = [0,0]
leftCorner = [0,0]
rightCorner = [0,0]

minj = 1024
maxj = 0

x = []
y = []
count = 0

for i in range(0,len(occupancyGrid)):
	for j in range(0,len(occupancyGrid[i])):
		if(occupancyGrid[i][j] == 100):
			count +=1
			x.append(i)
			y.append(j)
			print(i, j)
		if(occupancyGrid[i][j] == 100 and topCorner[0] == 0):
			topCorner[0] = i
			topCorner[1] = j
		if(occupancyGrid[i][j] == 100):
			bottomCorner[0] = i
			bottomCorner[1] = j
		if(occupancyGrid[i][j] == 100 and j > maxj):
			maxj = j
			rightCorner[0] = i
			rightCorner[1] = j
		if(occupancyGrid[i][j] == 100 and j < minj):
			minj = j
			leftCorner[0] = i
			leftCorner[1] = j
		
print 'Top Corner is    ' + str(topCorner)
print 'Bottom Corner is ' + str(bottomCorner)
print 'Left Corner is   ' + str(leftCorner)
print 'Right Corner is  ' + str(rightCorner)

bag.close()

gs = gridspec.GridSpec(1, 1, width_ratios=[1,1], height_ratios=[1,1])

subplot(gs[0])    
axis([0, 1024, 0, 1024])
areaPos = pi*(2)**2 # radius of dots
xlabel('cells',fontdict={'fontsize':20})



grid(True)
scatter(x,y,s=areaPos, marker='.', c='y', edgecolors ='none')
#scatter(topCorner[0],topCorner[1],s=areaPos, marker='.', c='y', edgecolors ='none')
#scatter(bottomCorner[0],bottomCorner[1],s=areaPos, marker='.', c='b', edgecolors ='none')
#scatter(leftCorner[0],leftCorner[1],s=areaPos, marker='.', c='g', edgecolors ='none')
#scatter(rightCorner[0],rightCorner[1],s=areaPos, marker='.', c='r', edgecolors ='none')
show()


