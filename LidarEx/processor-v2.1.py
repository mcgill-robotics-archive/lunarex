#!/usr/bin/env python
# -*- coding: utf-8 -*-

usage = "Usage: arg1 is the input file, it is compulsory\n"

import sys
import pprint
import math
#import numpy as np
#import scipy as sp

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
		self.maxLineR = maxLineR # in metres
		self.RIncr = RIncr
		self.minTheta = minTheta
		self.maxTheta = maxTheta
		self.thetaIncr = thetaIncr
		self.lines = []
		
		self.H = [[Line(0,0) for theta in xrange(int(math.fabs(minTheta) + math.fabs(maxTheta)))] for r in xrange(int(maxLineR/RIncr))] 
		
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
		
i=0
scans = []
def lidar_handler(msg):
	scans.append(Scan(msg))
	
rospy.init_node(NODE_NAME)
rospy.Subscriber("/scan", LaserScan, lidar_handler)
rospy.spin()

