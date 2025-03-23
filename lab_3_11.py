#!/usr/bin/python3.12


#solve: x = 2-e^-x
from math import exp
import numpy as np
x = 1.0
"""
for i in range(10):
	x = 2-exp(-x)
	print(x)
"""

x =.5
print("QUESTION 2: FORM A")
#Form A: x = e^(1-x^2)
for i in range(50):
	x = exp(1.0-x**2)
	print(x)


print("QUESTION 2: FORM B")
#Form B: x = (1-lnx)^.5
for i in range(100):
	x = np.sqrt(1.0-np.log(x))
	print(x)