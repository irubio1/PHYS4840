#!/usr/bin/env python3.12

import numpy as np
import matplotlib.pyplot as plt
import sys


load_file = '/home/irubio/PHYS4840_labs/MIST_v1.2_feh_m1.75_afe_p0.0_vvcrit0.4_HST_WFPC2.iso.cmd'

## I want columns 14 and 18 for the filters
log10_isochrone_age_yr, F606, F814,\
logL, logTeff, phase= np.loadtxt(load_file, usecols=(1,14,18,6,4,22), unpack=True, skiprows=14)


#############################################
#
# this file actually contains many isochrone models, and we
# only need one. Deciding which is a physics question. 
# We know Globular Clusters are very old, so let's try
# an isochrone with age around 12 or 13 billion years.
# First, we will need to load the age column and make sure
# it is on the correct scale. Log or linear?
#
##############################################
age_Gyr_1e9 = (10.0**log10_isochrone_age_yr)/1e9 	## should be the same as 10**9.
age_Gyr_10 = (10.0**log10_isochrone_age_yr)/10.**9 	## should be the same as 10**9.
age_Gyr = age_Gyr_1e9

## we only want to use the model(s) that fall in this age range
age_selection = np.where((age_Gyr > 12) & (age_Gyr <= 13.8)) 
## this should extract only one isochrone

color_selected = F606[age_selection]-F814[age_selection]
magnitude_selected = F606[age_selection]
###########################################
#
# Now let's plot the isochrone. Let's do this
# in terms of LogL vs Teff (HRD) AS WELL AS
# in the HST filter system (CMD)
#
# Let's convert log(Teff) to its unlogged form:
# 
###########################################

Teff = 10.0**logTeff

################################
#
# NOTE that we have already changed the size 
# of the color and magnitude arrays above using
# np.where()
#
# Therefore, we must adjust LogL, Teff arrays
# to be the same size as well, otherwise
# the indices selected by np.where() will
# not align correctly 
#
################################
Teff_for_desired_ages =  Teff[age_selection]
logL_for_desired_ages =  logL[age_selection]

############################################
#
# we now have the equal-sized arrays
#	color_selected
#   magnitude_selected
#   Teff_for_desired_ages
#   logL_for_desired_ages
#
# But we want to perform some additional data cleaning. 
# There is a quantity in the iso.cmd file called "phase."
# This indicates the evolutionary phase of the model. 
# We are only interested in the earlier evolution, so we can
# clean our data by removing phase indices above 4.
#
################################################


### First, we have to truncate the "phase" array
# so that it is the same size and has the same
# index coordinates as the other arrays to which
# we have applied age selection:
phases_for_desired_age = phase[age_selection]

desired_phases = np.where(phases_for_desired_age <= 3)


## now, we can restrict our equal-sized arrays by phase
cleaned_color = color_selected[desired_phases]
cleaned_magnitude = magnitude_selected[desired_phases]
cleaned_Teff = Teff_for_desired_ages[desired_phases]
cleaned_logL = logL_for_desired_ages[desired_phases]

###############################################
#
# Check that all of these arrays are the same length!
# Plotting will fail otherwise
#
################################################
print("lengths of processed arrays: ", len(cleaned_color),\
									   len(cleaned_magnitude),\
									   len(cleaned_Teff),\
									   len(cleaned_logL) )



#########################################
#
# This plotting code should produce a 
# BEAUTFIUL, two-panel figure showing
# the SAME DATA SET, but rendered in two different
# sets of coordinates: The left is a color-magnitude diagram, 
# in observational coordinates (HST filters), and 
# the left is a theoretical Hertzsprung-Russel diagram,
# in raw physical units (temperature, luminosity)
#
###########################################

fig, axes = plt.subplots(1, 2, figsize=(8, 6))  # 2:1 aspect ratio per panel

# First panel: Color-Magnitude Diagram
axes[0].plot(cleaned_color, cleaned_magnitude, 'go', markersize=2, linestyle='-', label='color-mag')
axes[0].invert_yaxis()
axes[0].set_xlabel('Color', fontsize=15)
axes[0].set_ylabel('Magnitude', fontsize=15)
#axes[0].set_xlim(7500, 2800)

# Second panel: Theoretical Isochrone
axes[1].plot(cleaned_Teff, cleaned_logL, 'go', label='isochrone theoretical')
axes[1].invert_xaxis()
axes[1].set_xlabel('Teff (K)', fontsize=15)
axes[1].set_ylabel('logL', fontsize=15)
axes[1].set_xlim(7500, 2800)

fig.tight_layout()
#plt.ylim(-3,4)
plt.savefig('compare_isochrones.png')
plt.close()

filename = '/home/irubio/PHYS4840_labs/NGC6341.dat'

## # Col.  9: F336W calibrated magnitude
## # Col. 15: F438W calibrated magnitude
## # Col. 27: F814W calibrated magnitude
## # Col. 33: membership probability
## but Python indexes from 0, not 1!

blue, green, red, probability = np.loadtxt(filename, usecols=(8, 14, 26, 32), unpack=True)

magnitude = blue
color     = blue - red

quality_cut = np.where( (red   > -99.) &\
					    (blue  > -99)  &\
					    (green > -99)  &\
					    (probability != -1))
 
print("quality_cut: ", quality_cut )


fig, ax = plt.subplots(figsize=(8,16))

plt.plot(color[quality_cut], magnitude[quality_cut], "k.", markersize = 4, alpha = 0.2)
plt.gca().invert_yaxis()
plt.xlabel("Color: B-R", fontsize=20)
plt.ylabel("Magnitude: B", fontsize=20)
plt.title('Hubble Space Telescope Data for\nthe Globular Cluster NGC6341', fontsize=22)
plt.xlim(-2, 5)
plt.ylim(25,13.8)
#plt.show()
plt.savefig("NCGdat_plot")
plt.close()

fig, axes = plt.subplots(1, 3, figsize=(14, 6))  # 3 panels side by side

def format_axes(ax):
    ax.tick_params(axis='both', which='major', labelsize=14, length=6, width=1.5)  # Larger major ticks
    ax.tick_params(axis='both', which='minor', labelsize=12, length=3, width=1)    # Minor ticks
    ax.minorticks_on()  # Enable minor ticks

# First panel: Isochrone in color/magnitude coordinates
axes[0].plot(cleaned_color, cleaned_magnitude, 'go', markersize=2, linestyle='-')
axes[0].invert_yaxis()
axes[0].set_xlabel('Color', fontsize=18)
axes[0].set_ylabel('Magnitude', fontsize=18)
format_axes(axes[0])

# Second panel: Isochrone in theoretical coordinates
axes[1].plot(cleaned_Teff, cleaned_logL, 'mo')
axes[1].invert_xaxis()
axes[1].set_xlabel('Teff (K)', fontsize=18)
axes[1].set_ylabel('logL', fontsize=18)
axes[1].set_xlim(7500, 2800)
format_axes(axes[1])

# Third panel: HST Data for globular cluster
axes[2].plot(color[quality_cut], magnitude[quality_cut], "k.", markersize=4, alpha=0.2)
axes[2].invert_yaxis()
axes[2].set_xlabel("Color: B-R", fontsize=18)
axes[2].set_ylabel("Magnitude: B", fontsize=18)
axes[2].set_title('Hubble Space Telescope Data for\n the Globular Cluster NGC6341', fontsize=16)
axes[2].set_xlim(-2, 5)
axes[2].set_ylim(25, 13.8)
format_axes(axes[2])

plt.tight_layout()
plt.savefig("three_panel_CMD_figure.png", dpi=300)
plt.close()





#_________________________________-----------------------------_______________________________

#Assums NGC 6341 is 8.63 kiloparsecs (kpc) away

import my_functions_lib as mfl


d_kpc = 8.63
d_pc = d_kpc * 1000

distance_modulus = mfl.distance_modulus(d_pc)

#14.680053978576048

load_file = '/home/irubio/PHYS4840_labs/MIST_v1.2_feh_m1.75_afe_p0.0_vvcrit0.4_HST_WFPC2.iso.cmd'

log10_isochrone_age_yr, F606, F814,\
logL, logTeff, phase= np.loadtxt(load_file, usecols=(1,14,18,6,4,22), unpack=True, skiprows=14)

age_Gyr_1e9 = (10.0**log10_isochrone_age_yr)/1e9
age_Gyr = age_Gyr_1e9

age_selection = np.where((age_Gyr > 12) & (age_Gyr <= 13.8)) 

color_selected = F606[age_selection]-F814[age_selection]
magnitude_selected = F606[age_selection]

Teff = 10.0**logTeff
Teff_for_desired_ages =  Teff[age_selection]
logL_for_desired_ages =  logL[age_selection]

phases_for_desired_age = phase[age_selection]
desired_phases = np.where(phases_for_desired_age <= 3)

## now, we can restrict our equal-sized arrays by phase
cleaned_color = color_selected[desired_phases]
cleaned_magnitude = magnitude_selected[desired_phases]
cleaned_Teff = Teff_for_desired_ages[desired_phases]
cleaned_logL = logL_for_desired_ages[desired_phases]

filename = '/home/irubio/PHYS4840_labs/NGC6341.dat'

## # Col.  9: F336W calibrated magnitude
## # Col. 15: F438W calibrated magnitude
## # Col. 27: F814W calibrated magnitude
## # Col. 33: membership probability
## but Python indexes from 0, not 1!

blue, green, red, probability = np.loadtxt(filename, usecols=(8, 14, 26, 32), unpack=True)

magnitude = blue
color     = blue - red

quality_cut = np.where( (red   > -99.) &\
					    (blue  > -99)  &\
					    (green > -99)  &\
					    (probability != -1))
 
print("quality_cut: ", quality_cut )


fig, ax = plt.subplots(figsize=(8, 8))  # Single panel

def format_axes(ax):
    ax.tick_params(axis='both', which='major', labelsize=14, length=6, width=1.5)  # Larger major ticks
    ax.tick_params(axis='both', which='minor', labelsize=12, length=3, width=1)    # Minor ticks
    ax.minorticks_on()  # Enable minor ticks

# Plot HST Data
ax.plot(color[quality_cut], magnitude[quality_cut], "k.", markersize=4, alpha=0.2, label='HST Data (NGC6341)')

# Plot Isochrone model
ax.plot([i for i in cleaned_color], [k+distance_modulus for k in cleaned_magnitude], 'go', markersize=2, linestyle='-', label='Isochrone Model')

# Axis settings
ax.invert_yaxis()
ax.set_xlabel('Color', fontsize=18)
ax.set_ylabel('Magnitude', fontsize=18)
ax.set_title('Comparison of Isochrone Model and HST Data', fontsize=16)
ax.set_xlim(0.2,2.5)
ax.set_ylim(25,10)
format_axes(ax)
ax.legend(fontsize=14, loc='best')

plt.tight_layout()
#mvplt.show()
plt.savefig("overlay.png", dpi=300)
plt.close()


### Not a very great model ###