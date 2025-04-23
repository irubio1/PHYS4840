#!/usr/bin/python3.8
#####################################
#
# Class 23: PDEs I: 3D Laplace Solver
# Author: Adapted by M Joyce from Mark Newman
#
#####################################
import numpy as np
import matplotlib.pyplot as plt

import os
import sys

sys.path.append(os.path.join("/home/irubio/PHYS4840_labs"))

import my_functions_lib as mfl


# Constants
N = 30             # Grid size (cube of size N x N x N)
h = 1               # Grid spacing
V = 1.0             # Voltage on the top face (z = 0)
target = 1e-8       # Convergence criterion

# Initialize the potential arrays
phi = np.zeros((N+1, N+1, N+1), dtype=float)
phinew = np.empty_like(phi)

# Apply boundary condition: top face (z = 0) at V, others at 0
phi[:,:,0] = V

# Iterative solution using Gauss-Seidel-like update
delta = 1.0
iteration = 0
while delta > target:
    iteration += 1
    phinew =phi+ mfl.laplacian_operator(phi, h,h,h)/6

    # Preserve boundary conditions
    phinew[:,:,0] = V
    phinew[:,:,N] = 0
    phinew[:,0,:] = 0
    phinew[:,N,:] = 0
    phinew[0,:,:] = 0
    phinew[N,:,:] = 0

    delta = np.max(np.abs(phi - phinew))
    phi, phinew = phinew, phi

    if iteration % 10 == 0:
        print(f"Iteration {iteration}, max delta = {delta:.2e}")


# Visualization: middle slice in z-direction
mid_z = N // 2
plt.figure(figsize=(6,5))
plt.imshow(phi[:,:,mid_z], origin='lower', cmap='inferno')
plt.colorbar(label='Potential $\Phi$')
plt.title(f"Midplane slice at z = {mid_z}")
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.show()