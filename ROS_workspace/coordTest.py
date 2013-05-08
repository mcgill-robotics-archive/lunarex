import sys

#sys.path.append("~/McGill/McGill_LunarEx_2013/ROS_workspace/")

#from corner_detector.coord import arena2Global
import corner_detector.coord as coord

#def arena2Global(arenaCoords, corner1, corner2, corner3, corner4, resolution):

#corner1 must be the bottom left point
#corner2 "bottom right"
#corner3 "top right"
#corner4 "top left"

arenaCoords = (2, 4)
bottom_left = (100, 100)
bottom_right = (300, 100)
top_right = (300, 300)
top_left = (100, 300)
resolution = 0.025

print(coord.arena2Global(arenaCoords, bottom_left, bottom_right, top_right, top_left, resolution))

