# EscapingAnt
A more generalised version of Question #613 from Project Euler

Problem: On each one in a set of Pythagorean triangles, from anywhere an ant starts off, and attempts to leave the triangle.
All possible positiosn within the triangle, All possible directions of moving on are equiprobable.
what is the probability that the ant leaves the triangle along its longest side?

Steps:
1.Read the Pythagorean triples from the file $triangle_triples.data
2.(a)
For EACH Triple,Repeat N times:
    *randomly generate a position (x, y) and a angle theta.
    *find the exit side of the ant starting in (x,y) and moving in the angle theta
    *use counters to record the frequency of the ant leaving from the hypotenuse
    *divide the frequency by N, we get the probability.
3.find the triangles for which the probability of exiting through hypotenuse is the smallest and the greatest，give value and triples associated
4.Check if result changes when increasing the sample size N.
5.Check, when N is large enough, the probability of triangle(3,4,5) converge to 0.3916721504.
6.Report a histogram showing how the Pythagorean triangles in $triangle_triples.data are distributed over the different exit probabilities.

