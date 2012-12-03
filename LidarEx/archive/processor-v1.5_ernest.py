#!/usr/bin/env python
# -*- coding: utf-8 -*-

usage = "Usage: arg1 is the input file, it is compulsory\n"

import sys
import pprint
import math
import numpy as np
# import scipy as sp
# import matplotlib as mpl
# import matplotlib.pyplot as plt

from numpy import *

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
		
	def __str__(self):
		return "Point with angle: " + str(self.theta) + " and distance: " + str(self.r) + "\n X coord: " + str(self.x) + " and Y coord: " + str(self.y)
	
class Line(object):
	
	def __init__(self, r, theta):
		self.theta = float(theta)
		self.r = float(r)  # negative line R <---------- 0 -------------> positive lineR, along x axis
		self.points = []
		self.pointCount = 0
		
	def addPoint(self, p):
		self.points.append(p)
		self.pointCount += 1
		
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
		arenaWidth = 0.896  # 0.913m - measured, tweaked based on lidar data
		arenaLength = 1.11  # 1.22m - measured, tweaked based on lidar data
		arenaX = []
		arenaY = []
		# origin is in lower left corner
		
		# Use N most populated lines to calculate location
		for l in self.getSortedLines()[:30]:
			
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
		print arenaY
		print mean(arenaY)
					
		print "Lidar is at: "
		print xPosition , yPosition
		#print len(self.lines)
		print "\n"
	
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
h1 = HoughMatrix(scans[50].points, 2, 0.1, 0, 360, 5)


print("hough matrix has " + str(h1.columnRank) + "columns")
print("hough matrix has " + str(h1.rowRank) + "rows")
print(h1)

# Get getLocation takes heading in degrees
# 0 degrees is towards back wall; -/+ 90 to face left/right walls respectively
h1.getLocation(0)

print(h1.getMostPopulatedLineInThetaRange(0, 5))
print(h1.getMostPopulatedLineInThetaRange(85, 95))

print("BREAK ------------")


for l in h1.getNMostPopulatedLines(len(h1.lines)):
	print l

	
for p in h1.points:	
	print p
	
