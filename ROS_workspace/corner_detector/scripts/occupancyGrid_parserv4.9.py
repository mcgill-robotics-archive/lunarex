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
NUMBER_OF_POTENTIAL_WALLS = 100

WALL_THETA_THRESH = 3
WALL_R_THRESH = 0.4

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
		self.points = []
		
	def __str__(self):
		s = "Line has " + str(len(self.points)) + " points at distance r= " + str(self.r) + " with angle theta = " + str(self.theta)
		return s
		
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
rospy.init_node('corner_detector')

print("Started waiting for hector mapping map service")
rospy.wait_for_service('dynamic_map')
print("Done waiting for hector mapping map service")

cornersPub = rospy.Publisher("corners", Corners)

ranOnce = False

while(not ranOnce):
	ranOnce=True
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

	Rres = mapRes*4

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

	print("PointCount = " +str(pointCount))

	#PLACING HOUGH MATRIX LINES INTO LINE OBJECTS
	lines=[]
	pointThresh = pointCount / 50
	for r in xrange(Rrank):
		for t in xrange(Trank):
			if(H[r][t]!=0 and len(H[r][t].points)>pointThresh):
				lines.append(H[r][t])

	print("sort & print best lines")
	sortedLines = sorted(lines, key=lambda l: len(l.points), reverse=True)
		
	for l in sortedLines[:NUMBER_OF_POTENTIAL_WALLS]:
		print l

	#DEFINE WALLS AND WALL BUCKETS
	walls=[sortedLines[0],-1,-1,-1] 
	bestWallsAreLong = True	

 	print("fill walls & wall buckets")

	bestTheta = BIGNUMBER
	wallDone = [True, False, False, False]
	while(not( wallDone[1] or wallDone[2] or wallDone[3])):
		for l in sortedLines[:NUMBER_OF_POTENTIAL_WALLS]: #order of decreasing points/line
	 		print("Evaluating line: " +str(l))
	 		if(not wallDone[1]):
	 			if(abs(l.theta - walls[0].theta) < WALL_THETA_THRESH or abs(abs(l.theta - walls[0].theta) - 180) < WALL_THETA_THRESH):
	 			#we have a parallel wall. Is it within arena width or length?
	 				tempR = l.r
	 				if(l.theta > 180):
	 					tempR = - tempR
	 				if(walls[0].theta > 180):
	 					tempR = - tempR
	 				rDiff = abs(walls[0].r - tempR)
	 				if(rDiff > ARENA_WIDTH-WALL_R_THRESH and rDiff < ARENA_WIDTH+WALL_R_THRESH):
	 					#wall[0] & l are the long walls
	 					print("Line " +str(l)+ "getting set as wall1")
	 					walls[1]=l
	 					wallDone[1]=True
	 					bestWallsAreLong= True
	 				elif(rDiff > ARENA_HEIGHT-WALL_R_THRESH and rDiff < ARENA_HEIGHT+WALL_R_THRESH):
	 					#wall[0] & l are the short walls
	 					print("Line " +str(l)+ "getting set as wall1")
	 					walls[1]=l
	 					wallDone[1]=True
	 					bestWallsAreLong = False
	 		if(not wallDone[2]):
	 			if(abs(l.theta - walls[0].theta) > 90 - WALL_THETA_THRESH and abs(l.theta - walls[0].theta) < 90 + WALL_THETA_THRESH
	 				or (abs(l.theta - walls[0].theta) > 270 - WALL_THETA_THRESH and abs(l.theta - walls[0].theta) < 270 + WALL_THETA_THRESH)):
	 				#both thetas on same 1/2 circle case
					wallDone[2]=True
	 				walls[2]=l
					print("Line " +str(l) +"getting set as wall2")
	 		elif wallDone[2] and not wallDone[3] :
	 			if(abs(l.theta - walls[2].theta) < WALL_THETA_THRESH or abs(abs(l.theta - walls[2].theta) - 180) < WALL_THETA_THRESH):
	 				tempR = l.r
	 				if(l.theta > 180):
	 					tempR = - tempR
	 				if(walls[2].theta > 180):
	 					tempR = - tempR
					rDiff = abs(walls[2].r - tempR)
					if(rDiff > ARENA_WIDTH-WALL_R_THRESH and rDiff < ARENA_WIDTH+WALL_R_THRESH):
						#wall[0] & l are the long walls
						walls[3]=l
						wallDone[3]=True
						print("Line " +str(l) +"getting set as wall3")
					elif(rDiff > ARENA_HEIGHT-WALL_R_THRESH and rDiff < ARENA_HEIGHT+WALL_R_THRESH):
						#wall[0] & l are the short walls
						walls[3]=l
						wallDone[3]=True
						print("Line " +str(l) +"getting set as wall3")

	 		if(wallDone[1] and wallDone[2] and wallDone[3]):
	 			break
		WALL_R_THRESH      = WALL_R_THRESH * 1.5
		WALL_THETA_THRESH  = WALL_THETA_THRESH * 1.5

	print("done getting walls. Right now we have:")
	for i in range(0,4):
		print ("WALL "+str(i)+": "+str(walls[i])) 

	print("Making sure that the best 4 walls are LONG - LONG - SHORT - SHORT")

	if(not bestWallsAreLong):
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

	#print("Returning: LR=" +str(latest_corners.LR_corner) +", RR=" +str(latest_corners.RR_corner)
	#	+ ", LF=" +str(latest_corners.LF_corner) + ", RF=" +str(latest_corners.RF_corner))
	print("\tself.insertValueInOccupancyGrid("+str(latest_corners.LR_corner[0])+","+str(latest_corners.LR_corner[1])+",100)")
	print("\tself.insertValueInOccupancyGrid("+str(latest_corners.RR_corner[0])+","+str(latest_corners.RR_corner[1])+",100)")
	print("\tself.insertValueInOccupancyGrid("+str(latest_corners.LF_corner[0])+","+str(latest_corners.LF_corner[1])+",100)")
	print("\tself.insertValueInOccupancyGrid("+str(latest_corners.RF_corner[0])+","+str(latest_corners.RF_corner[1])+",100)")

	# get the area
	long_wall = [latest_corners.LR_corner[0] - latest_corners.LF_corner[0], latest_corners.LR_corner[1] - latest_corners.LF_corner[1]]
	len_long_wall = math.sqrt(long_wall[0]**2 + long_wall[1]**2) * mapRes
	short_wall = [latest_corners.LR_corner[0] - latest_corners.RR_corner[0], latest_corners.LR_corner[1] - latest_corners.RR_corner[1]]
	len_short_wall = math.sqrt(short_wall[0]**2 + short_wall[1]**2) * mapRes
	area = len_long_wall * len_short_wall

	latest_corners.area = int(area)

	print "AREA = " + str(latest_corners.area)


	cornersPub.publish(latest_corners)
	if(ranOnce):
		time.sleep(SLEEP_TIME_SECS)
	ranOnce = True	
