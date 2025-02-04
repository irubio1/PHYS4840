#!/usr/bin/python3.8

import numpy as np

def my_function(vector):
	a = vector[0]
	b = vector[1]
	c = vector[2]

	return np.linalg.norm(vector)


def Catlan_number(n):
	if n == 0:
		return 1
	else:
		return ((4*n-2)/(n+1))*Catlan_number(n-1)


def greatest_common_divisor(m,n):
	if n == 0:
		return m
	else:
		return greatest_common_divisor(n,(m%n))

def y(x):
	y = 2.0*x**3.0
	return y
