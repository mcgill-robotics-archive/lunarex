#!/usr/bin/env python
# -*- coding: utf-8 -*-

usage = "Usage: arg1 is the input file, it is compulsory\n"

import sys
import pprint
import math
import numpy as np

from numpy import *
from pylab import *
import matplotlib.gridspec as gridspec

NODE_NAME = 'lidar_localization'
import roslib; roslib.load_manifest(NODE_NAME)
import rospy

from sensor_msgs.msg import *

pp = pprint.PrettyPrinter(indent=4)

minAngleDefault = -1.57079637051
maxAngleDefault = 1.56643295288
angleIncDefault = 0.00436332309619

class Point(object):
	def __init__(self, theta, r):
		self.theta = float(theta)
		self.r = float(r)
		# v1.4 - cos&sin were switched around to account for lidar theta=0 to be +y axis
		self.x = math.sin(math.radians(self.theta)) * self.r
		self.y = math.cos(math.radians(self.theta)) * self.r
		# v1.5 added point weight score to use in line selection
		self.weight = abs(self.r)**(1.5)	
		
	def __str__(self):
		return "Point with angle: " + str(self.theta) + " and distance: " + str(self.r) + "\n X coord: " + str(self.x) + " and Y coord: " + str(self.y)
	
class Line(object):
	
	def __init__(self, r, theta):
		self.theta = float(theta)
		self.r = float(r)  # negative line R <---------- 0 -------------> positive lineR, along x axis
		self.points = []
		self.pointCount = 0
		#v1.5 added a line weight object, the summation of weighted points
		self.weight = 0
		
	def addPoint(self, p):
		self.points.append(p)
		self.pointCount += 1
		#v1.5 added weight calculation
		self.weight += p.weight
		
	def getClosestPoint(self, cloudSize):
		pts = sorted(self.points, key=lambda p: p.r, reverse=False)
		if(cloudSize >= len(self.points)):
			return pts[0]			
		return pts[cloudSize / 2]  # median
		
	def getFurthestPoint(self, cloudSize):
		pts = sorted(self.points, key=lambda p: p.r, reverse=True)
		if(cloudSize >= len(self.points)):
			return pts[0]			
		return pts[cloudSize / 2]  # median

	def __str__(self):
		# s=str(self.pointCount)
		s = "Line has " + str(self.pointCount) + " points at distance r= " + str(self.r) + " with angle theta = " + str(self.theta)
		# s += "\n the points are: "+self.points
		return s
		
class Scan(object):#degrees
	def __init__(self, m):
		self.minAngleRad = m.angle_min
		self.maxAngleRad = m.angle_max
		self.angleIncRad = m.angle_increment
		self.minAngleDeg = math.degrees(self.minAngleRad)
		self.maxAngleDeg = math.degrees(self.maxAngleRad)
		self.angleIncDeg = math.degrees(self.angleIncRad)
		self.points = []
		for i in range (len(m.ranges)):
			self.pointAngleDeg = self.minAngleDeg + i*self.angleIncDeg #point angle in degrees
			self.points.append(Point(self.pointAngleDeg, m.ranges[i]))
			
class HoughMatrix(object):
	
	def __init__(self, points, maxLineR, RIncr, minTheta, maxTheta, thetaIncr):
		self.points = points
		self.maxLineR = maxLineR  # in metres
		self.RIncr = RIncr
		self.minTheta = minTheta #cannot be negative
		self.maxTheta = maxTheta #cannot be negative
		self.thetaIncr = thetaIncr
		self.lines = []
		
		self.columnRank = int((math.fabs(minTheta) + math.fabs(maxTheta)) / thetaIncr) 
		self.rowRank = int(maxLineR / RIncr)

		# hough matrix containing line object in each entry
		self.H = [[Line(0, 0) for theta in xrange(self.columnRank)] for r in xrange(self.rowRank)] 
		
		# hough matrix containing point count in each entry
		self.Hlight = [[0 for theta in xrange(self.columnRank)] for r in xrange(self.rowRank)] 

		for point in self.points:
			t = minTheta
			while(t <= maxTheta):
				lineR = point.x * math.cos(math.radians(t)) + point.y * math.sin(math.radians(t))
				if(lineR<0):
					t+=thetaIncr
					continue
				
				#to avoid indexing outside matrix. Need {t/thetaIncr <= columnRank} <=> {t<=columnRank*thetaIncr} (same for R)
				if(lineR < (self.rowRank * RIncr) and t < (self.columnRank * thetaIncr)):  
					
					# Principle of indexing here is that each matrix index is an integer, but t & r can increment by a fraction
					# Actual value  ||  Matrix index
					# 	lineR 		||	lineR / RIncr
					#   t			|| 	t / thetaIncr  (note float() and int() used to get precise division results, not just quotient from possible integer division)
					
					if(self.H[int(lineR / float(RIncr))][int(t / float(thetaIncr))].r == 0):  # line not created
						self.H[int(lineR / float(RIncr))][int(t / float(thetaIncr))] = Line(lineR, t)  
					
					self.H[int(lineR / float(RIncr))][int(t / float(thetaIncr))].addPoint(point)  # add point, increments line counter
					self.Hlight[int(lineR / float(RIncr))][int(t / float(thetaIncr))] += 1
				
				t += thetaIncr
				
		for r in xrange(self.rowRank):
			for theta in xrange(self.columnRank):
				if(self.H[r][theta].r != 0 and self.H[r][theta].pointCount != 0):  # ATTN: changed from if(self.H[r][theta].r!=0
					self.lines.append(self.H[r][theta])
	
	def getMostPopulatedLineInThetaRange(self, startTheta, endTheta):
		if(startTheta < self.minTheta or endTheta > self.maxTheta):
			return -1
			
		out = Line(0,0)
		currentMax = 0
		for r in xrange(self.rowRank):
			for t in xrange(startTheta, endTheta, 1):
				l=self.H[r][int(t / float(self.thetaIncr))]
				if(l.pointCount > currentMax):
					currentMax = l.pointCount
					out = l
		 
		return out
	
	def getNMostPopulatedLines(self, N):
		return self.getSortedLines()[:N]
		
		
	# Very basic localization method
	# 1) Aligns Hough transform lines to arena using heading
	# 2) Filters data to focus on walls; Approx 0, 90, 180 degrees
	# 3) Calculate average of distance to walls
	# 4) Subtract from arena length and width to obtain position relative to lower left corner
	# Works on points A,B and D
	# Will need better than "most populated" lines to work with point C
	def getLocation(self, heading, arenaLength, arenaWidth):
		arenaX = []
		arenaY = []
		# origin is in lower left corner
		
		# Use N most populated lines to calculate location
		for l in self.getSortedLines()[:30]:
		#for l in self.getWeightSortedLines()[:30]:
			
			# Align lidar with map using heading so readings point towards backpanel
			mapAngle = l.theta + heading
			# print l
			# print abs(l.r)
			
			# Filter X/Y data based on angle to walls
			if (mapAngle >= 85) and (mapAngle <= 95):
					arenaY.append(abs(l.r))	
			if (heading <= 0):
				if (mapAngle > 0) and  (mapAngle <= 10):
					arenaX.append(abs(l.r))				
			else:
				if (mapAngle > 170) and  (mapAngle <= 180):
					arenaX.append(-abs(l.r))
					arenaWidth = 0	
						
		xPosition = arenaWidth - mean(arenaX)
		yPosition = arenaLength - mean(arenaY)
		if(yPosition < 0):
			yPosition = 0
		#print arenaY
		#print mean(arenaY)
					
		#print "Lidar is at: "
		#print xPosition , yPosition
		#print len(self.lines)
		#print "\n"
		
		p = Point(0,0)
		p.x = xPosition
		p.y = yPosition
		return p
	
	def getSortedLines(self):
		return sorted(self.lines, key=lambda l: l.pointCount, reverse=True)
		
	def __str__(self):
		out="hough matrix has " + str(self.columnRank) + "columns\n"
		out+="hough matrix has " + str(self.rowRank) + "rows\n"
		for row in self.Hlight:
			rowString = ""
			for entry in row:
				rowString += str(entry)
				rowString += "\t"
			out += rowString
			out += "\n"
		return out
	
	def getWeightSortedLines(self):
		return sorted(self.lines, key=lambda l: l.weight, reverse=True)
	
	def getNMostWeightedLines(self, N):
		return self.getWeightSortedLines()[:N]
								

gs = gridspec.GridSpec(2, 2, width_ratios=[1,1], height_ratios=[1,1])
dotArea = pi*(2.5)**2 # radius of dots

def lidar_handler(msg):
	if(msg.header.stamp.second%2==0):
		scan = Scan(msg)
		hough = HoughMatrix(scan.points, 2, 0.1, 0, 360, 5)
		arenaLength = 70 #usually 1.11
		arenaWidth = 21 #usually 0.896
		pos = hough.getLocation(0, arenaLength, arenaWidth)	 #full size testing: 1.11, 0.896
		
rospy.init_node(NODE_NAME)
rospy.Subscriber("/scan", LaserScan, lidar_handler)
rospy.spin()

xval =[]
yval = []
for l in hough.getNMostPopulatedLines(3):
	for p in l.points:
		xval.append(p.x)
		yval.append(p.y)    
subplot(gs[0])
ylabel('meters',fontdict={'fontsize':20})
grid(True)
axis([-1.5, 1.5, -1.5, 1.5])
scatter(xval,yval,s=dotArea, marker='.', c='b', edgecolors = 'none')

xweight = [] 
yweight = []
for l in hough.getNMostWeightedLines(3):
	for p in l.points:
		xweight.append(p.x)
		yweight.append(p.y)
subplot(gs[1])    
#autoscale(enable=True, axis='both', tight=None)
axis([-1.5, 1.5, -1.5, 1.5])
xlabel('meters',fontdict={'fontsize':20})
grid(True)
scatter(xweight,yweight,s=dotArea, marker='.', c='r', edgecolors ='none')

xPos = []
yPos = []
subplot(gs[2])    
axis([0, arenaWidth, 0, arenaLength])
areaPos = pi*(10)**2 # radius of dots
xlabel('meters',fontdict={'fontsize':20})
#ylabel('meters',fontdict={'fontsize':20})
xPos.append(pos.x)
yPos.append(pos.y)

grid(True)
scatter(xPos,yPos,s=areaPos, marker='.', c='g', edgecolors ='none')

xTotal = []
yTotal = []
xTotal = xval + xweight
yTotal = yval + yweight
subplot(gs[3])    
axis([-1.5, 1.5, -1.5, 1.5])
xlabel('meters',fontdict={'fontsize':20})

grid(True)
scatter(xTotal,yTotal,s=dotArea, marker='.', c='r', edgecolors ='none')

show()	


