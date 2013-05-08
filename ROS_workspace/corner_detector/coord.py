import math
import numpy as np
import matplotlib.nxutils as nx

import roslib; roslib.load_manifest('corner_detector')

import rospy
import tf

''' 
Documentation of coordinate frames: https://sites.google.com/site/lunarex2013/software/coordinatetransformationreference
'''

def arenaAngle2hectorAngle(angle, corner1, corner2, corner3, corner4):
    theta = math.atan2((corner2[1]-corner1[1]), (corner2[0]-corner1[0]))  #angle of bottom wall of arena w.r.t. the positive global x axis
    return theta * 180.0/math.pi + angle


def arenaAngle2mobileAngle(arenaAngle, slam_out_pose, corner1, corner2, corner3, corner4):
  #interpret quaternion of current angle as radians on [-pi, pi]
  hector_headings = tf.transformations.euler_from_quaternion([slam_out_pose.pose.orientation.x,slam_out_pose.pose.orientation.y, slam_out_pose.pose.orientation.z, slam_out_pose.pose.orientation.w]) 
  current_heading = hector_headings[2] # only z component of euler angle
  #subtract
  mobileAngle = arenaAngle2hectorAngle(arenaAngle, corner1, corner2, corner3, corner4)-current_heading
  return mobileAngle

def arena2mobile(arenaCoords, slam_out_pose, corner1, corner2, corner3, corner4, resolution):
  # step1: transform arenaX and arenaY to global frame  - these are goals
  # step2: get current position in Hector frame from hector mapping, and transform it to global frame
  # step3: subtract the two sets of global coordinates, and multiply by the resolution to convert to meters

  (goal_x_global, goal_y_global) = arena2global(arenaCoords, corner1, corner2, corner3, corner4, resolution)
  (current_x_global, current_y_global) = hector2global(slam_out_pose, resolution)
  goal_x_mobile = (goal_x_global - current_x_global)*resolution
  goal_y_mobile = (goal_y_global - current_y_global)*resolution
  return (goal_x_mobile, goal_y_mobile)

def hector2global(slam_out_pose, resolution):
  x_hector = slam_out_pose.pose.position.x
  y_hector = slam_out_pose.pose.position.y

  x_global = -1*y_hector / resolution #resolution in m/cell, see documentation on google site for logic here
  y_global = x_hector / resolution

  return (x_global, y_global)

def arena2global(arenaCoords, corner1, corner2, corner3, corner4, resolution):
  # corners defined in global coordinate system
  # arenaCoords in meters
  #output Global coords in cells


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

  #scale by resolution
  arenaCoords[0] /= resolution   #resolution is m per cell
  arenaCoords[1] /= resolution   #resolution is m per cell

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

def isInObstacleArea(globalCoords, corner1, corner2, corner3, corner4, resolution):

  #Obstacle area corners in global coordinate system
  obs_corner0 = arena2global((0, 100), corner1, corner2, corner3, corner4, resolution)
  obs_corner1 = arena2global((0, 200), corner1, corner2, corner3, corner4, resolution)
  obs_corner2 = arena2global((156, 100), corner1, corner2, corner3, corner4, resolution)
  obs_corner3 = arena2global((156, 200), corner1, corner2, corner3, corner4, resolution)
    
  verts = np.array([[obs_corner0[0], obs_corner0[1]], [obs_corner1[0], obs_corner1[1]], [obs_corner2[0], obs_corner2[1]], [obs_corner3[0], obs_corner3[1]]])
    
  if(nx.pnpoly(globalCoords[0],globalCoords[1], verts)==1):
    return True
  return False