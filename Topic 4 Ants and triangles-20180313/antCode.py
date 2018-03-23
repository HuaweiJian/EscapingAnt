"""
Source code from Huawei Jian for python coursework of UCL MATH1402.
"""

from math import *
from random import *
import matplotlib.pyplot as plt


def read_file():
    """
    *read file $triangle_triples.data into a string `inflie`
    *split the string, store triples of numbers(string casted) into 'trpls'
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
               	
         # point is valid if inside the triangle
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
    
    """

def monte_carlo(a,b):
    """
    parameters: two shorter sides of each triple 
    feature:compute N times: create random sides, accumulate the probs
    output: divide the sum by N to get average prob of the N trials
    """
    # container to hold sum of probs
    probs = 0.
    # trial number 
    N = 60000

    for i in range(N):
        x,y = random_pnt(a,b)
        probs += 1/(2*pi) * (pi/2 + atan2(x,b-y) + atan2(y,a-x)) 

    return probs/N
    

def plot(p):
    """
    *plot a histogram for distribution of triangles 
    """
    plt.hist(p, bins=30, edgecolor='tab:orange', linewidth=1.5)
    plt.title("Distribution of Pythagorean triangles over exit probability")
    plt.ylabel("Number of triangles")
    plt.xlabel("Exiting probability")
    plt.savefig("my_histogram.png")

		 
def  main():
    """ 
        *read all triples from the file into `trpls`
        *implement monte carlo method on each one
        *store results into `p`
        *get max/min from p, trace initial triple from indices
        *plot a histogram 
    """

    trpls = read_file()

    # holds all prob from the triples
    p = []
    
    for i in range(len(trpls)):
        a,b,c = trpls[i]
        p.append(monte_carlo(a,b)) 
            
    print p
    
    # get min and max values of probs and triples associated
    print "triple with max exit prob is",trpls[p.index(max(p))]
    print "with rob", max(p)

    print "triple with min exit prob is:",trpls[p.index(min(p))]
    print "with prob", min(p)

    plot(p)


main()

#print monte_carlo(3.,4.)
