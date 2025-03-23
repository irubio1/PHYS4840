#!/usr/bin/python3.12
#####################################
#
# Class 13: Matrices and Linear algebra 
# Author: M Joyce
#
#####################################
import numpy as np
from numpy import array,empty

A = np.array([ [2,1,4,1], 
			[3,4,-1,-1], 
			[1,-4,1,5], 
			[2,-2,1,3] ],float)

vector = np.array([-4,3,9,7],float)

## dimension 
N = len(vector)

for m in range(N):

	## first, divide by the diagonal element
	divisor = A[m,m]

	## divide every entry in row m by the divisor
	A[m,:] /= divisor

	## the above is shorthand for this operation:
	## A[m,:] = A[m,:]/divisor

	##anything we do to the matrix we must do to the vector:
	vector[m] /= divisor

	## now subtract multipls of the top row from the lower rows
	## to zero out rows 2,3 and 4
	for i in range(m+1, N): ## note that we start from the second row: m+1

		## because the first row now has 1 in the upper-left corner,
		## the factor by which we have to multiply the first row to subtract
		## it from the second is equal to the value in the first entry
		## of the second row
		multiplication_factor = A[i,m] 

		## now we must apply this operation to the entire row 
		## AND vector, as usual 
		A[i,:]    -= multiplication_factor*A[m,:]
		vector[i] -= multiplication_factor*vector[m] 


print('the upper diagonal version of A is: \n', A)

## Write the next part of this program:
##  how do we solve the system of equations now that we have
##  an upper-diagonal matrix?

## you may consult example 6.1 in your textbook if you need help


z = vector[3]
y = vector[2]-A[2,3]*z
x = vector[1]-A[1,2]*y-A[1,3]*z
w = vector[0]-A[0,1]*x-A[0,2]*y-A[0,3]*z

print("W is: ", w)
print("y is: ", y)
print("x is: ", x)
print("z is: ", z)

answers = np.array([w,x,y,z])
solution = np.array((A*answers))

if np.all(solution == vector):
	print(f"The solution is correct")

	