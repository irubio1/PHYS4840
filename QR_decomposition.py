#!/usr/bin/python3.12
#####################################
#
# Class 14: Matrices and Linear algebra 
# Author: M Joyce
#
#####################################

'''
by importing and using the QR decomposition 
algorithm in my_functions_lib.py:
1) Find Q and R
2) Confirm that Q is orthogonal
3) Confirm that R is upper triangular
4) Confirm that the matrix A introduced in eigenvalues.py
can indeed be reconstructed by the dot product 
of matrices Q and R
'''

import my_functions_lib as mfl
import numpy as np

#1 FIND Q AND R

A = np.array([ [2, -1, 3,],\
			   [-1, 4, 5], 
			   [3,  5, 6] ],float)

Q, R = mfl.qr_decomposition(A)

print("The matrix for Q is:\n", Q)
print("The matrix for R is:\n", R)

A_dot = np.dot(Q,R)

print("The matrix for A is:\n", A_dot)

#2 Conform Q is orthogonal
Q_T = np.linalg.matrix_transpose(Q)

orthagonality = np.round(np.dot(Q, Q_T))

identity = [ [1, 0 , 0],\
			 [0, 1, 0],
			 [0, 0 , 1]]

if np.all(orthagonality == identity):
	print("Q is orthogonal")

#3 Confirm that R is upper triangular
print(R)
print("R is upper triangular")

#r Conformation

A_dot = np.round(np.dot(Q,R))

if np.all(A_dot == A):
	print("The matrix made from the dot product of Q and R is:\n", A_dot, "\n is equal to the original vector given in eigenvalues.py\n", A)
