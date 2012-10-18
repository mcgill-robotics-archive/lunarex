#!/usr/bin/env python
# -*- coding: utf-8 -*-

#This is a first prototype for parsing a Lidar "friendly format" raw data file.
#first and only argument of script should be the data file name
#select your scan by giving it's scan time, and find a scan value according to its parameter: (field.ranges529 for instance). 

usage = "Usage: arg1 is the input file, it is compulsory\n"
import sys
import pprint
pp = pprint.PrettyPrinter(indent=4)

if(len(sys.argv)<2):
	print(usage);
	sys.exit()

inputFile = open(sys.argv[1], 'r') 
inputString = inputFile.read()
scans = inputString.splitlines()

parameters = scans[0].split(",") 
paramhash = {}
i=0
for param in parameters:
	#print(param, i)
	paramhash[str(param)]=i 
	i+=1

j=-1
timehash = {}
for scan in scans:
	j+=1
	if j==0:
		continue
	tempScan = scan.split(",")	
	scans[j]=tempScan
	#print("tempScan[0] is: "+tempScan[0])
	timehash[tempScan[0]] = j

#pp.pprint(timehash)
	
while(True):
	while(True):
		time = str(input("enter the time of the scan to retrieve:\n"))
		#time = "1348343731317672000"
		if(timehash.get(time, "boohoo") == "boohoo"):
			print("time is not a timehash key..")
			continue
		if(scans[timehash[time]] is not None):
			break

	print("scan done at time: " +str(time)+" with scan index: "+str(timehash[time])+"\n")
	#pp.pprint(scans[timehash[time]])	
	
	#pp.pprint(paramhash)

	
	while(True):
		userParam = raw_input("enter the param of the scan value you want to retrieve:\n")
		if(paramhash.get(str(userParam), "naaaaah") == "naaaaah"):
			print("param is not a paramhash key..")
			continue
		if(scans[timehash[time]][paramhash[userParam]] is not None):
			break

	print("param "+userParam+" for scan id "+str(timehash[time])+" is:  "+str(scans[timehash[time]][paramhash[userParam]]))
