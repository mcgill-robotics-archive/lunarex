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
ARENA_WIDTH = 3.88
ARENA_HEIGHT = 7.38

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

def findCorners(req):
	
	rospy.loginfo("dealing with request")

	startingTime = rospy.get_time()
	#MAP META. ***IMPORTANT NOTE*** the map meta data is also available in /map topic. Check which is best.
	mapWidth = req.map_meta.width
	mapHeight=req.map_meta.height
	mapRes = req.map_meta.resolution
	
	rospy.loginfo("META: map width = "+str(mapWidth)+" height=" +str(mapHeight)+" and res= "+str(mapRes))
	
	#GRID 
	gridData = req.map.data

	#COLLECTING OCCUPANCY GRID
	occupancyGrid = np.empty((mapWidth,mapHeight),dtype='int')
	occupancyGrid = np.reshape(gridData,(mapWidth,mapHeight), order='F') #C is row major order; F is col major
	
	#DEFINING HOUGH MATRIX
	Rres = mapRes #CHANGE BACK TO mapRes/4 ONCE SERVICE IS WRITTEN
	 #r bucket resolution. Doesn't make sense to have r buckets smaller than map res.
	Rrank = int((math.sqrt(2)*max(mapWidth, mapHeight))/Rres) #nb of R buckets
	Tres = 1
	Trank = 360#360/1#90/1#180/1

	print ("***Hough matrix has***")
	print(str(Rrank) +" R buckets of size: "+str(Rres))
	print("and : "+str(Trank) +" theta buckets of size: " +str(Tres))

	H = [[0 for T in xrange(Trank)] for R in xrange(Rrank)] 


	rospy.loginfo("Started placing points into the matrix")

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

	rospy.loginfo("Started placing hough matrix lines into Line objects")

	#PLACING HOUGH MATRIX LINES INTO LINE OBJECTS
	lines=[]
	for r in xrange(Rrank):
		for t in xrange(Trank):
			if(H[r][t]!=0 and len(H[r][t].points)>0):
				lines.append(H[r][t])

	rospy.loginfo("sort & print best lines")
	sortedLines = sorted(lines, key=lambda l: len(l.points), reverse=True)
	for l in sortedLines[:15]:
		print l
		
	#DEFINE WALLS AND WALL BUCKETS
	walls=[0,0,0,0] 
	walls[0]=sortedLines[0] #assume most populous line is first wall
		
	rospy.loginfo("fill walls & wall buckets")	

	#FILL WALLS & WALL BUCKETS
	wallIndex=1 #next wall to fill
	for l in sortedLines[:15]: #order of decreasing points/line
		if(walls[wallIndex%4]==0):#not filled
			sameBucket=False
			for w in walls:
				if(w!=0 and sameBuckets(l, w)==True):#not the same bucket as any current wall
					sameBucket=True
			if(sameBucket==False):
				walls[wallIndex]=l
				wallIndex+=1	

	rospy.loginfo("Making sure that the best 4 walls are LONG - LONG - SHORT - SHORT")

	rospy.loginfo("done getting walls. Right now we have:")
	for i in range(0,4):
		print ("WALL "+str(i)+": "+str(walls[i])) 

	bestWallsDistance = abs(walls[0].r -  walls[1].r) 
	if(bestWallsDistance < 1.2*ARENA_HEIGHT and bestWallsDistance > 0.8*ARENA_HEIGHT):
		print("best walls are SHORT. Switch walls 0&1 with 2&3")
		temp1 = walls[2]
		temp2 = walls[3]
		walls[2] = walls[0]
		walls[3] = walls[1]
		walls[0]=temp1
		walls[1]=temp2

	elif(not(bestWallsDistance < 1.2*ARENA_WIDTH and bestWallsDistance > 0.8*ARENA_WIDTH)):
		rospy.loginfo("the best walls are not LONG LONG (nor SHORT SHORT) ")
		
		middleWallsDistance = abs(walls[1].r - walls[2].r)
		if(middleWallsDistance < 1.2*ARENA_WIDTH and middleWallsDistance > 0.8*ARENA_WIDTH):
			rospy.loginfo("two middle ones are long. so we have short - long - long - short")
			rospy.loginfo("switching wall 0 with wall 2")
			temp1 = walls[2]
			walls[2] = walls[0]
			walls[0]=temp1
		elif(middleWallsDistance < 1.2*ARENA_HEIGHT and middleWallsDistance > 0.8*ARENA_HEIGHT):
			rospy.loginfo("two middle ones are short. so we have long - short - short - long")
			rospy.loginfo("switching wall 3 with wall 1")
			temp1 = walls[3]
			walls[3]=walls[1]
			walls[1] = temp1
		else:
			rospy.loginfo("two middle ones are short-long or long-short")
			rospy.loginfo("switching the two middle walls - wall1 and wall2")
			temp1 = walls[2]
			walls[2] = walls[1]
			walls[1]=temp1

			rospy.loginfo("now can either be short-short-long-long or long-long-short-short")
			if(bestWallsDistance < 1.2*ARENA_HEIGHT and bestWallsDistance > 0.8*ARENA_HEIGHT):
				print("best walls are SHORT. Switch walls 0&1 with 2&3")
				temp1 = walls[2]
				temp2 = walls[3]
				walls[2] = walls[0]
				walls[3] = walls[1]
				walls[0]=temp1
				walls[1]=temp2

	rospy.loginfo("done getting walls. Now get corners")
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
	
	axis([-100, mapWidth, -100, mapHeight])
	areaPos = pi*(2)**2 # radius of dots
	areaPos2 = pi**2 # radius of dots
	areaP = pi*(10)**2 # radius of dots
	xlabel('cells',fontdict={'fontsize':20})

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

	# corners is an Array of corner Tuples: (name, X, Y, distance)
	# Populate array with corner tuples
	corners = [('Corner 0', cornersX[0], cornersY[0], math.sqrt(((cornersX[0]-mapWidth/2)**2 + (cornersY[0]-mapHeight/2)**2))),
	('Corner 1', cornersX[1], cornersY[1], math.sqrt(((cornersX[1]-mapWidth/2)**2 + (cornersY[1]-mapHeight/2)**2))), ('Corner 2', cornersX[2], cornersY[2], math.sqrt(((cornersX[2]-mapWidth/2)**2 + (cornersY[2]-mapHeight/2)**2))),('Corner 3', cornersX[3], cornersY[3], math.sqrt(((cornersX[3]-mapWidth/2)**2 + (cornersY[3]-mapHeight/2)**2)))]

	# sort array by distance
	corners.sort(key=lambda corner: corner[3])

	print(corners)

	# Initialize corners
	error = ('error', 0, 0, 0)
	left_bottom_corner = error
	right_bottom_corner = error
	left_top_corner = error
	right_top_corner = error

	vector01 = array([corners[1][1] - corners[0][1], corners[1][2] - corners[0][2]])
	vector02 = array([corners[2][1] - corners[0][1], corners[2][2] - corners[0][2]])
	vector03 = array([corners[3][1] - corners[0][1], corners[3][2] - corners[0][2]])
	
	print(vector01)
	print(vector02)
 	print(vector03)

	if(0 < cross(vector01,vector02)):
		print('Starting on the left')
		left_bottom_corner = corners[0]
		right_bottom_corner = corners[1]
		left_top_corner = corners[2]
		right_top_corner = corners[3]

	else:
		print('Starting on the right')
		left_bottom_corner = corners[1]
		right_bottom_corner = corners[0]
		left_top_corner = corners[3]
		right_top_corner = corners[2]	
		
	'''

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

	'''

	response = corner_detectorResponse()
	response.left_bottom_corner = [int(left_bottom_corner[1]), int(left_bottom_corner[2])]
	response.right_bottom_corner = [int(right_bottom_corner[1]), int(right_bottom_corner[2])]
	response.left_top_corner = [int(left_top_corner[1]), int(left_top_corner[2])]
	response.right_top_corner = [int(right_top_corner[1]), int(right_top_corner[2])]

	print('Tuple: (Name, X, Y, Distance)')
	print('Top left corner: ' + str(left_top_corner))
	print('Top right corner: ' + str(right_top_corner))
	print('Bottom left corner: ' + str(left_bottom_corner))
	print('Bottom right corner: ' + str(right_bottom_corner))

	
	grid(True)
	scatter(x,y,s=areaPos2, marker='.', c='c', edgecolors ='none')
	scatter(mapWidth/2,mapHeight/2,s=areaP, marker='.', c='k', edgecolors ='none')
	scatter(x1,y1,s=areaP, marker='.', c='y', edgecolors ='none')
	scatter(x2,y2,s=areaP, marker='.', c='b', edgecolors ='none')
	scatter(x3,y3,s=areaP, marker='.', c='g', edgecolors ='none')
	scatter(x4,y4,s=areaP, marker='.', c='r', edgecolors ='none')

	scatter(x,y,s=areaPos, marker='.', c='c', edgecolors ='none')
	scatter(xWalls,yWalls,s=areaPos, marker='.', c='b', edgecolors ='none')

	show()
	
	endTime = rospy.get_time()
	print ("Time taken: " +str(endTime - startingTime))
	return response
	
rospy.init_node('corner_detector')
s = rospy.Service('corner_detector_srv', corner_detector, findCorners)
print "Ready to find some corners."
rospy.spin()
