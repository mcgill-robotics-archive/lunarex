#!/usr/bin/env python
"""This goes through each kinect on your system, grabs one frame and
displays it.  Uncomment the commented line to shut down after each frame
if your system can't handle it (will get very low FPS but it should work).
This will keep trying indeces until it finds one that doesn't work, then it
starts from 0.
"""
import freenect
import cv
import frame_convert
import math


#
# Variables
#

height = 460
width = 640
vertical_view_angle = 43 # in degrees
horizontal_view_angle = 57 # in degrees
vert_angle = vertical_view_angle * math.pi / 180# in rads
horiz_angle = horizontal_view_angle * math.pi / 180 # in rads
height_of_kinect = 82 # cm
Xmid = width/2
Zmid = height/2 

#
#
#


def getFocalLength():
    return (height/2)/ (math.tan(vert_angle/2))

def createVector(x,y, depth):
    vector = []
    vector.append(x-Xmid)           # x component of the vector
    vector.append(getFocalLength()) # y component of the vector
    vector.append(y - Zmid)
    # normalise vector and multiply by registered depth
    length =  math.sqrt(vector[0]*vector[0] + vector[1]*vector[1]+vector[2]*vector[2])
    vector[0] = vector[0] / length  *  depth
    vector[1] = vector[1] / length  *  depth
    vector[2] = vector[2] / length  *  depth
    return vector

cv.NamedWindow('Depth')
cv.NamedWindow('Video')
ind = 0
print('%s\nPress ESC to stop' % __doc__)


def get_depth(ind):
    return frame_convert.pretty_depth_cv(freenect.sync_get_depth(ind)[0])


def get_video(ind):
    return frame_convert.video_cv(freenect.sync_get_video(ind)[0])

def getDepthFromPixel(pix):
   return 100.0/(-0.0030711016*pix + 3.3309495161) 
i=0
while i==0:
    i=1
    #print(ind)
    try:
        depth = get_depth(ind)
        video = get_video(ind)
    except TypeError:
        ind = 0
        continue
    depth_matrix = freenect.sync_get_depth(ind)
    # first  dim: 480 
    # second dim: 480
    sum = 0
    index = 0
#    for i in range(480):
#    for ii in range(640):
#        val = getDepthFromPixel(depth_matrix[0][i][ii])
#        if (val<100000 and val > 10):
#            sum+=val
#            index +=1
#    if (index!=0):
#    print "Average: " + str( sum/index)
#    print "Number of pixels used: " + str(index) + " out of: " + str(480*640)
    
    #
    # make a 12*16 grid of average depth in the picture

    #
    picture = []
    projection = [[0 for i in range(30)] for ii in range(40)] # 40 x 50 ----- 10 cm / square
    print "Starting Processign"
    for iFrame in range(12):
        row = []
    for iiFrame in range(16):
        
        #loop [20*20] to get average
        sum = 0
            index = 0            
           for i in range(40):

            for ii in range(40):

                val = getDepthFromPixel(depth_matrix[0][iFrame*40+i][iiFrame*40+ ii])
                if (val<100000 and val > 10):
                    sum+=val
                    index +=1
        if (index > 40*40 /2):  # at least half of the points
                 row.append(int(sum/index))        
            vector = createVector(iiFrame*40+ii+20,iFrame*40+i+20, int(sum/index))
            print vector
            if(((vector[0])/10+30/2)>=0 and (((vector[0])/10+30/2))<30 and (vector[1])>0 and (40-((vector[1])/10))>0):
                if (math.fabs( height_of_kinect - vector[2])>math.fabs(projection[int(40-(vector[1])/10)][int((vector[0]/10+30/2))])):
                    projection[int((40-vector[1]/10))][int((vector[0]/10+30/2))] =int( height_of_kinect - vector[2])
        
        else:
            row.append(-index+0.1)
        #
        #


    picture.append(row)
    ind += 1    
    for y in range(12):    
    print picture[y]
    
#
# #   for i in range(480):
#    for ii in range(640):
#        if (getDepthFromPixel(depth_matrix[0][i][ii])>0):
#            vector = createVector(ii,i, getDepthFromPixel(depth_matrix[0][i][ii]))
#            if (i%50==0 and ii%50==0):
#                print vector  # works!!!
#        #does not work
#        if(((vector[0])/10+30/2)>=0 and (((vector[0])/10+30/2))<30 and (vector[1])>0 and (40-((vector[1])/10))>0):
#            if (math.fabs( height_of_kinect - vector[2])>math.fabs(projection[int(40-(vector[1])/10)][int((vector[0]/10+30/2))])):
#                projection[int((40-vector[1]/10))][int((vector[0]/10+30/2))] =int( height_of_kinect - vector[2])
#        
#        #if (vector[0]>0 and vector[0]<20*20 and vector[1]>0 and vector[1]<50*20):
#        #    projection[vector[1]/20][vector[0]/20] = height_of_kinect - vector[3]
    for i in range(40):
    print str(40*10 -i*10) + "cm: "+str(projection[i])
    cv.ShowImage('Depth', depth)

    cv.ShowImage('Video', video)


    if cv.WaitKey(10) == 27:
        break
    freenect.sync_stop()  # NOTE: Uncomment if your machine can't handle it
