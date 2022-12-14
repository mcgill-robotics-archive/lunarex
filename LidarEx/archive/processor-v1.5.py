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

minAngleDefault = -1.57079637051
maxAngleDefault = 1.56643295288
angleIncDefault = 0.00436332309619
arenaWidth = 0.896  # 0.913m - measured, tweaked based on lidar data
arenaLength = 1.11  # 1.22m - measured, tweaked based on lidar data

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
		
class Scan(object):  # degrees
	def __init__(self, scanData, params):
		self.scanData = scanData
		self.params = params
		self.points = []
		self.minAngleRad = float(minAngleDefault)
		self.maxAngleRad = float(maxAngleDefault)
		self.angleIncRad = float(angleIncDefault)
		self.minAngleDeg = math.degrees(minAngleDefault)
		self.maxAngleDeg = math.degrees(maxAngleDefault)
		self.angleIncDeg = math.degrees(angleIncDefault)
		
		for i in range (len(scanData)):
			if(scanData[i] == "laser"):
				continue
			# print(scanData[i])
			if params[i] == "%time":
				self.time = scanData[i]  # time in seconds since Unix epoch
			elif params[i] == "field.angle_min":
				self.minAngleDeg = math.degrees(float(scanData[i]))  # min angle in radians
				self.minAngleRad = float(scanData[i])  # min angle in radians
			elif params[i] == "field.angle_max":
				self.maxAngleDeg = math.degrees(float(scanData[i]))  # max degrees in radians
				self.maxAngleRad = float(scanData[i])  # max angle in radians
			elif params[i] == "field.angle_increment":
				self.angleIncDeg = math.degrees(float(scanData[i]))  # angle increment in degrees
				self.angleIncRad = float(scanData[i])  # angle increment in radians
			elif "field.ranges" in params[i]:
				pointNumber = int(params[i][len("field.ranges"):])
				# note: changed to allow for angle start on right & scans going anti-clockwise
				pointAngleDeg = self.maxAngleDeg - pointNumber * self.angleIncDeg  # point angle in degrees
				pointAngleRad = self.maxAngleRad - pointNumber * self.angleIncRad  # point angle in radians
				self.points.append(Point(pointAngleDeg, scanData[i]))		
			
class HoughMatrix(object):
	
	def __init__(self, points, maxLineR, RIncr, minTheta, maxTheta, thetaIncr):
		self.points = points
		self.maxLineR = maxLineR  # in metres
		self.RIncr = RIncr
		self.minTheta = minTheta #cannot be negative
		self.maxTheta = maxTheta #cannot be negative
		self.thetaIncr = thetaIncr
		self.lines = []
		self.arenaWidth = 0.896  # 0.913m - measured, tweaked based on lidar data
		self.arenaLength = 1.11  # 1.22m - measured, tweaked based on lidar data
		

		
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
	def getLocation(self, heading):
		arenaX = []
		arenaY = []
		arenaWidth = self.arenaWidth
		# origin is in lower left corner
		
		# Use N most populated lines to calculate location
		for l in self.getSortedLines()[:50]:
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
						
		xPosition = arenaWidth - median(arenaX)
		yPosition = self.arenaLength - median(arenaY)
		if(yPosition < 0):
			yPosition = 0
		print arenaY
		print median(arenaY)
		
		if(xPosition < 0):
			xPosition = 0
		
		print arenaX
		print median(arenaX)
					
		print "Lidar is at: "
		print xPosition , yPosition
		#print len(self.lines)
		print "\n"
		
		p = Point(0,0)
		p.x = xPosition
		p.y = yPosition
		return p
		
	def getLocation2(self, heading):
		arenaX = []
		arenaY = []
		arenaWidth = self.arenaWidth
		# origin is in lower left corner
		
		line = self.getMostPopulatedLineInThetaRange((85+heading), (95+heading))
		print(line)
			
		# Filter X/Y data based on angle to walls
		arenaY.append(abs(self.getMostPopulatedLineInThetaRange((85+heading), (95+heading)).r))		
		if (heading <= 0):
			arenaX.append(abs(self.getMostPopulatedLineInThetaRange((0+heading), (10+heading)).r))				
		else:
			arenaX.append(-abs(self.getMostPopulatedLineInThetaRange((170+heading), (180+heading)).r))				
			arenaWidth = 0	
						
		xPosition = arenaWidth - median(arenaX)
		yPosition = self.arenaLength - median(arenaY)
		if(yPosition < 0):
			yPosition = 0
		print arenaY
		print median(arenaY)
		
		if(xPosition < 0):
			xPosition = 0
		
		print arenaX
		print median(arenaX)
					
		print "Lidar is at: "
		print xPosition , yPosition
		#print len(self.lines)
		print "\n"
		
		p = Point(0,0)
		p.x = xPosition
		p.y = yPosition
		return p
	
	def getSortedLines(self):
		return sorted(self.lines, key=lambda l: l.pointCount, reverse=True)
		
	def __str__(self):
		out = ""
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
										
					
if(len(sys.argv) < 2):
	print(usage)
	sys.exit()
	
inputFile = open(sys.argv[1], 'r') 
inputString = inputFile.read()
scans = inputString.splitlines()

params = scans[0].split(",")
	
j = -1
timehash = {}
for scan in scans:
	j += 1
	if j == 0:
		continue
	scanData = scan.split(",")
	scans[j] = Scan(scanData, params)
	timehash[scanData[0]] = j
	
# 	def __init__(self, points, maxLineR, RIncr, minTheta, maxTheta, thetaIncr):
h1 = HoughMatrix(scans[4].points, 2, 0.1, 0, 360, 5)

pos = h1.getLocation2(85);

print("hough matrix has " + str(h1.columnRank) + "columns")
print("hough matrix has " + str(h1.rowRank) + "rows")

print(h1)

gs = gridspec.GridSpec(2, 2, width_ratios=[1,1], height_ratios=[1,1])

xval = []
yval = []
xMeasured = []
yMeasured = []
xMeasured.append(arenaWidth-0.64)
yMeasured.append(0.60)

for l in h1.getNMostPopulatedLines(3):
    for p in l.points:
        xval.append(p.x)
        yval.append(p.y)    
        
        
#xlabel('meters',fontdict={'fontsize':20})
#axis([xmin,xmax,ymin,ymax])
subplot(gs[0])
area = pi*(2.5)**2 # radius of dots
ylabel('y (meters)',fontdict={'fontsize':15})
title('Most populated lines',fontdict={'fontsize':20})
#autoscale(enable=True, axis='both', tight=None)
grid(True)
axis([-1.5, 1.5, -1.5, 1.5])
scatter(xval,yval,s=area, marker='.', c='b', edgecolors = 'none')

#show()
xweight = []
yweight = []
for l in h1.getNMostWeightedLines(3):
    for p in l.points:
        xweight.append(p.x)
        yweight.append(p.y)
subplot(gs[1])    
area = pi*(2.5)**2 # radius of dots
#autoscale(enable=True, axis='both', tight=None)
axis([-1.5, 1.5, -1.5, 1.5])
xlabel('',fontdict={'fontsize':15})
title('Weight-adjusted lines',fontdict={'fontsize':20})
#ylabel('meters',fontdict={'fontsize':20})

grid(True)
scatter(xweight,yweight,s=area, marker='.', c='r', edgecolors ='none')

xPos = []
yPos = []
subplot(gs[2])    
axis([-.05, h1.arenaWidth, -.05, h1.arenaLength])
areaPos = pi*(10)**2 # radius of dots
title('View of the arena',fontdict={'fontsize':20})
xlabel('x (meters)',fontdict={'fontsize':15})
#ylabel('meters',fontdict={'fontsize':20})
xPos.append(pos.x)
yPos.append(pos.y)

grid(True)
scatter(xPos,yPos,s=areaPos, marker='.', c='g', edgecolors ='none')
scatter(xMeasured,yMeasured,s=areaPos, marker='.', c='y', edgecolors = 'none')

xTotal = []
yTotal = []
for l in h1.getNMostWeightedLines(3):
    for p in l.points:
        xTotal.append(p.x)
        yTotal.append(p.y)

for l in h1.getNMostPopulatedLines(3):
    for p in l.points:
        xTotal.append(p.x)
        yTotal.append(p.y)
  
subplot(gs[3])    
area = pi*(2.5)**2 # radius of dots
axis([-1.5, 1.5, -1.5, 1.5])
xlabel('',fontdict={'fontsize':20})
title('Combined lines',fontdict={'fontsize':20})
#ylabel('meters',fontdict={'fontsize':20})


grid(True)
scatter(xTotal,yTotal,s=area, marker='.', c='r', edgecolors ='none')

show()


