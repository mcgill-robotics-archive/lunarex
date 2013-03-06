#!/usr/bin/env python

'''
Lunarex Map_Builder Node
Author I: Sebastien Lemieux-Codere
Author II:Alan Yan
'''

import roslib; roslib.load_manifest('kinect_node')

from kinect_node.srv import *
import rospy
import sys
import numpy as np
import freenect
import cv
import frame_convert
import math
from pylab import *


height = 460
width = 640
vertical_view_angle = 43 # in degrees
horizontal_view_angle = 57 # in degrees
vert_angle = vertical_view_angle * math.pi / 180# in rads
horiz_angle = horizontal_view_angle * math.pi / 180 # in rads
height_of_kinect =80 # cm
Xmid = width/2
Zmid = height/2
 
sobel_x = np.matrix('-1 0 1;-2 0 2; -1 0 1')
sobel_y = np.matrix('-1 -2 -1; 0 0 0; 1 2 1')
#print sobel_x, sobel_y


tilt_x_axis =0.05# in rads
focalLength = 580 # in pixels

def handle_service(req):
    print "Returning kinect data matrix"
    kinect_matrix = np.array(createMap(), np.int32)
    return KinectDataResponse(kinect_matrix.shape[0], kinect_matrix.shape[1], np.reshape(kinect_matrix, -1))

def service_server():
    s = rospy.Service('kinect_service', KinectData, handle_service)
    print "Test Server Ready."
    rospy.spin()

def createMap():
    # this takes kinect data using libfreenect and outputs a filtered 2d array that is a overhead view with 100 for obstacles
    #map = [  [  0 for i in range(30)]for ii in range(40)]
    print "Starting..."
    ind = 0


    try:

        depth = get_depth(ind)
        video = get_video(ind)
    except TypeError:
	ind = 0
	print "error!!!!"

    depth_matrix = freenect.sync_get_depth(ind)

	# get sample vectors to detect the tilt angle
    sample_vectors = []
    for y in range(10, 50): # ignore the low accuracy borders
	for x in range(10, 40): # ignore the low accuracy borders
		if (x %2 ==0 and y %2 ==0):
			val = getDepthFromPixel(depth_matrix[0][y*height/50][x*width/50])
			if (val<100000 and val > 10):
		 		sample_vectors.append(createVector(x*width/50,y*height/50, int(val)))
	
	# find the tilt angle
	step_size = 0.005
	x_tilt =-math.pi/5
	score = 0
	best_score = 0
	best_angle = 0
	while (x_tilt<= 0.05):
		score = 0
		x_tilt += step_size
		for i in range(len(sample_vectors)):
			vector = adjustForTilt(sample_vectors[i], x_tilt)
			vector_height = getHeightOfVector(vector)
			threshold = 6
			if ( (vector_height < threshold) and (vector_height > -threshold) ):	
				score+=1
				#print x_tilt, math.fabs(getHeightOfVector(sample_vectors[i])), sample_vectors[i][0],sample_vectors[i][1]
		if (score>=best_score):
			#print x_tilt, score
			#print "new high score!!"

			best_angle = x_tilt
			best_score = score

    print "angle:  "
    print best_angle 
    print " score: "
    print  best_score
    print len(sample_vectors)
    tilt_x_axis = best_angle
    #print sample_vectors


    	##
	# process the image
	##
    projection = [[0 for i in range(30)] for ii in range(40)]
    print "Starting Processing"
    for iFrame in range(height/5, height-height/3):
		#if(iFrame %2 !=0):
		#	continue

	for iiFrame in range(width/5, width- width/5):
			#if(iiFrame %2 !=0):
			#	continue

		val = getDepthFromPixel(depth_matrix[0][iFrame][iiFrame])
		if (val<100000 and val > 10):
			vector = createVector(iiFrame,iFrame, int(val))
			vector = adjustForTilt(vector, tilt_x_axis )
				#print vector
			if(((vector[0])/10+30/2)>=0 and (((vector[0])/10+30/2))<30 and (vector[1])>0 and (40-((vector[1])/10))>0):
				if (math.fabs( getHeightOfVector(vector))>math.fabs(projection[int(40-(vector[1])/10)][int((vector[0]/10+30/2))])):
					projection[int((40-vector[1]/10))][int((vector[0]/10+30/2))] =(getHeightOfVector(vector))# +projection[int((40-vector[1]/10))][int((vector[0]/10+30/2))])/2 # average of previous and new
						#if (getHeightOfVector(vector)<10):
						#	print vector[1], getHeightOfVector(vector)



    for i in range(40):
	print str(40*10 -i*10) + "cm: "+str(projection[i])	
    print str("      " )+str([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

	# Sobel filter
    sobel_filter = [[0 for i in range(30)] for ii in range(40)]
    for y in range(1, len(sobel_filter )-1):
	for x in range(1,len(sobel_filter[0])-1):

		subset = np.matrix(  [   
		[ projection[y-1][x-1], projection[y-1][x], projection[y-1][x+1]  ],  
		[ projection[y][x-1]  ,   projection[y][x],   projection[y][x+1]  ],
  		[ projection[y+1][x-1], projection[y+1][x], projection[y+1][x+1]  ]   
		]  )

		variance_x =sum(np.fabs( subset*sobel_x))
		varience_y =sum(np.fabs(subset*sobel_y))

		variance = math.sqrt(variance_x**2 + varience_y**2)
		if (variance>230):
			variance = 100
		else:
			variance = 0
		sobel_filter[y][x] = int( variance)


    for i in range(40):
	print str(40*10 -i*10) + "cm: "+str(sobel_filter[i])	
    print str("      " )+str([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
    

    
    return sobel_filter


# 
# Helper functions
#


def createVector(x,y, depth):
    	vector = []
    	vector.append(x-Xmid)           # x component of the vector
    	vector.append(focalLength) # y component of the vector
    	vector.append(y - Zmid)
    	# normalise vector and multiply by registered depth
    	length =  math.sqrt(vector[0]*vector[0] + vector[1]*vector[1]+vector[2]*vector[2])
    	vector[0] = vector[0] / length  *  depth
    	vector[1] =  vector[1] / length  *  depth 
    	vector[2] = - vector[2] / length  *  depth
    	return vector
def adjustForTilt(vector, x_axis):
	# tilt about the x-axis
	vect= [vector[0],vector[1],vector[2]]
	vect[1] = vector[1]*math.cos(x_axis )+vector[2]* -1*math.sin(x_axis )# y-adjustement
	vect[2] = vector[1]*math.sin(x_axis )+vector[2]*math.cos(x_axis )# z-adjustement	
	return vect

def getHeightOfVector(vector):
	return int( height_of_kinect + vector[2])

def get_depth(ind):
    	return frame_convert.pretty_depth_cv(freenect.sync_get_depth(ind)[0])


def get_video(ind):
    	return frame_convert.video_cv(freenect.sync_get_video(ind)[0])

def getDepthFromPixel(pix):
   	return 100.0/(-0.0030711016*pix + 3.3309495161) 



print createMap() #  runs it when  the node is starting

if __name__ == "__main__":
    try:
	rospy.init_node("kinect_srv_server")
	service_server()
    except KeyboardInterrupt:
	sys.exit(0)







