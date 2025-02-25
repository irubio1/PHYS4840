import my_functions_lib as mfl
import numpy as np 
from math import cosh

def sech(x):
  return 1 / cosh(x)


x = np.linspace(-2,2,100)
h = 10**(-10)

dfx = []
#central Difference 
for i in x:
	df = (mfl.f(i+.5*h)-mfl.f(i-.5*h))
	dx = h

	dfx.append(df/dx)


print(f"Approximate derivative: {np.average(dfx)}")
print(f"Actual derivative: {sech(2*2)**2 - sech(2*-2)**2}")

