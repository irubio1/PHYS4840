#!/usr/bin/python3.12
#####################################
#
# Class 12: Numerical Differentiation II
# Author: M Joyce
#
#####################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, CubicSpline

# some data
#x = np.array([0, 1, 2, 3, 4, 5])
x = np.arange(0, 101)
y = np.sin(x) 

# Define fine-grained x-values for interpolation
x_domain = np.linspace(min(x), max(x), 100000)

# Linear Interpolation
linear_interp = interp1d(x, y, kind='quadratic')
y_linear = linear_interp(x_domain)

# Cubic Spline Interpolation
cubic_spline = CubicSpline(x, y)
y_cubic = cubic_spline(x_domain)

# Plot the results
plt.figure(figsize=(8, 5))
plt.scatter(x, y, color='red', label='Data Points', zorder=3)
plt.plot(x_domain, y_linear, '--', label='Linear Interpolation', linewidth=2)
plt.plot(x_domain, y_cubic, label='Cubic Spline Interpolation', linewidth=2)
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear vs. Cubic Spline Interpolation')
plt.grid(True)
plt.show()

residuals = np.abs(y_linear - y_cubic)
"""
Q1: How does the smoothness of the two interpolation methods compare?
-  Smoothness is dependent on the number of x_values in the data we're interpolating. 
The greater the number of plotted points, the smoother and more fitting linear and cubic spline 
become.

Q2: What happens if you add more data points? Does one method improve more than the other?
-  Adding more data point increases the smoothness of both linear and cubic spline. 
*interpolate_q2.png attached to this problem

Q3: Try changing y values to represent a sinusoidal function. Which method approximates the function better?
- Cubic spline approximates the functio better
*interpolate_q3.png attached to this problem

Q4: Experiment with kind='quadratic' in interp1d. How does it compare to cubic splines?
- It's not exactly identical but it is extremely close and approximates sin very well.
*interpolate_q4.png attached to this problem
"""