#!/usr/bin/python3.8

import numpy as np
import matplotlib.pyplot as plt
from math import tanh


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

def distance_modulus(d):
	distance_modulus = 5*np.log10(d/10)

	return distance_modulus
		

def format_axes(ax):
    ax.tick_params(axis='both', which='major', labelsize=14, length=6, width=1.5)  # Larger major ticks
    ax.tick_params(axis='both', which='minor', labelsize=12, length=3, width=1)    # Minor ticks
    ax.minorticks_on()  # Enable minor ticks


def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])


def simpsons_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("n must be even for Simpson's Rule")
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    return (h/3) * (y[0] + 4*np.sum(y[1:n:2]) + 2*np.sum(y[2:n-1:2]) + y[-1])

"""
Remember that for integration we can use:

import numpy a np

# Number of points (n) for Gauss-Legendre Quadrature
n = 1000

legendre_roots, weights = np.polynomial.legendre.leggauss(n)
integral_approx = 0

for i in range(n):
    point = legendre_roots[i]
    weight = weights[i]
    function_value = f(point)
    
    weighted_value = weight*function_value
    integral_approx = integral_approx + weighted_value

print(integral_approx)
    
for error:
	error = np.abs(exact_integral - integral_approx)

"""


def f(x):
	f = 1+1/2*tanh(2*x)
	return f


	#derivative = sec^2(2x)