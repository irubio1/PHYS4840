#!/usr/bin/python3.8
#####################################
#
# Class 26: Oddball integration
# Author: Mark Newman, modified by M Joyce
#
#####################################

from math import sqrt,log,cos,sin,pi
from random import random

Z = 79
e = 1.602e-19
E = 7.7e6*e
epsilon0 = 8.854e-12
a0 = 5.292e-11
sigma = a0/100 #

N = int(1e7)

def gaussian():
    r = sqrt(-2*sigma*sigma*log(1-random())) #Define radius
    theta = 2*pi*random() #Define theta
    x = r*cos(theta) #conversion to cartesian coordinates
    y = r*sin(theta) #conversion
    return x,y

count = 0
for i in range(N):
    x,y = gaussian()
    b = sqrt(x*x+y*y)
    if b<Z*e*e/(2*pi*epsilon0*E): #Reflection limit is Z*e*e/(2*pi*epsilon0*E
        count += 1

print(count,"particles were reflected out of",N)


"""
In comparison to the fortran compilation and exectution time, python is taking a REALLY long time
to run and do this computation
"""