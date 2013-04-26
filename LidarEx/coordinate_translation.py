import sys
import pprint
import math
import numpy as np

from numpy import *
from pylab import *
import matplotlib.gridspec as gridspec


#plot point area
pi = np.pi
dotArea = pi*(5)**2

#returns the square of distance between two points
def distance(x1,y1,x2,y2):
  return((x1-x2)**2+(y1-y2)**2)


def closestCorner(xPos, yPos, xcor, ycor):
  #fix this
  corner = (50000, 50000)
  for i in range(len( xcor)):
    if(distance(xPos,yPos,xcor[i],ycor[i]) < distance(xPos,yPos, corner[0],corner[1]) and
    distance(xPos,yPos, xcor[i],ycor[i]) != 0):

      corner = (xcor[i], ycor[i])
  return corner

def getYAxisPoint(xPos, yPos, xcor, ycor):
  xtemp = xcor[:]
  ytemp = ycor[:]
  xtemp.remove(xPos)
  ytemp.remove(yPos)
  xtemp.remove(closestCorner(localOrigin[0], localOrigin[1], xCorners, yCorners)[0])
  ytemp.remove(closestCorner(localOrigin[0], localOrigin[1], xCorners, yCorners)[1])
  return closestCorner(localOrigin[0], localOrigin[1], xtemp, ytemp)

def vectorAddition(xAxisPoint, yAxisPoint, localOrigin, localCoords):
  x1ComponentDir = 1
  y1ComponentDir = 1
  if(xAxisPoint[0]-localOrigin[0] < 0):
    x1ComponentDir = -1
  if(xAxisPoint[1] - localOrigin[1] < 0):
    y1ComponentDir = -1
  
  x2ComponentDir = 1
  y2ComponentDir = 1
  if(yAxisPoint[0] - localOrigin[0] < 0):
    x2ComponentDir = -1
  if(yAxisPoint[1] - localOrigin[1] < 0):
    y2ComponentDir = -1
  
  theta = math.atan2(abs(localOrigin[1]-xAxisPoint[1]), abs(localOrigin[0]-xAxisPoint[0]))
  print theta
  xGlobal = localOrigin[0] + x1ComponentDir*localCoords[0]*math.cos(theta)+x2ComponentDir*localCoords[1]*math.sin(theta)

  yGlobal = localOrigin[1] + y1ComponentDir*localCoords[0]*math.sin(theta)+y2ComponentDir*localCoords[1]*math.cos(theta)
  
  a = (xGlobal, yGlobal)
  return a


def findGlobalCoords(xPos, yPos, xCorners, yCorners, localCoords):
  localOrigin = closestCorner(xPos, yPos, xCorners, yCorners)
  xAxisPoint = closestCorner(localOrigin[0], localOrigin[1], xCorners, yCorners)
  yAxisPoint = getYAxisPoint(localOrigin[0], localOrigin[1], xCorners, yCorners)
  a= vectorAddition(xAxisPoint, yAxisPoint,localOrigin, localCoords)
  return a





#corners
xCorners = []
yCorners = []

#Robot Position
xPos = 600
yPos = 600

#local destination
localCoords = (50, 200)



theta = 1*pi / 20
#manually position first corner, then arena makes itself
x1, y1 = 490, 580

x2, y2 = x1-296*math.sin(theta), y1+296*math.cos(theta)

x3 = x2+156*math.cos(theta)
y3 = y2+156*math.sin(theta)

x4 = x1+156*math.cos(theta) 
y4 = y1+156*math.sin(theta)


xCorners.append(x1)
yCorners.append(y1)

xCorners.append(x2)
yCorners.append(y2)

xCorners.append(x3)
yCorners.append(y3)

xCorners.append(x4)
yCorners.append(y4)

#the local origin is defaulted to the corner closest to the robot

#the corner closest to the origin will be used to find the angle of the arena 
localOrigin = closestCorner(xPos, yPos, xCorners, yCorners)
xAxisPoint = closestCorner(localOrigin[0], localOrigin[1], xCorners, yCorners)
yAxisPoint = getYAxisPoint(localOrigin[0], localOrigin[1], xCorners, yCorners)


grid(True)
scatter(xCorners, yCorners,s =dotArea, marker = '.', c = 'b', edgecolors = 'none') 



plot((x1,x2), (y1, y2), color = 'k')
plot((x2,x3), (y2,y3), color = 'k')
plot((x3,x4), (y3,y4), color = 'k')
plot((x4,x1), (y4,y1), color = 'k')

scatter(xPos, yPos, color = 'g', s = dotArea)
scatter(localOrigin[0], localOrigin[1], color = 'b', s = dotArea*3)
scatter(xAxisPoint[0], xAxisPoint[1], color = 'r', s = dotArea*3)
scatter(yAxisPoint[0], yAxisPoint[1], color = 'g', s = dotArea*3)




a = findGlobalCoords(xPos, yPos, xCorners, yCorners, localCoords)
scatter(a[0],a[1], color = 'g' , s = dotArea*3)



#title(gridAngle*180/pi)
axes().set_aspect('equal')
show()
