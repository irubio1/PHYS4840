#!/usr/bin/python3.12
import numpy as np

def f(x):
    return x**2  # Some function thats easy to integrate by hand and hence verify

# Number of points (n) for Gauss-Legendre Quadrature
n = 1000


# Compute the Gauss-Legendre Quadrature points (roots of the Legendre polynomial) and weights
roots, weights = np.polynomial.legendre.leggauss(n)


#print the roots and weights for the points
print(f"Roots: {roots}")
print(f"Weights: {weights}")

# Compute the integral approximation manually using a for loop
#iterating through each legendre polynomial

integral_approx = 0
exact_integral =2/3
for i in range(n):
    point = roots[i]
    weight = weights[i]

    #grab the root for this polynomial
    #grap the weight for this polynomial

    function_value = f(point)
    #Evaluate function at the root

    weighted_value = weight*function_value
    # Apply weight

    integral_approx = integral_approx + weighted_value
    # append to running sum




# Print final comparison
print("\nFinal Results:")
print(f"Approximated integral using Gauss-Legendre Quadrature: {integral_approx}")
print(f"Exact integral: {exact_integral}")
print(f"Error: {abs(integral_approx - exact_integral)}")


"""
for n = 10
Final Results:
Approximated integral using Gauss-Legendre Quadrature: 0.6666666666666663
Exact integral: 0.6666666666666666
Error: 3.3306690738754696e-16


for n = 1000
Final Results:
Approximated integral using Gauss-Legendre Quadrature: 0.6666666666665336
Exact integral: 0.6666666666666666
Error: 1.3300471835009375e-13

"""