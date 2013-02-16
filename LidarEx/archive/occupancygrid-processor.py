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
	
class Scan(object):  # degrees
	def __init__(self, scanData, params):
		
		for i in range (len(scanData)):
			if(scanData[i] == "data"):	
				
					
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

for l in h1.getNMostPopulatedLines(len(h1.lines)):
	print l

for p in h1.points:	
	print p
	
