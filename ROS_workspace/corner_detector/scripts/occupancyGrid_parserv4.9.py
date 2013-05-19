#!/usr/bin/env python

#IMPORTS
import numpy as np
import math
import geometry_msgs.msg
from pylab import *
import time
import threading

import rospy
import roslib; roslib.load_manifest('corner_detector')
from corner_detector.msg import Corners
from nav_msgs.msg import OccupancyGrid
from nav_msgs.msg import MapMetaData
import std_msgs.msg
from nav_msgs.srv import GetMap

#CONSTANTS
BIGNUMBER = 1000
ARENA_WIDTH = 3.88
ARENA_HEIGHT = 7.38
SLEEP_TIME_SECS = 30
NUMBER_OF_POTENTIAL_WALLS = 50

#bucket thresholds
tThresh = 5 #absolute: 2de
rThresh = 1.0 #absolute: 8% R difference between 2 walls max in 1 bucket

#TOPIC PUBLISHED
latest_corners = Corners()
latest_corners.LR_corner = [-1, -1]
latest_corners.RR_corner = [-1, -1]
latest_corners.LF_corner = [-1, -1]
latest_corners.RF_corner = [-1, -1]
latest_corners.resolution = -1
latest_corners.width = -1
latest_corners.height = -1
latest_corners.left = True 

#STATE VARS
latest_map = None
gridData = None
getNewMap = True
#CALLBACKS
	
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
	
rospy.init_node('corner_detector')

print("Started waiting for hector mapping map service")
rospy.wait_for_service('dynamic_map')
print("Done waiting for hector mapping map service")

cornersPub = rospy.Publisher("corners", Corners)

ranOnce = False

while(True):
	corner_detector_proxy = rospy.ServiceProxy('dynamic_map', GetMap)
	latest_map = corner_detector_proxy()
	gridData = latest_map.map.data
	latest_corners.width = latest_map.map.info.width
	latest_corners.height = latest_map.map.info.height
	latest_corners.resolution = latest_map.map.info.resolution
	print("Just started crunching a new map.")

	#COLLECTING OCCUPANCY GRID
	occupancyGrid = np.empty((latest_corners.width,latest_corners.height),dtype='int')
	occupancyGrid = np.reshape(gridData,(latest_corners.width,latest_corners.height), order='F') #C is row major order; F is col major
	
	#DEFINING HOUGH MATRIX
	mapRes = latest_corners.resolution
	# if( not ranOnce): 
	# 	Rres = mapRes*4
	# else:
	# 	Rres = mapRes

	Rres = mapRes*3

	mapWidth = latest_corners.width
	mapHeight = latest_corners.height
	Rrank = int((math.sqrt(2)*max(mapWidth, mapHeight))/Rres) #nb of R buckets
	Tres = 1
	Trank = 360

	print ("***Hough matrix has***")
	print(str(Rrank) +" R buckets of size: "+str(Rres))
	print("and : "+str(Trank) +" theta buckets of size: " +str(Tres))

	H = [[0 for T in xrange(Trank)] for R in xrange(Rrank)] 

	print("Started placing points into the matrix")

	pointCount = 0
	#PLACING POINTS INTO THE MATRIX
	for i in range(0,len(occupancyGrid)):
		for j in range(0,len(occupancyGrid[i])):
			if(occupancyGrid[i][j]==100):
				pointCount +=1
				for t in range(0, Trank):	
					lineR = i*mapRes*math.cos(math.radians(t)) + j*mapRes*math.sin(math.radians(t))
					if(lineR<0):
						t+=180
						t=t%360
						lineR=abs(lineR)
					if(H[int(lineR/Rres)][t])==0:
						H[int(lineR/Rres)][t]=Line(lineR, t)
					H[int(lineR/Rres)][t].points.append(Point(i,j))

	print("Started placing hough matrix lines into Line objects")

	#PLACING HOUGH MATRIX LINES INTO LINE OBJECTS
	lines=[]
	for r in xrange(Rrank):
		for t in xrange(Trank):
			if(H[r][t]!=0 and len(H[r][t].points)>0):
				lines.append(H[r][t])

	print("sort & print best lines")
	sortedLines = sorted(lines, key=lambda l: len(l.points), reverse=True)
		
	#DEFINE WALLS AND WALL BUCKETS
	walls=[sortedLines[0],sortedLines[1],sortedLines[2],sortedLines[3]] 
		
 	print("fill walls & wall buckets")

	bestTheta = BIGNUMBER
	wallDone = [True, False, False, False]
	for l in sortedLines[:NUMBER_OF_POTENTIAL_WALLS]: #order of decreasing points/line
 		if(not wallDone[1] and 
 			abs(l.theta - walls[0].theta) < 10 and abs(l.r-walls[0].r) > 3):
 			walls[1] = l
 			wallDone[1] = True
 		if(not wallDone[2] and 
 			(abs(l.theta - (walls[0].theta - 90)) < 10 or 
 				abs(l.theta - ((walls[0].theta + 90) % 360)) < 10)):
			wallDone[2]=True
 			walls[2]=l
 		if wallDone[2] and (not wallDone[3]) and (abs(l.theta - walls[2].theta) < 10 and abs(l.r-walls[2].r) > 3):
 			walls[3]=l
 			wallDone[3]=True
 		if(wallDone[1] and wallDone[2] and wallDone[3]):
 			break

	print("done getting walls. Right now we have:")
	for i in range(0,4):
		print ("WALL "+str(i)+": "+str(walls[i])) 

	print("Making sure that the best 4 walls are LONG - LONG - SHORT - SHORT")

	#Ordering the walls by theta. Want a-a-b-b regardless of whether a or b corresponds to short or long
	smallestThetaDifference = 360
	smallestThetaDifferenceIndex = 1
	for i in range(1, 4):
		tempDiff = abs(walls[i].theta - walls[0].theta)
		if(tempDiff>180):
			tempDiff = abs(tempDiff - 360)
		#print("tempDiff for index: "+str(i) +" is: "+str(tempDiff))
		if(tempDiff < smallestThetaDifference):
			smallestThetaDifference = tempDiff
			smallestThetaDifferenceIndex = i

	#print("smallestThetaDifferenceIndex is "+str(smallestThetaDifferenceIndex))
	#switch wall 1 with wall that has theta closest to wall0
	tempWall = walls[smallestThetaDifferenceIndex]
	walls[smallestThetaDifferenceIndex] = walls[1]
	walls[1] = tempWall

	bestWallsDistance = abs(walls[0].r -  walls[1].r) 
	if(bestWallsDistance < 1.2*ARENA_HEIGHT and bestWallsDistance > 0.8*ARENA_HEIGHT):
		print("best walls are SHORT. Switch walls 0&1 with 2&3")
		temp1 = walls[2]
		temp2 = walls[3]
		walls[2] = walls[0]
		walls[3] = walls[1]
		walls[0]=temp1
		walls[1]=temp2		

	print("done getting walls. they are:")
	for i in range(0,4):
		print ("WALL "+str(i)+": "+str(walls[i])) 

	print("Now get corners")

	y1 = (walls[2].r*sin(math.radians(walls[2].theta)) + walls[1].r*sin(math.radians(walls[1].theta)))/mapRes
	x1 = (walls[2].r*cos(math.radians(walls[2].theta)) + walls[1].r*cos(math.radians(walls[1].theta)))/mapRes

	y2 = (walls[1].r*sin(math.radians(walls[1].theta)) + walls[3].r*sin(math.radians(walls[3].theta)))/mapRes
	x2 = (walls[1].r*cos(math.radians(walls[1].theta)) + walls[3].r*cos(math.radians(walls[3].theta)))/mapRes

	y3 = (walls[2].r*sin(math.radians(walls[2].theta)) + walls[0].r*sin(math.radians(walls[0].theta)))/mapRes
	x3 = (walls[2].r*cos(math.radians(walls[2].theta)) + walls[0].r*cos(math.radians(walls[0].theta)))/mapRes

	y4 = (walls[0].r*sin(math.radians(walls[0].theta)) + walls[3].r*sin(math.radians(walls[3].theta)))/mapRes
	x4 = (walls[0].r*cos(math.radians(walls[0].theta)) + walls[3].r*cos(math.radians(walls[3].theta)))/mapRes

	# corners is an Array of corner Tuples: (name, X, Y, distance)
	corners = [('Corner 0', x1, y1, math.sqrt(((x1-mapWidth/2)**2 + (y1-mapHeight/2)**2))),
	('Corner 1', x2, y2, math.sqrt(((x2-mapWidth/2)**2 + (y2-mapHeight/2)**2))),
	('Corner 2', x3, y3, math.sqrt(((x3-mapWidth/2)**2 + (y3-mapHeight/2)**2))),
	('Corner 3', x4, y4, math.sqrt(((x4-mapWidth/2)**2 + (y4-mapHeight/2)**2)))]

	# sort array by distance
	corners.sort(key=lambda corner: corner[3])

	vector01 = array([corners[1][1] - corners[0][1], corners[1][2] - corners[0][2]])
	vector02 = array([corners[2][1] - corners[0][1], corners[2][2] - corners[0][2]])
	vector03 = array([corners[3][1] - corners[0][1], corners[3][2] - corners[0][2]])

	if(0 < cross(vector01,vector02)):
		print('Starting on the left')
		latest_corners.left = True
		latest_corners.LR_corner = [int(corners[0][1]), int(corners[0][2])]
		latest_corners.RR_corner = [int(corners[1][1]), int(corners[1][2])]
		latest_corners.LF_corner = [int(corners[2][1]), int(corners[2][2])]
		latest_corners.RF_corner = [int(corners[3][1]), int(corners[3][2])]
	else:
		print('Starting on the right')
		latest_corners.left = False
		latest_corners.LR_corner = [int(corners[1][1]), int(corners[1][2])]
		latest_corners.RR_corner = [int(corners[0][1]), int(corners[0][2])]
		latest_corners.LF_corner = [int(corners[3][1]), int(corners[3][2])]
		latest_corners.RF_corner = [int(corners[2][1]), int(corners[2][2])]

	print("Returning: LR=" +str(latest_corners.LR_corner) +", RR=" +str(latest_corners.RR_corner)
		+ ", LF=" +str(latest_corners.LF_corner) + ", RF=" +str(latest_corners.RF_corner))
	cornersPub.publish(latest_corners)
	if(ranOnce):
		time.sleep(SLEEP_TIME_SECS)
	ranOnce = True	
