#!/usr/bin/env python
# -*- coding: utf-8 -*-

usage = "Usage: arg1 is the input file, it is compulsory\n"

import sys
import pprint
import math
#import numpy as np
#import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter(indent=4)

minAngleDefault = -1.57079637051
maxAngleDefault = 1.56643295288
angleIncDefault = 0.00436332309619

class Point(object):
	def __init__(self, theta, r):
		self.theta = float(theta)
		self.r = float(r)
		self.x = math.cos(math.radians(self.theta))*self.r
		self.y = math.sin(math.radians(self.theta))*self.r
		
	def __str__(self):
		return "Point with angle: "+str(self.theta)+" and distance: "+str(self.r) + "\n X coord: "+str(self.x)+" and Y coord: "+str(self.y)
	
class Line(object):
	
	def __init__(self, r, theta):
		self.theta = float(theta)
		self.r = float(r) 				# negative line R <---------- 0 -------------> positive lineR, along x axis
		self.points = []
		self.pointCount = 0
		
	def addPoint(self, p):
		self.points.append(p)
		self.pointCount +=1
		
	def getClosestPoint(self, cloudSize):
		pts = sorted(self.points, key = lambda p: p.r, reverse = False)
		if(cloudSize>=len(self.points)):
			return pts[0]			
		return pts[cloudSize/2] #median
		
	def getFurthestPoint(self, cloudSize):
		pts = sorted(self.points, key = lambda p: p.r, reverse = True)
		if(cloudSize>=len(self.points)):
			return pts[0]			
		return pts[cloudSize/2] #median

	def __str__(self):
		s = "Line has "+str(self.pointCount)+" points at distance r= "+str(self.r)+" with angle theta = "+str(self.theta)
		#s += "\n the points are: "+self.points
		return s
		
class Scan(object):#degrees
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
			if(scanData[i]=="laser"):
				continue
			#print(scanData[i])
			if params[i] == "%time":
				self.time = scanData[i]											#time in seconds since Unix epoch
			elif params[i] == "field.angle_min":
				self.minAngleDeg = math.degrees(float(scanData[i]))				#min angle in radians
				self.minAngleRad = float(scanData[i])							#min angle in radians
			elif params[i] == "field.angle_max":
				self.maxAngleDeg = math.degrees(float(scanData[i]))				#max degrees in radians
				self.maxAngleRad = float(scanData[i])							#max angle in radians
			elif params[i] == "field.angle_increment":
				self.angleIncDeg = math.degrees(float(scanData[i]))				#angle increment in degrees
				self.angleIncRad = float(scanData[i])							#angle increment in radians
			elif "field.ranges" in params[i]:
				pointNumber = int(params[i][len("field.ranges"):])
				pointAngleDeg = self.minAngleDeg + pointNumber*self.angleIncDeg #point angle in degrees
				pointAngleRad = self.minAngleRad + pointNumber*self.angleIncRad #point angle in radians
				self.points.append(Point(pointAngleDeg, scanData[i]))		
			
class HoughMatrix(object):
	def __init__(self, points, maxLineR, RIncr, minTheta, maxTheta, thetaIncr):
		self.points = points
		self.maxLineR = maxLineR # in metres
		self.RIncr = RIncr
		self.minTheta = minTheta
		self.maxTheta = maxTheta
		self.thetaIncr = thetaIncr
		self.lines = []
		
		self.H = [[Line(0,0) for theta in xrange(int(math.fabs(minTheta) + math.fabs(maxTheta)))] for r in xrange(int(maxLineR/RIncr))] 
		#the range of thetas should be int((math.fabs(minTheta) + math.fabs(maxTheta))/thetaIncr)		

		for point in self.points:
			k=self.minTheta
			#print point.r, k
			while(k<=self.maxTheta):
				lineR = point.x*math.cos(math.radians(k)) + point.y*math.sin(math.radians(k))
				if(lineR<maxLineR/RIncr and k<math.fabs(minTheta) + math.fabs(maxTheta)):
					if(self.H[int(lineR*100)][int(k)].r==0): #line not created
						self.H[int(lineR*100)][int(k)]=Line(lineR, k) #r, theta in line constructor
						#print("creating line with r: "+str(lineR) +" and theta: "+str(k))
					self.H[int(lineR*100)][int(k)].addPoint(point) #add point, increments line counter
				k+=thetaIncr
				
		for r in xrange(int(maxLineR/RIncr)):
			for theta in xrange(int(math.fabs(minTheta) + math.fabs(maxTheta))):
				if(self.H[r][theta].r!=0):
					self.lines.append(self.H[r][theta])
	
	def getNMostPopulatedLines(self, N):
		return self.getSortedLines()[:N]
	
	def getSortedLines(self):
		return sorted(self.lines, key = lambda l: l.pointCount, reverse = True)
		
	#def __str__(self):
		#return str(self.lines)
			
if(len(sys.argv)<2):
	print(usage)
	sys.exit()
	
inputFile = open(sys.argv[1], 'r') 
inputString = inputFile.read()
scans = inputString.splitlines()

params = scans[0].split(",")
	
j=-1
timehash = {}
for scan in scans:
	j+=1
	if j==0:
		continue
	scanData = scan.split(",")
	scans[j]= Scan(scanData, params)
	timehash[scanData[0]] = j
	
maxLineR = 10
minTheta = 0
maxTheta = 90
thetaIncr = 1

#	def __init__(self, points, maxLineR, RIncr, minTheta, maxTheta, thetaIncr):
for l in HoughMatrix(scans[4].points, 10, 0.01, 0, 90, 1).getNMostPopulatedLines(6):
# minTheta = 0 & maxTheta = 360 in standard Hough Transform! Not to be mistaken for Lidar's angles of operation
	print(l)
	a=l.getClosestPoint(5)
	b=l.getFurthestPoint(5)
	print("------------")
