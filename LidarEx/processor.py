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
		self.x = math.cos(math.radians(self.theta))*self.r
		self.y = math.sin(math.radians(self.theta))*self.r
		
	def __str__(self):
		return "Point with angle: "+str(self.theta)+" and distance: "+str(self.r) + "\n X coord: "+str(self.x)+" and Y coord: "+str(self.y)
	
		
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

	def computeDistances(self):
		count = 0
		average = 0.0
		for i in range(len(self.points)):
			for j in range(len(self.points)):
				count += 1
				#distance between points using  Distance formula
				distanceCart = math.hypot(self.points[i].x - self.points[j].x, self.points[i].y - self.points[j].y)
				#distance between points using Law of Cosines
				distancePolar = math.sqrt(self.points[i].r*self.points[i].r + self.points[j].r*self.points[j].r - 2*self.points[i].r*self.points[j].r*math.cos(self.angleIncRad*(j-i)))
				average = average + distanceCart/count
			#Print distance in Cartesian and Polar
			#print("Cartesian: " + str(distanceCart))
			#print("Polar:     " + str(distancePolar))
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
	
for i in range(0, len(scans[4].points)):
	if(i%5 == 0): #print every 5 variables
		print(scans[4].points[i])

scans[4].computeDistances()
