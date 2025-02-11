#!/usr/bin/python3.12

####################################################
#
# Author: M Joyce
#
####################################################
import time
import numpy as np
import sys
import pandas as pd

### where is this file located for you?
### be careful with file organization!!
filename = '/home/irubio/PHYS4840_labs/NGC6341.dat'

###################################################
#
# testing np.loadtxt()
#
###################################################
"""
put the action you want to time between the
star and end commands
"""

start_numpy = time.perf_counter()


blue, green, red, probability = np.loadtxt(filename,\
                 usecols=(8, 14, 26, 32), unpack=True)
print("len(green): ", len(green))


end_numpy  = time.perf_counter()

print('Time to run loadtxt version: ', end_numpy-start_numpy, ' seconds')



###################################################
#
# testing custom parser
#
###################################################
start_parser = time.perf_counter()
filename = '/home/irubio/PHYS4840_labs/NGC6341.dat'

blue, green, red, probability = [], [], [], []
with open(filename, 'r') as file: 
    for line in file:
        if line.startswith('#'):
            continue

        columns = line.split()

        blue.append(float(columns[8]))
        green.append(float(columns[14]))
        red.append(float(columns[26]))
        probability.append(float(columns[32]))



    blue = np.array(blue)
    green = np.array(green)
    red = np.array(red)

    print("len(green): ", len(green))



end_parser  = time.perf_counter()

print('Time to run custom parser version: ', end_parser-start_parser, ' seconds')


###################################################
#
# testing pandas
#
###################################################
start_pandas = time.perf_counter()

filename = '/home/irubio/PHYS4840_labs/NGC6341.dat'
df = pd.read_csv(filename, sep = r'\s+', comment = "#")


blue = df[df.columns[8]]
green = df[df.columns[14]]
red = df[df.columns[26]]

print("len(green): ", len(green))


end_pandas  = time.perf_counter()

print('Time to run pandas version: ', end_pandas-start_pandas, ' seconds')


#len(green):  158219
#Time to run loadtxt version:  0.5650400779995834  seconds
#len(green):  158219
#Time to run custom parser version:  0.7573225299993283  seconds
#len(green):  158218
#Time to run pandas version:  1.0918542339995838  seconds