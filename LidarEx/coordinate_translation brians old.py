import sys
import pprint
import math
import numpy as np

from numpy import *
from pylab import *
import matplotlib.gridspec as gridspec
import matplotlib.nxutils as nx

#plot point area
pi = np.pi
dotArea = pi*(5)**2

#returns the square of distance between two points
def distance(x1,y1,x2,y2):
  return((x1-x2)**2+(y1-y2)**2)

#given an xPosition, yPosition,and x and y coordinate values of the arena corners,
#returns the corner closest to xPosition, yPosition
def closestCorner(xPos, yPos, xcor, ycor):
  #fix this
  corner = (50000, 50000)
  for i in range(len( xcor)):
    if(distance(xPos,yPos,xcor[i],ycor[i]) < distance(xPos,yPos, corner[0],corner[1]) and
    distance(xPos,yPos, xcor[i],ycor[i]) != 0):

      corner = (xcor[i], ycor[i])
  return corner



def arena2Global(arenaCoords, corner1, corner2, corner3, corner4):
  # corners defined in global coordinate system

  #corner1 must be the bottom left point
  #corner2 "bottom right"
  #corner3 "top right"
  #corner4 "top left"

  #xAxisPoint -- corner2
  #localOrigin -- corner 1
  #yAxisPoint -- corner4

  #goal_x_arena = arenaCoords[0]
  #goal_y_arena = arenaCoords[1]

  #all parameters are tuples

  x1ComponentDir = 1
  y1ComponentDir = 1
  if(corner2[0]-corner1[0] < 0):
    x1ComponentDir = -1
  if(corner2[1] - corner1[1] < 0):
    y1ComponentDir = -1
  
  x2ComponentDir = 1
  y2ComponentDir = 1
  if(corner4[0] - corner1[0] < 0):
    x2ComponentDir = -1
  if(corner4[1] - corner1[1] < 0):
    y2ComponentDir = -1
  
  theta = math.atan2(abs(corner1[1]-corner2[1]), abs(corner1[0]-corner2[0]))  #angle of bottom wall of arena w.r.t. the positive global x axis
  
  xGlobal = corner1[0] + x1ComponentDir*arenaCoords[0]*math.cos(theta)+x2ComponentDir*arenaCoords[1]*math.sin(theta)

  yGlobal = corner1[1] + y1ComponentDir*arenaCoords[0]*math.sin(theta)+y2ComponentDir*arenaCoords[1]*math.cos(theta)
  
  a = (xGlobal, yGlobal)
  return a    


#returns coordinates of closest
def getYAxisPoint(xPos, yPos, xcor, ycor):
  xtemp = xcor[:]
  ytemp = ycor[:]
  xtemp.remove(xPos)
  ytemp.remove(yPos)
  #xtemp.remove(closestCorner(localOrigin[0], localOrigin[1], xCorners, yCorners)[0])
  xtemp.remove(closestCorner(xPos, yPos, xCorners, yCorners)[0])
  #ytemp.remove(closestCorner(localOrigin[0], localOrigin[1], xCorners, yCorners)[1])
  ytemp.remove(closestCorner(xPos, yPos, xCorners, yCorners)[1])
#  return closestCorner(localOrigin[0], localOrigin[1], xtemp, ytemp)
  return closestCorner(xPos, yPos, xtemp, ytemp)

def findGlobalCoords(arenaCoords):
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
  
  xGlobal = localOrigin[0] + x1ComponentDir*arenaCoords[0]*math.cos(theta)+x2ComponentDir*arenaCoords[1]*math.sin(theta)

  yGlobal = localOrigin[1] + y1ComponentDir*arenaCoords[0]*math.sin(theta)+y2ComponentDir*arenaCoords[1]*math.cos(theta)
  
  a = (xGlobal, yGlobal)
  return a


def isInObstacleArea(globalCoords):

  #Obstacle area corners in global coordinate system
  corner0 = findGlobalCoords((0, 100))
  corner1 = findGlobalCoords((0, 200))
  corner2 = findGlobalCoords((156, 100))
  corner3 = findGlobalCoords((156, 200))
    
  verts = np.array([[corner0[0], corner0[1]], [corner1[0], corner1[1]], [corner2[0], corner2[1]], [corner3[0], corner3[1]]])
    
  if(nx.pnpoly(globalCoords[0],globalCoords[1], verts)==1):
    return True
  return False
  
    
  
#corner coordinates of the arena
xCorners = []
yCorners = []

##### make mock arena coordinates to test algorithm ##############

#change theta here to spin mock arena around
theta = np.pi / 12
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

###################################################################




#Robot starting position
xPos = 600
yPos = 600

#local destination
localCoords = (50,200)

#find closest corner to robot at beginning of run, this is used as origin for local coordinate system
localOrigin = closestCorner(xPos, yPos, xCorners, yCorners)

#find other near corner at beginning of run, this is used to define positive X direction movement in the local coordinate system
xAxisPoint = closestCorner(localOrigin[0], localOrigin[1], xCorners, yCorners)

#find nearest farside corner at beginning of run, this is used to define positive Y direction movement in the local coordinate system
yAxisPoint = getYAxisPoint(localOrigin[0], localOrigin[1], xCorners, yCorners)


globalCoords = findGlobalCoords(localCoords)

print isInObstacleArea((500,500))
print isInObstacleArea((0,0))

print isInObstacleArea((500,700))
print isInObstacleArea((600,750))
print isInObstacleArea((495,770))


grid(True)
scatter(xCorners, yCorners,s =dotArea, marker = '.', c = 'b', edgecolors = 'none') 

plot((x1,x2), (y1, y2), color = 'k')
plot((x2,x3), (y2,y3), color = 'k')
plot((x3,x4), (y3,y4), color = 'k')
plot((x4,x1), (y4,y1), color = 'k')

scatter(xPos, yPos, color = 'g', s = dotArea)
#scatter(localOrigin[0], localOrigin[1], color = 'b', s = dotArea*3)
#scatter(xAxisPoint[0], xAxisPoint[1], color = 'r', s = dotArea*3)
#scatter(yAxisPoint[0], yAxisPoint[1], color = 'g', s = dotArea*3)

scatter(globalCoords[0],globalCoords[1], color = 'g' , s = dotArea*3)

#title(gridAngle*180/pi)
axes().set_aspect('equal')
show()
