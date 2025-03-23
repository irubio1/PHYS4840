#!/usr/bin/env python3.12

import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append('../')
import my_functions_lib as mfl


filename = 'NGC6341.dat'

## # Col.  9: F336W calibrated magnitude
## # Col. 15: F438W calibrated magnitude
## # Col. 27: F814W calibrated magnitude
## # Col. 33: membership probability

blue, green, red, probability = np.loadtxt(filename, usecols=(8, 14, 26, 32), unpack=True)


magnitude = blue
color     = blue - red


quality_cut = np.where( (red   > -99.) &\
					    (blue  > -99)  &\
					    (green > -99)  &\
					    (probability != -1))

#If the magnitude is -99, it means the data is missing or invalid, and -1 for probability means 
#it ensures that the membership probability is valid as
#a value of -1 might indicate that the probability is undefined or not calculated

acceptable_colors = color[quality_cut]
acceptable_magnitude = magnitude[quality_cut]

fig, ax = plt.subplots(figsize=(8,16))

plt.plot(acceptable_colors, acceptable_magnitude, "k.")
plt.gca().invert_yaxis()
plt.xlabel("Color: B-R", fontsize = 15)
plt.ylabel("Magnitude: B", fontsize = 15)
plt.title('Hubble Space Telescope Data for the\nGlobular Cluster NGC6341', fontsize=20)
plt.xlim(-2, 5)
plt.ylim(25,13.8)
plt.show()
plt.close()

#__________________________________________________________________________________________#

# Set dimensions of figure
fig, ax = plt.subplots(figsize=(8, 16))

membership_probability = probability[quality_cut]
#quality_cut here gives me all the VALID points of the membership probability (>-1)

scatter = ax.scatter(acceptable_colors, acceptable_magnitude, c=membership_probability, 
                     cmap='viridis', s=4, alpha=0.8)

# Add a color bar to show probability
cbar = plt.colorbar(scatter)
cbar.set_label('Membership Probability', fontsize=16)

# Invert the y-axis
plt.gca().invert_yaxis()

# Label the axes and title
plt.xlabel("Color: B-R", fontsize=20)
plt.ylabel("Magnitude: B", fontsize=20)
plt.title('Hubble Space Telescope Data for\nthe Globular Cluster NGC6341', fontsize=22)

# Set axis limits
plt.xlim(-2, 5)

# Show the plot
plt.show()
plt.close()