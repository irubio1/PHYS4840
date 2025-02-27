#!/usr/bin/python3.12
#####################################
#
# Class 12: Numerical Differentiation II
# Author: M Joyce
#
#####################################

import numpy as np
import matplotlib.pyplot as plt
from math  import tanh, cosh

import sys
sys.path.append('../')
import my_functions_lib as mfl

## compute the instantaneous derivatives
## using the central difference approximation
## over the interval -2 to 2

x_lower_bound = -2.0
x_upper_bound = 2.0

N_samples = 100

#####################
#
# Try different values of h
# What did we "prove" h should be
# for C = 10^(-16) in Python?
#
#######################
h = 10e-10 ## what goes here?

xdata = np.linspace(x_lower_bound, x_upper_bound, N_samples)

central_diff_values = []
for x in xdata:
	central_difference = ( mfl.f(x + 0.5*h) - mfl.f(x - 0.5*h) ) / h
	central_diff_values.append(central_difference)

## Add the analytical curve
## let's use the same xdata array we already made for our x values

analytical_values = []
for x in xdata:
	dfdx = mfl.df_dx_analytical(x)
	analytical_values.append(dfdx)


plt.plot(xdata, analytical_values, linestyle='-', color='black')
plt.plot(xdata, central_diff_values, "*", color="green", markersize=8, alpha=0.5)
plt.savefig('numerical_vs_analytic_derivatives.png')
plt.close()


"""
Q5: Assuming the functions and derivatives are of order unity (1), what is a
good guess for an appropriate value of h?
h = 10e-10

Q6: Once you have reproduced my figure on
GitHub, try h = 2, h = 1, and h = 1e-16

"""

#QUESTION 6

h = [2, 1, 1e-14]

x_lower_bound = -2.0
x_upper_bound = 2.0
N_samples = 100

xdata = np.linspace(x_lower_bound, x_upper_bound, N_samples)

central_diff_values_6 = []
analytical_values_6 = []

for i in h:
	h = i
	central_diff_values_6 = []
	analytical_values_6 = []

	for x in xdata:
		central_difference = ( mfl.f(x + 0.5*h) - mfl.f(x - 0.5*h) ) / h
		central_diff_values_6.append(central_difference)

		dfdx = mfl.df_dx_analytical(x)
		analytical_values_6.append(dfdx)

	plt.plot(xdata, analytical_values_6, linestyle='-', color='black', label = "Analytical graph")
	plt.plot(xdata, central_diff_values_6, linestyle='-', label = f"Central difference of h = {i}")

plt.xlabel("X data")
plt.ylabel("Differential value")
plt.title("Comparison between Analytical and Central Difference Differential")
plt.legend()
#plt.show()
plt.savefig("numerical_vs_multiple_analytic_derivatives.png")