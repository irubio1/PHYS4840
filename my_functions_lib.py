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


def romberg(y_values, x_values, max_order):
    """
    Approximates the integral using Romberg's method for given y_values at given x_values.

    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        max_order (int): Maximum order (controls accuracy).

    Returns:
        float: The approximated integral.
    """
    R = np.zeros((max_order, max_order))
    a = x_values[0]
    b =x_values[-1]
    N = 1
    h = (b - a)/N

    # First trapezoidal estimate
    R[0, 0] = (h / 2) * (y_values[0] + y_values[-1])

    for i in range(1, max_order):
        N = 2**i#Remember: we are recomputing the integral with different N (and therefore h)
        h = (b - a) / N #Look at the github derivation for richardson extrapolation

        sum_new_points = sum(np.interp(a + k * h, x_values, y_values) for k in range(1, N, 2))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_new_points

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)

    return R[max_order - 1, max_order - 1]

#Trapezoidal rule with array data
def trapezoidal(y_values, x_values, N):
    """
    Approximates the integral using trapezoidal rule for given y_values at given x_values.
    
    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals.

    Returns:
        float: The approximated integral.
    """
    a = x_values[0] #first value
    b = x_values[-1] #last value
    h = (b-a)/N

    integral = (1/2) * (y_values[0] + y_values[-1]) * h  # First and last terms

    for k in range(1, N):
        xk = a + k * h  # Compute x_k explicitly
        yk = np.interp(xk, x_values, y_values)  # Interpolate y at x_k manually in loop
        integral += yk * h

    return integral

# Simpson's rule for array data
def simpsons(y_values, x_values, N):
    """
    Approximates the integral using Simpson's rule for given y_values at given x_values.

    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals (must be even).

    Returns:
        float: The approximated integral.
    """

    a = x_values[0]
    b = x_values[-1]
    h = (b-a)/N

    integral = y_values[0] + y_values[-1]# First and last y_value terms

    for k in range(1, N, 2):  # Odd indices (weight 4)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 4 * yk

    for k in range(2, N, 2):  # Even indices (weight 2)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 2 * yk

    return (h / 3) * integral  # Final scaling

def romberg_rule(f, a, b, max_order):
    """
    Approximates the integral using Romberg's method, leveraging the trapezoidal rule.

    Parameters:
        f (function): The function to integrate.
        a (float): Lower bound of integration.
        b (float): Upper bound of integration.
        max_order (int): Maximum order (controls accuracy).

    Returns:
        float: The approximated integral.
    """
    R = np.zeros((max_order, max_order))  # Create a Romberg table
    
    # First approximation using the trapezoidal rule
    R[0, 0] = trapezoidal_rule(f, a, b, 1)
    
    for i in range(1, max_order):
        N = 2**i  # Number of intervals (doubles each step)
        R[i, 0] = trapezoidal_rule(f, a, b, N)
        
        # Compute extrapolated Romberg values
        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)
    
    return R[max_order - 1, max_order - 1]  # Return the most refined estimate


def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)