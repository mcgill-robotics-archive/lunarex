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
from pylab import *

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
		self.minTheta = minTheta
		self.maxTheta = maxTheta
		self.thetaIncr = thetaIncr
		self.lines = []
		
		self.columnRank = int((math.fabs(minTheta) + math.fabs(maxTheta)) / thetaIncr) 
		self.rowRank = int(maxLineR / RIncr)
		
		# hough matrix containing line object in each entry
		self.H = [[Line(0, 0) for theta in xrange(self.columnRank)] for r in xrange(self.rowRank)] 
		
		# hough matrix containing point count in each entry
		self.Hlight = [[0 for theta in xrange(self.columnRank)] for r in xrange(self.rowRank)] 

		for point in self.points:
			k = self.minTheta
			# theta policy: http://docs.opencv.org/doc/tutorials/imgproc/imgtrans/hough_lines/hough_lines.html
			while(k <= self.maxTheta):
				lineR = point.x * math.cos(math.radians(k)) + point.y * math.sin(math.radians(k))
				if(lineR < self.rowRank and k < (self.columnRank * self.thetaIncr)):  # THE PROBLEM IS HERE! 
				# Column Rank is the number of indices, which only goes up to 90 (for minAngle=0 and maxangle=180 since angleIncr is 2). 
				# We need some functions to convert between actual thetas/Rs and hough matrix indices (hash map is a way to do this. See scans timestamp example)
					if(self.H[int(lineR / RIncr)][k].r == 0):  # line not created
						self.H[int(lineR / RIncr)][k] = Line(lineR, k)  # r, theta in line constructor
					self.H[int(lineR / RIncr)][k].addPoint(point)  # add point, increments line counter
					self.Hlight[int(lineR / RIncr)][k] += 1
				k += self.thetaIncr

		# TODO: put R, theta -> Hough indices into functions for clarity
				
		for r in xrange(self.rowRank):
			for theta in xrange(self.columnRank):
				if(self.H[r][theta].r != 0 and self.H[r][theta].pointCount != 0):  # ATTN: changed from if(self.H[r][theta].r!=0
					self.lines.append(self.H[r][theta])
	
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
		for l in self.getSortedLines()[:200]:
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
h1 = HoughMatrix(scans[4].points, 10, 0.1, 0, 180, 1)
# h1 = HoughMatrix(scans[4].points, 10, 0.1, 0, 180, 2)

# for l in h1.getNMostPopulatedLines(8):
# minTheta = 0 & maxTheta = 360 in standard Hough Transform! Not to be mistaken for Lidar's angles of operation
	# print(l)
	# a=l.getClosestPoint(5)
	# b=l.getFurthestPoint(5)
	# print("------------")

print("hough matrix has " + str(h1.columnRank) + "columns")
print("hough matrix has " + str(h1.rowRank) + "rows")

# pp = pprint.PrettyPrinter(indent=4, depth=h1.columnNumber, width=h1.rowNumber)

# np.set_printoptions(threshold='nan')
# a = np.array(h1.Hlight)
# a.reshape(h1.rowNumber, h1.columnNumber)
# pp.pprint(a)
# a.tofile("pointAHough.txt", sep="\t", format="%s")
# print(a)

print(h1)

xval = []
yval = []
for l in h1.getNMostPopulatedLines(3):
    for p in l.points:
        xval.append(p.x)
        yval.append(p.y)    
area = pi*(2)**2 # radius of dots
scatter(xval,yval,s=area, marker='.', c='b')

show()


