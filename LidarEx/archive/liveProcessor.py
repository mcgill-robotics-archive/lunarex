#!/usr/bin/env python
# -*- coding: utf-8 -*-

usage = "Usage: arg1 is the input file, it is compulsory\n"

import sys
import pprint
import math

import fileinput

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
		return "Point with angle: "+str(self.theta)+"and distance: "+str(self.r)
	
		
class Scan(object):
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
				
scans=[]
timehash={}

i=-1
for line in fileinput.input():
	i+=1
	if i>200:
		break
	if i==0:
		params = line.split(",")
		continue
	scanData = line.split(",")
	scans.append(Scan(scanData, params))
	print("Scan: "+str(i)+"at time: "+scanData[0]+" just created.")
	timehash[scanData[0]] = i
	
for i in range(0, len(scans[4].points)):
	print(scans[4].points[i])

print(len(scans[4].points))
	
#scans[4].computeDistances()
