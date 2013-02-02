import freenect
import cv
import frame_convert
import math
from pylab import *


#
# Variables
#

height = 460
width = 640
vertical_view_angle = 43 # in degrees
horizontal_view_angle = 57 # in degrees
vert_angle = vertical_view_angle * math.pi / 180# in rads
horiz_angle = horizontal_view_angle * math.pi / 180 # in rads
height_of_kinect =79 # cm
Xmid = width/2

Zmid = height/2
 
tilt_x_axis =0#math.pi/7 # in rads, tilt towards the ground is negative, straight ahead is 0 rad 

#
#
#

def getFocalLength():
	length = (height/2)/ (math.tan(vert_angle/2))
	print length
    	return length

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
def adjustForTilt(vector):
	# tilt about the x-axis
	vector[1] = vector[1]*math.cos(tilt_x_axis )+vector[2]* -1*math.sin(tilt_x_axis )# y-adjustement
	vector[2] = vector[1]*math.sin(tilt_x_axis )+vector[2]*math.cos(tilt_x_axis )# z-adjustement	
	
	return vector
def get_depth(ind):
    	return frame_convert.pretty_depth_cv(freenect.sync_get_depth(ind)[0])


def get_video(ind):
    	return frame_convert.video_cv(freenect.sync_get_video(ind)[0])

def getDepthFromPixel(pix):
   	return 100.0/(-0.0030711016*pix + 3.3309495161) 


ind = 0
i=0

cv.NamedWindow('Depth')
cv.NamedWindow('Video')

while i==0:
	print "Starting..."
	i=1

	try:

        	depth = get_depth(ind)
        	video = get_video(ind)
	except TypeError:
		ind = 0
		print "error!!!!"


	depth_matrix = freenect.sync_get_depth(ind)
	


    	projection = [[0 for i in range(30)] for ii in range(40)]
 	print "Starting Processing"
 	for iFrame in range(height):
		if(iFrame %2 !=0):
			continue

		for iiFrame in range(width):
			if(iiFrame %2 !=0):
				continue



			val = getDepthFromPixel(depth_matrix[0][iFrame][iiFrame])
			if (val<100000 and val > 10):
				vector = createVector(iiFrame,iFrame, int(val))
				vector = adjustForTilt(vector)
				print vector
				if(((vector[0])/10+30/2)>=0 and (((vector[0])/10+30/2))<30 and (vector[1])>0 and (40-((vector[1])/10))>0):
					if (math.fabs( height_of_kinect - vector[2])>math.fabs(projection[int(40-(vector[1])/10)][int((vector[0]/10+30/2))])):
						projection[int((40-vector[1]/10))][int((vector[0]/10+30/2))] =int( height_of_kinect - vector[2])
		

		#


	ind += 1    

    	for i in range(40):
		print str(40*10 -i*10) + "cm: "+str(projection[i])	
	print str("      " )+str([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])

    	figure(1)
    	imshow(projection, interpolation='nearest')	
    	grid(True)
    	show()





	if cv.WaitKey(10) == 27:
		break
    	freenect.sync_stop()  # NOTE: Uncomment if your machine can't handle it


