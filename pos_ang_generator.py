# Import required functions
from math import *
from random import *

A = [5., 12., 13.]

# Function to check if point is within given triangle
def checkPosition(xi,yi,X,Y):
	if xi < X and yi < -1.*(Y/X)*xi+Y:
		return True
	else:
		return False

# Write function that generates a position and angle
def positionAngleGenerate(triple):
	
	# Establish random angle
	theta = random()*2.*pi
	
	# Establish variables for x and y extremes of triangle
	X = triple[0]
	Y = triple[1]
	
	# Set initial condition of particle being inside triangle as false
	inside = True
	
	# Check whether point inside triangle
	while inside:
		
		# Generate Random point
		x = random()*X
		y = random()*Y
		
		# Determine if inside
		if x<X and y<-1.*(Y/X)*x+Y:
			inside = False
		
	return [x,y,theta]
	
print(positionAngleGenerate(A))
