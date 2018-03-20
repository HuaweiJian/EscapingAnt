"""
Source code from Huawei Jian for python coursework of UCL MATH1402.
"""

from math import *
from random import *


def read_file():
    """
    Read all Pythagorean triples from $triangle_triples.data into a list `trpls`
    """    
    infile = open('triangle_triples.data', 'r')
    trpls = []
    for line in infile:
            trpl = []
            trpl = map(float, line.split())
            trpls.append(trpl)
    infile.close()
    return trpls


def random_pnt(a,b):
    """
    parameter: two shorter sides of (each) Pythagorean triple from file
    output: generated random point within the triangle
    """		
    inside = True
    while inside:	
        # random() outputs a number [0.0,1.0)
	x = random()* a
	y = random()* b
               	
         # This point is valid if it's inside the triangle
        if y < -1.* (b/a) * x + b:
            inside = False
    return [x,y]


    """       
            A\
            |.\
            |  \
         b  | . \ c
            |  . \ 
            | P....O
            |  . . \
            |  .  . \
            C__.____.B
               Q  a
    return true if the ant leaves via the hypotenuse  
    """

def monte_carlo(a,b):
    """
    parameters: one triple 
    outputs: 
    """
    N = 60000    
    probs = 0.
    
    for i in range(N):
        x,y = random_pnt(a,b)
        probs += 1/(2*pi) * (pi/2 + atan2(x,b-y) + atan2(y,a-x)) 
    return probs/N
    
		 
def  main():

    trpls = read_file()
    all_probs = []
    
    for i in range(len(trpls)):
        a,b,c = trpls[i]
        all_probs.append(monte_carlo(a,b)) 
            
    
    #get min and max values of probs and triples associated
    max_index, max_prob = max(enumerate(all_probs))
    print "max:",trpls[max_index], max_prob

    min_index, min_prob = min(enumerate(all_probs))
    print "min:",trpls[min_index], min_prob 



main()
print monte_carlo(3.,4.)
