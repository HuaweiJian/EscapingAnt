# MATH1402 Python Project
# Blake Nielson SN: 17016395

# Import all required functions
from math import *
from random import *
from pos_ang_generator import *

# Read the Pythagorean triples and store data in variable
infile = open('triangle_triples.data', 'r')
pythagTriples = []
for line in infile:
	pythagTriplesloc = []
	strlist = line.split()
	for i in range(len(strlist)):
		pythagTriplesloc.append(float(strlist[i]))
	pythagTriples.append(pythagTriplesloc)
infile.close()

# Fix sample size N to be used for number of trials in code
N = 10

# Loop through each pythagorean triple
for ptriple in range(len(pythagTriples)):
	
	# Initialise variables for counters of each side
	x_side = 0
	y_side = 0
	hyp = 0
	
	# Loop through number of iterations N
	for i in range(N):
		
		# Need to generate a position and angle for ant
		[x,y,theta] = positionAngleGenerate(pythagTriples[ptriple])
		
		
