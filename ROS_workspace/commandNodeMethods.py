def excavate():
	# excavation subroutine involves a circular digging pattern
	# first go to the starting point
	# turn on the auger
	# lower suspension to appropriate height
	# drive through circular waypoints for a discrete parametrizable number of times
	# lift suspension
	# stop auger


def setAugerSpeed(desiredSpeed);
	# smoothly changes auger speed from current to desired (0-255)
	increment = 1	
	
	if currentSpeed < desiredSpeed:
		while currentSpeed < desiredSpeed:
			#speed up
			currentSpeed  = currentSpeed + increment
			#publish currentSpeed here	
			
	elif currentSpeed > desiredSpeed:
		while currentSpeed > desiredSpeed:
			#slow down
			currentSpeed = currentSpeed - increment
			#publish currentSpeed here