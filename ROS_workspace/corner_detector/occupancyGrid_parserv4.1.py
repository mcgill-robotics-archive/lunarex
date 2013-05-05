#!/usr/bin/env python

#IMPORTS
import rosbag
import nav_msgs.msg
import std_msgs.msg
import numpy as np
import roslib.message
import math
import struct
import geometry_msgs.msg
import nav_msgs.msg
import std_msgs.msg
from pylab import *
import matplotlib.gridspec as gridspec

import rospy
import roslib; roslib.load_manifest('corner_detector')
from corner_detector.srv import *

BIGNUMBER = 1000

tThresh = 5 #absolute: 2de
rThresh = 1.0 #absolute: 8% R difference between 2 walls max in 1 bucket


class Line(object):
	
	def __init__(self, r, theta):
		self.theta = float(theta)
		self.r = float(r)  
		
		#y=mx+b representation
		if(math.sin(math.radians(theta))==0):
			self.m = BIGNUMBER
			self.b=BIGNUMBER
		else:
			self.m = -(math.cos(math.radians(theta))/math.sin(math.radians(theta)))
			self.b = r/math.sin(math.radians(theta))
		self.points = []
		
	def __str__(self):
		s = "Line has " + str(len(self.points)) + " points at distance r= " + str(self.r) + " with angle theta = " + str(self.theta)
		return s
		
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

def sameRBucket(a, b): #are a & b within rThresh% of eachother?
	if((a==0 and b<rThresh and b>-rThresh) or (b==0 and a<rThresh and a>-rThresh)):
		 return True
	if(abs(b-a) < rThresh):
		return True
	return False


def sameTBucket(t1, t2): #are t1&t2 within tThresh of eachother?
	if(abs(t1-t2)<=tThresh):
		return True
	if(t1+360-t2 <= tThresh or t2+360-t1<=tThresh):
		return True
	return False	

def sameBuckets(l1, l2):
	return (sameRBucket(l1.r, l2.r) and sameTBucket(l1.theta, l2.theta))

#occupancyGrid = 0
#mapWidth=0
#mapHeight=0 
#mapRes = 0 #the length of each cell
#gridData=[]

def findCorners(req):
	
	print ("dealing with request")
	#MAP META. ***IMPORTANT NOTE*** the map meta data is also available in /map topic. Check which is best.
	mapWidth = req.map_meta.width
	mapHeight=req.map_meta.height
	mapRes = req.map_meta.resolution
	
	print("META: map width = "+str(mapWidth)+" height=" +str(mapHeight)+" and res= "+str(mapRes) )
	
	#GRID 
	gridData = req.map.data

	#COLLECTING OCCUPANCY GRID
	occupancyGrid = np.empty((mapWidth,mapHeight),dtype='int')
	occupancyGrid = np.reshape(gridData,(mapWidth,mapHeight))

	#DEFINING HOUGH MATRIX
	Rres = mapRes/4 #CHANGE BACK TO mapRes/4 ONCE SERVICE IS WRITTEN
	 #r bucket resolution. Doesn't make sense to have r buckets smaller than map res.
	Rrank = int((math.sqrt(2)*max(mapWidth, mapHeight))/Rres) #nb of R buckets
	Tres = 1
	Trank = 360#360/1#90/1#180/1


	print ("***Hough matrix has***")
	print(str(Rrank) +" R buckets of size: "+str(Rres))
	print("and : "+str(Trank) +" theta buckets of size: " +str(Tres))

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

	#PLACING HOUGH MATRIX LINES INTO LINE OBJECTS
	lines=[]
	for r in xrange(Rrank):
		for t in xrange(Trank):
			if(H[r][t]!=0 and len(H[r][t].points)>0):
				lines.append(H[r][t])

	#sort & print best lines
	sortedLines = sorted(lines, key=lambda l: len(l.points), reverse=True)
	for l in sortedLines[:30]:
		print l
		
	#DEFINE WALLS AND WALL BUCKETS
	walls=[0,0,0,0] 
	wallBuckets=[[] for i in range(0,4)]
	walls[0]=sortedLines[0] #assume most populous line is first wall
		
	#FILL WALLS & WALL BUCKETS
	wallIndex=1 #next wall to fill
	for l in sortedLines: #order of decreasing points/line
		if(walls[wallIndex%4]==0):#not filled
			sameBucket=False
			for w in walls:
				if(w!=0 and sameBuckets(l, w)==True):#not the same bucket as any current wall
					sameBucket=True
			if(sameBucket==False):
				walls[wallIndex]=l

				wallIndex+=1	
		for i in range(0,4):
			if(walls[i]!=0 and sameBuckets(l, walls[i])):
				wallBuckets[i].append(l)						
					
	for i in range(0,4):
		print ("WALL "+str(i)+": "+str(walls[i])) 

	y1 = (walls[2].r*sin(math.radians(walls[2].theta)) + walls[1].r*sin(math.radians(walls[1].theta)))/mapRes
	x1 = (walls[2].r*cos(math.radians(walls[2].theta)) + walls[1].r*cos(math.radians(walls[1].theta)))/mapRes

	y2 = (walls[1].r*sin(math.radians(walls[1].theta)) + walls[3].r*sin(math.radians(walls[3].theta)))/mapRes
	x2 = (walls[1].r*cos(math.radians(walls[1].theta)) + walls[3].r*cos(math.radians(walls[3].theta)))/mapRes

	y3 = (walls[2].r*sin(math.radians(walls[2].theta)) + walls[0].r*sin(math.radians(walls[0].theta)))/mapRes
	x3 = (walls[2].r*cos(math.radians(walls[2].theta)) + walls[0].r*cos(math.radians(walls[0].theta)))/mapRes

	y4 = (walls[0].r*sin(math.radians(walls[0].theta)) + walls[3].r*sin(math.radians(walls[3].theta)))/mapRes
	x4 = (walls[0].r*cos(math.radians(walls[0].theta)) + walls[3].r*cos(math.radians(walls[3].theta)))/mapRes
	 
	print ("Corner 1: x: " + str(x1) + ", y:" + str(y1) + " => Yellow ")  
	print ("Corner 2: x: " + str(x2) + ", y:" + str(y2) + " => Blue")  
	print ("Corner 3: x: " + str(x3) + ", y:" + str(y3) + " => Green")  
	print ("Corner 4: x: " + str(x4) + ", y:" + str(y4) + " => Red")  

	cornersX = []
	cornersY = []
	
	cornersX.append(x1)
	cornersY.append(y1)
	cornersX.append(x2)
	cornersY.append(y2)
	cornersX.append(x3)
	cornersY.append(y3)
	cornersX.append(x4)
	cornersY.append(y4)
	
	# PLOT THE OCCUPANCY GRID AND CORNERS
	xWalls = []
	yWalls = []
	x = []
	y = []

	# Populate xWalls and yWalls with all the points on the 4 most populated lines
	for j in range(0,4):
		for i in range(0,len(walls[j].points)):
			xWalls.append(walls[j].points[i].x)
			yWalls.append(walls[j].points[i].y)

			
	for i in range(0,len(occupancyGrid)):
		for j in range(0,len(occupancyGrid[i])):
			if(occupancyGrid[i][j] == 100):
				x.append(i)
				y.append(j)

	# Array of corner Tuple: (name, X, Y, distance)
	# Populate array with corner tuples
	corners = [('Corner 1', cornersX[0], cornersY[0], math.sqrt(((cornersX[0]-mapWidth/2)**2 + (cornersY[0]-mapHeight/2)**2))),
	('Corner 2', cornersX[1], cornersY[1], math.sqrt(((cornersX[1]-mapWidth/2)**2 + (cornersY[1]-mapHeight/2)**2))), ('Corner 3', cornersX[2], cornersY[2], math.sqrt(((cornersX[2]-mapWidth/2)**2 + (cornersY[2]-mapHeight/2)**2))),('Corner 4', cornersX[3], cornersY[3], math.sqrt(((cornersX[3]-mapWidth/2)**2 + (cornersY[3]-mapHeight/2)**2)))]

	# sort array by distance
	corners.sort(key=lambda corner: corner[3])

	# Initialize corners
	error = ('error', 0, 0, 0)
	left_bottom_corner = error
	right_bottom_corner = error
	left_top_corner = error
	right_top_corner = error

	# X axis difference between corner 4 and 1
	cornerDiffX = corners[3][1] - corners[0][1]
	# Y axis difference between corner 4 and 1
	cornerDiffY = corners[3][2] - corners[0][2]

	# left corner if difference of X/Y coords of furthest corner and closest corner are SAME sign
	if(((cornerDiffX >= 0) and (cornerDiffY >= 0)) or ((cornerDiffX <= 0) and (cornerDiffY <= 0))):
		print('Starting on the left')
		left_bottom_corner = corners[0]
		right_bottom_corner = corners[1]
		left_top_corner = corners[2]
		right_top_corner = corners[3]

	# right corner if difference of X/Y coords of furthest corner and closest corner are DIFFERENT sign
	if(((cornerDiffX <= 0) and (cornerDiffY >= 0)) or ((cornerDiffX >= 0) and (cornerDiffY <= 0))):
		print('Starting on the right')
		left_bottom_corner = corners[1]
		right_bottom_corner = corners[0]
		left_top_corner = corners[3]
		right_top_corner = corners[2]

	response = corner_detectorResponse()
	response.left_bottom_corner = [int(left_bottom_corner[1]), int(left_bottom_corner[2])]
	response.right_bottom_corner = [int(right_bottom_corner[1]), int(right_bottom_corner[2])]
	response.left_top_corner = [int(left_top_corner[1]), int(left_top_corner[2])]
	response.right_top_corner = [int(right_top_corner[1]), int(right_top_corner[2])]

	return response
	
rospy.init_node('corner_detector')
s = rospy.Service('corner_detector_srv', corner_detector, findCorners)
print "Ready to find some corners."
rospy.spin()
