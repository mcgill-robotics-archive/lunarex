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

class Line(object):
	
	def __init__(self, r, theta):
		self.theta = float(theta)
		self.r = float(r)  
		self.points = []
		
	def __str__(self):
		s = "Line has " + str(len(self.points)) + " points at distance r= " + str(self.r) + " with angle theta = " + str(self.theta)
		return s
		
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

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
Rrank = (int)(math.sqrt(2)*max(mapWidth, mapHeight))#/Rres) #nb of R buckets
Tres = 1
Trank = 360#360/1#90/1#180/1

H = [[0 for T in xrange(Trank)] for R in xrange(Rrank)] 

#PLACING POINTS INTO THE MATRIX
for i in range(0,len(occupancyGrid)):
	for j in range(0,len(occupancyGrid[i])):
		if(occupancyGrid[i][j]==100):
			for t in range(0, Trank):	
				lineR = i*mapRes*math.cos(math.radians(t)) + j*mapRes*math.sin(math.radians(t))
				if(lineR<0):
					t+=180
					t=t%360
					lineR=abs(lineR)
				if(H[int(lineR/Rres)][t])==0:
					H[int(lineR/Rres)][t]=Line(lineR, t)
				H[int(lineR/Rres)][t].points.append(Point(i,j))

lines=[]
for r in xrange(Rrank):
	for t in xrange(Trank):
		if(H[r][t]!=0 and len(H[r][t].points)>0):
			lines.append(H[r][t])

walls=[0,0,0,0]

sortedLines = sorted(lines, key=lambda l: len(l.points), reverse=True)
for l in sortedLines[:30]:
	print l
	
walls[0]=sortedLines[0] #the first wall
angles = [0,0,0,0]
angles[0]= walls[0].theta
angles[1]=(angles[0] + 90)%360
angles[2] = (angles[0] + 180)%360
angles[3] = (angles[0] + 270)%360
thresh = 2

wrapIndex = -1
for i in range(0, len(angles)):
	if(angles[i]>360-thresh or angles[i]<thresh):
		wrapIndex=i

#print wrapIndex
#for a in angles:
#	print a
for l in sortedLines:
	for i in range(0, 4):
		if(walls[i]==0): #wall not set yet
			if((i==wrapIndex and (l.theta<thresh or l.theta>360-thresh)) or (i!=wrapIndex and l.theta>angles[i]-thresh and l.theta<angles[i]+thresh)):
				walls[i]=l
	if(walls[1]!=0 and walls[2]!=0 and walls[3]!=0):
		break

for i in range(0,4):
	print ("WALL "+str(i)+": "+str(walls[i])) 

	
sortedWalls = sorted(walls, key=lambda w: w.r, reverse=True)

#for w in sortedWalls:
#	print w
