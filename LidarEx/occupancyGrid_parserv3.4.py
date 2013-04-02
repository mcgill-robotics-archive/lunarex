#IMPORTS
import rosbag
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Int8
import numpy as np
import roslib.message
import math
import struct
import geometry_msgs.msg
import nav_msgs.msg
import std_msgs.msg
from pylab import *
import matplotlib.gridspec as gridspec

BIGNUMBER = 1000

class Line(object):
	
	def __init__(self, r, theta):
		self.theta = float(theta)
		self.r = float(r)  
		
		#y=mx+b representation
		if(math.sin(math.radians(theta))==0):
			self.m = BIGNUMBER
			self.b=BIGNUMBER
		else:
			self.m = -(math.cos(math.radians(theta))/math.sin(math.radians(theta)))
			self.b = r/math.sin(math.radians(theta))
		self.points = []
		
	def __str__(self):
		s = "Line has " + str(len(self.points)) + " points at distance r= " + str(self.r) + " with angle theta = " + str(self.theta)
		return s
		
class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

def sameRBucket(a, b): #are a & b within rThresh% of eachother?
	if((a==0 and b<rThresh and b>-rThresh) or (b==0 and a<rThresh and a>-rThresh)):
		 return True
	if(abs(b-a) < rThresh):
		return True
	return False


def sameTBucket(t1, t2): #are t1&t2 within tThresh of eachother?
	if(abs(t1-t2)<=tThresh):
		return True
	if(t1+360-t2 <= tThresh or t2+360-t1<=tThresh):
		return True
	return False	

def sameBuckets(l1, l2):
	return (sameRBucket(l1.r, l2.r) and sameTBucket(l1.theta, l2.theta))

#BAG SETUP
#bag = rosbag.Bag('/home/ernie/Dropbox/LunarEx2012-2013/Software Team/ROS/Bags/localization_feb10.bag')
##DO NOT USE THIS BAG. IT SUCKS. bag = rosbag.Bag('/home/ernie/Dropbox/LunarEx2012-2013/Software Team/ROS/Bags/2013-03-19-14-26-50.bag') #shitty

#netbook bag
bag = rosbag.Bag('basic_localization_stage.bag')
#DO NOT USE THIS BAG. IT SUCKS. bag = rosbag.Bag('/home/ernie/Dropbox/LunarEx2012-2013/Software Team/ROS/Bags/2013-03-19-14-21-47.bag') #shitty

#bag = rosbag.Bag('/home/ernie/Dropbox/LunarEx2012-2013/Software Team/ROS/Bags/2013-02-20-21-37-14.bag') # awesome stage bag
#bag = rosbag.Bag('/home/ernie/Dropbox/LunarEx2012-2013/Software Team/ROS/Bags/2013-03-19-14-19-48.bag')

#RETRIEVING MAP META DATA
mapWidth=0
mapHeight=0 
mapRes = 0 #the length of each cell
for topic, msg, t in bag.read_messages(topics=['/map_metadata']):
	mapWidth = msg.width
	mapHeight=msg.height
	mapRes = msg.resolution
	break

print("META: map width = "+str(mapWidth)+" height=" +str(mapHeight)+" and res= "+str(mapRes) )


#COLLECTING OCCUPANCY GRID
occupancyGrid = np.empty((mapWidth,mapHeight),dtype='int')
gridData = []
msg = OccupancyGrid()
for topic, msg, t in bag.read_messages(topics=['/map']):
	gridData = msg.data

occupancyGrid = np.reshape(gridData,(mapWidth,mapHeight))

#DEFINING HOUGH MATRIX
Rres = mapRes/4 #r bucket resolution. Doesn't make sense to have r buckets smaller than map res.
Rrank = int((math.sqrt(2)*max(mapWidth, mapHeight))/Rres) #nb of R buckets
Tres = 1
Trank = 360#360/1#90/1#180/1


print ("***Hough matrix has***")
print(str(Rrank) +" R buckets of size: "+str(Rres))
print("and : "+str(Trank) +" theta buckets of size: " +str(Tres))

H = [[0 for T in xrange(Trank)] for R in xrange(Rrank)] 

#PLACING POINTS INTO THE MATRIX
for i in range(0,len(occupancyGrid)):
	for j in range(0,len(occupancyGrid[i])):
		if(occupancyGrid[i][j]==100):
			for t in range(0, Trank):	
				lineR = i*mapRes*math.cos(math.radians(t)) + j*mapRes*math.sin(math.radians(t))
				if(lineR<0):
					t+=180
					t=t%360
					lineR=abs(lineR)
				if(H[int(lineR/Rres)][t])==0:
					H[int(lineR/Rres)][t]=Line(lineR, t)
				H[int(lineR/Rres)][t].points.append(Point(i,j))

#PLACING HOUGH MATRIX LINES INTO LINE OBJECTS
lines=[]
for r in xrange(Rrank):
	for t in xrange(Trank):
		if(H[r][t]!=0 and len(H[r][t].points)>0):
			lines.append(H[r][t])

#sort & print best lines
sortedLines = sorted(lines, key=lambda l: len(l.points), reverse=True)
for l in sortedLines[:30]:
	print l
	
#DEFINE WALLS AND WALL BUCKETS
walls=[0,0,0,0] 
wallBuckets=[[] for i in range(0,4)]
walls[0]=sortedLines[0] #assume most populous line is first wall

#PARAMS: threshold for r & theta wall buckets
tThresh = 5 #absolute: 2de
rThresh = 1.0 #absolute: 8% R difference between 2 walls max in 1 bucket
	
#FILL WALLS & WALL BUCKETS
#If wall to fill & a line is not in a current wall bucket, make the line a wall
wallIndex=1 #next wall to fill
for l in sortedLines: #order of decreasing points/line
	if(walls[wallIndex%4]==0):#not filled
		sameBucket=False
		for w in walls:
			if(w!=0 and sameBuckets(l, w)==True):#not the same bucket as any current wall
				sameBucket=True
		if(sameBucket==False):
			walls[wallIndex]=l

			wallIndex+=1	
	for i in range(0,4):
		if(walls[i]!=0 and sameBuckets(l, walls[i])):
			wallBuckets[i].append(l)		
				
				
for i in range(0,4):
	print ("WALL "+str(i)+": "+str(walls[i])) 

print ("R: " + str(walls[0].r) + ", Theta: " + str(walls[0].theta))
print ("R: " + str(walls[1].r) + ", Theta: " + str(walls[1].theta))
print ("R: " + str(walls[2].r) + ", Theta: " + str(walls[2].theta))
print ("R: " + str(walls[3].r) + ", Theta: " + str(walls[3].theta))

print ("X0: " + str(walls[0].r*cos(math.radians(walls[0].theta))/mapRes) + ", Y0: " + str(walls[0].r*sin(math.radians(walls[0].theta))/mapRes))
print ("X1: " + str(walls[1].r*cos(math.radians(walls[1].theta))/mapRes) + ", Y1: " + str(walls[1].r*sin(math.radians(walls[1].theta))/mapRes))
print ("X2: " + str(walls[2].r*cos(math.radians(walls[2].theta))/mapRes) + ", Y2: " + str(walls[2].r*sin(math.radians(walls[2].theta))/mapRes))
print ("X3: " + str(walls[3].r*cos(math.radians(walls[3].theta))/mapRes) + ", Y3: " + str(walls[3].r*sin(math.radians(walls[3].theta))/mapRes))
#print ("X3: " + str(walls[3].r*cos(0)/Rres) + ", Y3: " + str(walls[3].r*sin(0)/Rres))

# y1: 457
# x1: 445

y1 = (walls[2].r*sin(math.radians(walls[2].theta)) + walls[1].r*sin(math.radians(walls[1].theta)))/mapRes
x1 = (walls[2].r*cos(math.radians(walls[2].theta)) + walls[1].r*cos(math.radians(walls[1].theta)))/mapRes

y2 = (walls[1].r*sin(math.radians(walls[1].theta)) + walls[3].r*sin(math.radians(walls[3].theta)))/mapRes
x2 = (walls[1].r*cos(math.radians(walls[1].theta)) + walls[3].r*cos(math.radians(walls[3].theta)))/mapRes

y3 = (walls[2].r*sin(math.radians(walls[2].theta)) + walls[0].r*sin(math.radians(walls[0].theta)))/mapRes
x3 = (walls[2].r*cos(math.radians(walls[2].theta)) + walls[0].r*cos(math.radians(walls[0].theta)))/mapRes

y4 = (walls[0].r*sin(math.radians(walls[0].theta)) + walls[3].r*sin(math.radians(walls[3].theta)))/mapRes
x4 = (walls[0].r*cos(math.radians(walls[0].theta)) + walls[3].r*cos(math.radians(walls[3].theta)))/mapRes
 

print ("Corner 1: x: " + str(x1) + ", y:" + str(y1) + " => Yellow ")  
print ("Corner 2: x: " + str(x2) + ", y:" + str(y2) + " => Blue")  
print ("Corner 3: x: " + str(x3) + ", y:" + str(y3) + " => Green")  
print ("Corner 4: x: " + str(x4) + ", y:" + str(y4) + " => Red")  

axis([-100, mapWidth, -100, mapHeight])
areaPos = pi*(2)**2 # radius of dots
areaP = pi*(8)**2 # radius of dots
xlabel('cells',fontdict={'fontsize':20})

# PLOT THE OCCUPANCY GRID AND CORNERS
xWalls = []
yWalls = []
x = []
y = []

# Populate xWalls and yWalls with all the points on the 4 most populated lines
for j in range(0,4):
	for i in range(0,len(walls[j].points)):
		xWalls.append(walls[j].points[i].x)
		yWalls.append(walls[j].points[i].y)

		
for i in range(0,len(occupancyGrid)):
	for j in range(0,len(occupancyGrid[i])):
		if(occupancyGrid[i][j] == 100):
			x.append(i)
			y.append(j)


grid(True)
#scatter(x,y,s=areaPos, marker='.', c='c', edgecolors ='none')
scatter(x1,y1,s=areaP, marker='.', c='y', edgecolors ='none')
scatter(x2,y2,s=areaP, marker='.', c='b', edgecolors ='none')
scatter(x3,y3,s=areaP, marker='.', c='g', edgecolors ='none')
scatter(x4,y4,s=areaP, marker='.', c='r', edgecolors ='none')

#print(str(xWalls))

#scatter(x,y,s=areaPos, marker='.', c='c', edgecolors ='none')
scatter(xWalls,yWalls,s=areaPos, marker='.', c='b', edgecolors ='none')
scatter(walls[0].r*cos(math.radians(walls[0].theta))/mapRes,walls[0].r*sin(math.radians(walls[0].theta))/mapRes,s=areaP, marker='.', c='y', edgecolors ='none')
scatter(walls[1].r*cos(math.radians(walls[1].theta))/mapRes,walls[1].r*sin(math.radians(walls[1].theta))/mapRes,s=areaP, marker='.', c='b', edgecolors ='none')
scatter(walls[2].r*cos(math.radians(walls[2].theta))/mapRes,walls[2].r*sin(math.radians(walls[2].theta))/mapRes,s=areaP, marker='.', c='g', edgecolors ='none')
scatter(walls[3].r*cos(math.radians(walls[3].theta))/mapRes,walls[3].r*sin(math.radians(walls[3].theta))/mapRes,s=areaP, marker='.', c='r', edgecolors ='none')

show()

#corner0X = (walls[1].b-walls[0].b)/(float(walls[0].m-walls[1].m))
#print corner0X
