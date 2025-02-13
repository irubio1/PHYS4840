#!/usr/bin/python3.12

import numpy as np
import matplotlib.pyplot as plt
import my_functions_lib as mfl

#define x values
x = np.linspace(0,10,100)
y = mfl.y(x)


# (1) make a linear plot of y vs x

plt.plot(y, x,linestyle='-', color = 'blue', linewidth=5)
plt.title("Linear plot of y vs x")
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.grid(True) ## turn on/off as needed
plt.show()
plt.close()

# (2) make a log-log plot of y vs x
plt.plot(x,y, linestyle='-', color='red', linewidth=5)
plt.title("Log-log plot of y vs x")
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.xscale('log')  # Set x-axis to log scale
plt.yscale('log')  # Set y-axis to log scale
plt.grid(True) ## turn on/off as needed
plt.show()
plt.close()

# (3) make a plot of log(x) vs log(y)
logx = np.log10(x)
logy = np.log10(y)
plt.plot(logx, logy, linestyle='-', color='purple', linewidth=5)
plt.title("Plot of log(x) vs log(y)")
plt.xlabel('My x-axis')
plt.ylabel('My y-axis')
plt.grid(True) ## turn on/off as needed
plt.show()
plt.close()
