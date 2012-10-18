#!/usr/bin/env python
# -*- coding: utf-8 -*-

usage = "Usage: arg1 is the input file, it is compulsory\n"

import sys
import pprint
import math
#import numpy as np
#import scipy as sp
#import matplotlib as mpl
#import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter(indent=4)

minAngleDefault = -1.57079637051
maxAngleDefault = 1.56643295288
angleIncDefault = 0.00436332309619

class Point(object):
	def __init__(self, theta, r):
		self.theta = float(theta)
		self.r = float(r)
		self.x = math.cos(math.degrees(self.theta))*self.r
		self.y = math.sin(math.degrees(self.theta))*self.r
		
	def __str__(self):
		return "Point twih angle: "+str(self.theta)+"and distance: "+str(self.r)
	
		
class Scan(object):degrees
	def __init__(self, scanData, params):
		self.scanData = scanData
		self.params = params
		self.points = []
		self.minAngle = math.degrees(minAngleDefault)
		self.maxAngle = math.degrees(maxAngleDefault)
		self.angleInc = math.degrees(angleIncDefault)
		
		for i in range (len(scanData)):
			if(scanData[i]=="laser"):
				continue
			#print(scanData[i])
			if params[i] == "%time":
				self.time = scanData[i]
			elif params[i] == "field.angle_min":
				self.minAngle = math.degrees(float(scanData[i]))
			elif params[i] == "field.angle_max":
				self.maxAngle = math.degrees(float(scanData[i]))
			elif params[i] == "field.angle_increment":
				self.angleInc = math.degrees(float(scanData[i]))
			elif "field.ranges" in params[i]:
				pointNumber = int(params[i][len("field.ranges"):])
				pointAngle = self.minAngle + pointNumber*self.angleInc
				self.points.append(Point(pointAngle, scanData[i]))		

	def computeDistances(self):
		count = 0.0
		average = 0.0
		for i in range(len(self.points)):
			for j in range(len(self.points)):
				count = count + 1.0
				distance = math.sqrt(math.pow(self.points[i].x - self.points[j].x, 2) + math.pow(self.points[i].x - self.points[j].x, 2))
				average = average + distance/count
		print(average/count)
			
				
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
	
#for i in range(0, 720):
	#if i%5 == 0:
		#print(scans[4].points[i])

scans[4].computeDistances()
