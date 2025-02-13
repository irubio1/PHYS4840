#!/usr/bin/python3.8

import numpy as np
def my_function(vector):
	a = vector[0]
	b = vector[1]
	c = vector[2]

	return np.linalg.norm(vector)



#(1)
vector = [1,2,3]
print(my_function(vector))

# it prints 3.7416573867739413


#(2)
import my_functions_lib as mfl
vector = [1,2,3]
print(mfl.my_function(vector))


#It prints 3.7416573867739413 and I learned that numpy needs to be loaded in mfl instead of 
#just the file we're calling it to