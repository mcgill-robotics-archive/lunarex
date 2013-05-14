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

rospy.loginfo("Started waiting for hector mapping map service")
rospy.wait_for_service('dynamic_map')
rospy.loginfo("Done waiting for corner detector service")

cornersPub = rospy.Publisher("corners", Corners)

while(True):
	corner_detector_proxy = rospy.ServiceProxy('dynamic_map', GetMap)
	latest_map = corner_detector_proxy()
	gridData = latest_map.map.data
	latest_corners.width = latest_map.map.info.width
	latest_corners.height = latest_map.map.info.height
	latest_corners.resolution = latest_map.map.info.resolution
	rospy.loginfo("Just started crunching a new map.")

	rospy.loginfo("Done waiting for map.")

	#COLLECTING OCCUPANCY GRID
	occupancyGrid = np.empty((latest_corners.width,latest_corners.height),dtype='int')
	occupancyGrid = np.reshape(gridData,(latest_corners.width,latest_corners.height), order='F') #C is row major order; F is col major

	#DEFINING HOUGH MATRIX
	mapRes = latest_corners.resolution 
	Rres = mapRes
	mapWidth = latest_corners.width
	mapHeight = latest_corners.height
	Rrank = int((math.sqrt(2)*max(mapWidth, mapHeight))/Rres) #nb of R buckets
	Tres = 1
	Trank = 360

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

	rospy.loginfo("done getting walls. Right now we have:")
	for i in range(0,4):
		print ("WALL "+str(i)+": "+str(walls[i])) 

	rospy.loginfo("Making sure that the best 4 walls are LONG - LONG - SHORT - SHORT")

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

	rospy.loginfo("done getting walls. they are:")
	for i in range(0,4):
		print ("WALL "+str(i)+": "+str(walls[i])) 

	rospy.loginfo("Now get corners")

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
		rospy.loginfo('Starting on the left')
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

	rospy.loginfo("Returning: LR=" +str(latest_corners.LR_corner) +", RR=" +str(latest_corners.RR_corner)
		+ ", LF=" +str(latest_corners.LF_corner) + ", RF=" +str(latest_corners.RF_corner))
	cornersPub.publish(latest_corners)
	time.sleep(SLEEP_TIME_SECS)

# print("here")
# rospy.spin()
