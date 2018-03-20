"""
This module ...
"""
from math import *
from random import *

# parameters: (each) Pythagorean triple from file
# outputs: random point with a random angle
def posAngGenerate(triple):
	
	# Generate a random angle
	theta = random()*2.*pi
	
	# Get 2 non-hypotenuse sides from the input triple
	x_test = triple[0]
	y_test = triple[1]
	
	# Set initial condition of particle being inside triangle as false
	inside = True
	
	# Check whether point inside triangle
	while inside:
		
                # Generate a random point: random() outputs a number [0.0,1.0)
		x = random()*x_test
		y = random()*y_test
               		
		# This point is valid if it's inside the triangle constructed by triple
		if y < -1.* (y_test/x_test) * x + y_test:
                    inside = False
		
	return [x,y,theta]
	

