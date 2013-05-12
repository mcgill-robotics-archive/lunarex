import math
import numpy as np
import matplotlib.nxutils as nx

import roslib; roslib.load_manifest('corner_detector')

import rospy
import tf

''' 
Documentation of coordinate frames: https://sites.google.com/site/lunarex2013/software/coordinatetransformationreference
'''

#ANGLE TRANSFORMS
#takes in degrees, returns degrees
def arenaAngle2hectorAngle(arenaAngle, LR_corner, RR_corner, LF_corner, RF_corner):
  theta = math.atan2(abs(LR_corner[1]-RR_corner[1]), abs(LR_corner[0]-RR_corner[0])) #angle of bottom wall of arena w.r.t. the positive global x axis
  theta = theta * 180.0/math.pi
  hectorAngle = arenaAngle + 90 - theta
  rospy.loginfo("coord.arenaAngle2hectorAngle received: "+str(arenaAngle)+" and is returning: "+str(hectorAngle))
  return hectorAngle

#takes in degrees, returns degres
def arenaAngle2mobileAngle(arenaAngle, slam_out_pose, LR_corner, RR_corner, LF_corner, RF_corner):
  #interpret quaternion of current angle as radians on [-pi, pi]
  current_hector_heading = quatToDegrees(slam_out_pose)
  goal_hector_heading = arenaAngle2hectorAngle(arenaAngle, LR_corner, RR_corner, LF_corner, RF_corner)
  mobileAngle = goal_hector_heading - current_hector_heading
  rospy.loginfo("coord.arenaAngle2mobileAngle received: "+str(arenaAngle)+" and is returning: "+str(mobileAngle))
  #mobileAngle = mobileAngle * math.pi/180.0
  #rospy.loginfo("which is " +str(mobileAngle) + "in radians")
  return mobileAngle

def quatToDegrees(slam_out_pose):
  angles = tf.transformations.euler_from_quaternion([slam_out_pose.pose.orientation.x,slam_out_pose.pose.orientation.y, slam_out_pose.pose.orientation.z, slam_out_pose.pose.orientation.w])
  return angles[2]*(180.0/math.pi)

#POSITION TRANSFORMS
def arena2mobile(arenaCoords, slam_out_pose, LR_corner, RR_corner, LF_corner, RF_corner, resolution, global_map_size):
  # step1: transform arenaX and arenaY to global frame  - these are goals
  # step2: get current position in Hector frame from hector mapping, and transform it to global frame
  # step3: subtract the two sets of global coordinates, and multiply by the resolution to convert to meters

  (goal_x_global, goal_y_global) = arena2global(arenaCoords, LR_corner, RR_corner, LF_corner, RF_corner, resolution)
  (current_x_global, current_y_global) = hector2global(slam_out_pose, resolution, global_map_size)
  
  theta = math.atan2(abs(LR_corner[1]-RR_corner[1]), abs(LR_corner[0]-RR_corner[0]))  #angle of bottom wall of arena w.r.t. the positive global x axis

  goal_x_mobile = (goal_y_global - current_y_global)*resolution
  goal_y_mobile = -1.0*(goal_x_global - current_x_global)*resolution
  
  #this is a vector in global
  mobile_coords = (goal_x_mobile, goal_y_mobile)

  #rotate the vector from global to hector
  mobile_coords = rotateVector2D(mobile_coords, 90-quatToDegrees(slam_out_pose))
  rospy.loginfo("coord.arena2mobile received: "+str(arenaCoords)+" and is returning: "+str(mobile_coords))
  return mobile_coords

def hector2global(slam_out_pose, resolution, global_map_size):
  #meters to cells

  x_hector = slam_out_pose.pose.position.x
  y_hector = slam_out_pose.pose.position.y

  #translate global frame origin to middle of map
  x_temp = x_hector + global_map_size*resolution/2
  y_temp = y_hector - global_map_size*resolution/2

  x_global = -1*y_temp / resolution #resolution in m/cell, see documentation on google site for logic here
  y_global = x_temp / resolution 

  global_coords = (x_global, y_global)
  rospy.loginfo("coord.hector2global received: x_hector="+str(x_hector)+" & y_hector="+str(y_hector)+" and is returning: "+str(global_coords))

  return global_coords

#ORDER: LR, RR, RF, LF, resolution
def arena2global(arenaCoords, LR_corner, RR_corner, LF_corner, RF_corner, resolution):
  # arenaCoords in meters
  #output Global coords in cells

  #xAxisPoint -- RR_corner
  #localOrigin -- corner 1
  #yAxisPoint -- RF_corner

  #goal_x_arena = arenaCoords[0]
  #goal_y_arena = arenaCoords[1]

  #all parameters are tuples

  #scale by resolution
  arenaCoords_inCells = (int(arenaCoords[0]/resolution), int(arenaCoords[1] / resolution))   #resolution is m per cell

  print("corners received")
  print(str(LR_corner) + str(RR_corner) + str(LF_corner) + str(RF_corner))

  x1ComponentDir = 1
  y1ComponentDir = 1
  if(RR_corner[0] < LR_corner[0]):
    x1ComponentDir = -1
  if(RR_corner[1] < LR_corner[1]):
    y1ComponentDir = -1
  
  x2ComponentDir = 1
  y2ComponentDir = 1
  if(LF_corner[0] < LR_corner[0]):
    x2ComponentDir = -1
  if(LF_corner[1] < LR_corner[1]):
    y2ComponentDir = -1
  
  print("x1ComponentDir is: "+str(x1ComponentDir))
  print("x2ComponentDir is: "+str(x2ComponentDir))
  print("y1ComponentDir is: "+str(y1ComponentDir))
  print("y2ComponentDir is: "+str(y2ComponentDir))

  print("calling atan with " +str(abs(LR_corner[1]-RR_corner[1])) +" and: " + str(abs(LR_corner[0]-RR_corner[0])))
  theta = math.atan2(abs(LR_corner[1]-RR_corner[1]), abs(LR_corner[0]-RR_corner[0]))  #angle of bottom wall of arena w.r.t. the positive global x axis
  
  print(theta)

  xGlobal = LR_corner[0] + x1ComponentDir*arenaCoords_inCells[0]*math.cos(theta)+x2ComponentDir*arenaCoords_inCells[1]*math.sin(theta)
  yGlobal = LR_corner[1] + y1ComponentDir*arenaCoords_inCells[0]*math.sin(theta)+y2ComponentDir*arenaCoords_inCells[1]*math.cos(theta)
  
  globalCoords = (xGlobal, yGlobal)
  rospy.loginfo("coord.arena2global received: arenaCoord="+str(arenaCoords)+" ,equal to arenaCoords_inCells="+str(arenaCoords_inCells)+ "; and is returning: "+str(globalCoords))
  return globalCoords    

def isInObstacleArea(globalCoords, LR_corner, RR_corner, LF_corner, RF_corner, resolution):

  #Obstacle area corners in global coordinate system
  obs_LR_corner = arena2global((0, 100), LR_corner, RR_corner, LF_corner, RF_corner, resolution)
  obs_RR_corner = arena2global((0, 200), LR_corner, RR_corner, LF_corner, RF_corner, resolution)
  obs_LF_corner = arena2global((156, 100), LR_corner, RR_corner, LF_corner, RF_corner, resolution)
  obs_RF_corner = arena2global((156, 200), LR_corner, RR_corner, LF_corner, RF_corner, resolution)
    
  verts = np.array([[obs_LR_corner[0], obs_LR_corner[1]], [obs_RR_corner[0], obs_RR_corner[1]], [obs_LF_corner[0], obs_LF_corner[1]], [obs_RF_corner[0], obs_RF_corner[1]]])    
  isInObstacleArea = False  
  
  if(nx.pnpoly(globalCoords[0],globalCoords[1], verts)==1):
    isInObstacleArea=True

  rospy.loginfo("coord.isInObstacleArea received: globalCoords="+str(globalCoords)+" and is returning: "+str(isInObstacleArea))
  return isInObstacleArea

 #Rotate a coordinate ector
def rotateVector2D(vector, angle):
  rotated_vect = []
  rotated_vect.append(  vector[0]*math.cos(angle)  - vector[1]*math.sin(angle)             )
  rotated_vect.append(  vector[0]*math.sin(angle)  + vector[1]*math.cos(angle)   )
  return rotated_vect