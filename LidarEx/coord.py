import math
import numpy as np
import matplotlib.nxutils as nx


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

def isInObstacleArea(globalCoords, corner1, corner2, corner3, corner4):

  #Obstacle area corners in global coordinate system
  obs_corner0 = arena2Global((0, 100), corner1, corner2, corner3, corner4)
  obs_corner1 = arena2Global((0, 200), corner1, corner2, corner3, corner4)
  obs_corner2 = arena2Global((156, 100), corner1, corner2, corner3, corner4)
  obs_corner3 = arena2Global((156, 200), corner1, corner2, corner3, corner4)
    
  verts = np.array([[obs_corner0[0], obs_corner0[1]], [obs_corner1[0], obs_corner1[1]], [obs_corner2[0], obs_corner2[1]], [obs_corner3[0], obs_corner3[1]]])
    
  if(nx.pnpoly(globalCoords[0],globalCoords[1], verts)==1):
    return True
  return False