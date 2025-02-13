#!/usr/bin/python3.12

import numpy as np
import matplotlib.pyplot as plt
import sys
import my_functions_lib as mfl 

filename = 'NGC6341.dat'

blue, green, red = np.loadtxt(filename, usecols=(8, 14, 26), unpack=True)

magnitude = blue
color     = blue - red

plt.plot(color, magnitude, "ko")
#plt.show()
#plt.close()

plt.savefig('terrible_figure.png')

