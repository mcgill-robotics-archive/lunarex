print """# This is a prototype program to use the Kinect to create a map of a kinect's line of vision. It outputs a 2d array where the indexes are the coordinates (in 10cmx10cm squares) and the values are the predicted height with respect to the floor at that location. More precisely: the largest absolute value predicted by a depth pixell on that square, so it gives an upper bound with respect to the absolute value of the elevation difference. 

#Negative values are craters, small positive values are rocks, large positive values are walls. 
#Expect noise
# IF significant and consistent error:
# look at elevation if always off by constant value
# look at angle if off by varying values (for example, error gets worse as distance increases or even goes from positive error to negative error)
when floor close apears too high, increase the tilt_x_axis variable
"""
import freenect
import cv
import frame_convert
import math
from pylab import *
from numpy import *

#
# Variables
#

height = 460
width = 640
vertical_view_angle = 43 # in degrees
horizontal_view_angle = 57 # in degrees
vert_angle = vertical_view_angle * math.pi / 180# in rads
horiz_angle = horizontal_view_angle * math.pi / 180 # in rads
height_of_kinect =77 # cm
Xmid = width/2
Zmid = height/2
 
sobel_x = np.matrix('-1 0 1;-2 0 2; -1 0 1')
sobel_y = np.matrix('-1 -2 -1; 0 0 0; 1 2 1')
print sobel_x, sobel_y

tilt_x_axis =0.05#0.03 #math.pi/18 # in rads, tilt towards the ground is positive, straight ahead is 0 rad 
focalLength = 580 # in pixels
#
# minimum tilt on the x-axis seems to be about -0,57 rads
#

#def getFocalLength():
#	length = (height/2)/ (math.tan(vert_angle/2))
#	print length
#   	return length

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
	print "Starting..."

	depth_matrix = freenect.sync_get_depth(ind)
	print len(depth_matrix )
	print len(depth_matrix[0])
	##
	# determine the tilt about the x axis  
	# take vectors in a grid with 10 pixels in between vectors in order to determine the tilt. 
	# Method: find tilt angles that maximaze the number of vectors that are classified as being on the ground
	# only consider angles withing a limited range in order to prevent reaching an angle where wall vectors are considered
	# to be on the floor plane (for example, this could be a problem if the robot believes that it is tiled )
	##
	sample_vectors = []
	for y in range(10, 50): # ignore the low accuracy borders
		for x in range(10, 40): # ignore the low accuracy borders
			val = getDepthFromPixel(depth_matrix[0][y*height/50][x*width/50])
			if (val<100000 and val > 10):
		 		sample_vectors.append(createVector(x*width/50,y*height/50, int(val)))

	
	# easy, slow method to find the angle -- lots of ways to make this better and faster
	# for now, scan through angles [ -math.pi/4 ] (upwards) to [ math.pi/2 ] (facing directly down) 
	# keep the angle with the most points +- 5cm from the ground
	#print  sample_vectors[1]
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
	

		#print x_tilt
	#print  sample_vectors[1]
	print "angle:  "
	print best_angle 
	print " score: "
	print  best_score
	print len(sample_vectors)
	tilt_x_axis = best_angle

	#
	# remove all vectors in the vector list that are more than [threshold] cm off
	#
	#threshold = 	15 #cm
	#i=0
	#while (i<len(sample_vectors)):
	#	if ( math.fabs(getHeightOfVector(sample_vectors[i]) ) > threshold):
	#		sample_vectors.pop(i)
	#	i+=1
	#print "Vectors left: " 	
	#print len(sample_vectors)
	


	#
	# Find the angle that minimizes the total squared difference from the vector heights and the floor
	#
	domain_amplitude = 0.08
	step_size = 0.001
	x_tilt =best_angle- domain_amplitude
	score = 0
	best_score = 999999999999    # easy to do better
	best_angle = math.pi/2 # very bad angle, easy to see bugs
	
	while (x_tilt<=tilt_x_axis+ domain_amplitude):	

		score = 0
		
		for i in range(len(sample_vectors)):
			vector = adjustForTilt(sample_vectors[i], x_tilt)
			vector_height = math.fabs(getHeightOfVector(vector))
			score+=vector_height
		if (score<best_score):
			#print x_tilt, score
			#print "new high score!!"
			best_angle = x_tilt
			best_score = score

		x_tilt += step_size
	print "angle:  "
	print best_angle 
	print " score: "
	
	print  best_score
	print len(sample_vectors)
	tilt_x_axis = best_angle	
	

	
	#####
	##### other way to get angle----> dot product #####################################################################
	#####
	sample_vectors = []
	for y in range(10, 50): # ignore the low accuracy borders
		for x in range(25, 26): # ignore the low accuracy borders
			val = getDepthFromPixel(depth_matrix[0][y*height/50][x*width/50])
			if (val<100000 and val > 10):
		 		sample_vectors.append(createVector(x*width/50,y*height/50, int(val)))

	#print sample_vectors 
	plausible_angles =[]
	for i in range(len(sample_vectors)):
		vect1 = sample_vectors[i]
		vect1_len = math.sqrt(vect1[1]**2+vect1[2]**2)
		for ii in range(20,21):#len(sample_vectors)):		
			if (i==ii):
				continue			
			vect2 = sample_vectors[ii]

			diff = [0, vect1[1] - vect2[1], vect1[2] - vect2[2]]
			vect2_len = math.sqrt(vect2[1]**2+vect2[2]**2)
			#print diff[1]
			#print vect1, vect2, diff
			diff_len = math.sqrt(diff[1]**2+diff[2]**2)
			dot_product = (diff[1]*vect2[1]) + (diff[2]*vect2[2])
			angle =  math.acos(dot_product/ (diff_len*vect2_len)) 
			#print diff[1], angle			
			plausible_angles.append(angle)
	#plausible_angles.sort()
	print plausible_angles
	print len(plausible_angles)/2
	print plausible_angles[len(plausible_angles)/2]
	print tilt_x_axis

	##########################################################################################################	

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
		

		#


	ind += 1    

    	for i in range(40):
		print str(40*10 -i*10) + "cm: "+str(projection[i])	
	print str("      " )+str([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])

    	figure(1)
    	imshow(projection, interpolation='nearest')	
    	grid(True)




	#
	#	
	#
	sobel_filter = [[0 for i in range(30)] for ii in range(40)]
	for y in range(1, len(sobel_filter )-1):
		for x in range(1,len(sobel_filter[0])-1):

			subset = np.matrix(  [   
			[ projection[y-1][x-1], projection[y-1][x], projection[y-1][x+1]  ],  
			[ projection[y][x-1],   projection[y][x],   projection[y][x+1]    ],
  			[ projection[y+1][x-1], projection[y+1][x], projection[y+1][x+1]  ]   
			]  )

			variance_x =sum(np.fabs( subset*sobel_x))
			varience_y =sum(np.fabs(subset*sobel_y))

			variance = math.sqrt(variance_x**2 + varience_y**2)
			if (variance>230):
				variance = 300
			else:
				variance = 0
			sobel_filter[y][x] = int( variance)

#    	for i in range(40):
#		
#		print str(40*10 -i*10) + "cm: "+str(sobel_filter[i])	
#


	figure(2)
	imshow(sobel_filter, interpolation='nearest')	
	show()




	if cv.WaitKey(10) == 27:
		break
    	freenect.sync_stop()  # NOTE: Uncomment if your machine can't handle it


