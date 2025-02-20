#!/usr/bin/python3.12
import numpy as np
import time
import matplotlib.pyplot as plt


# Example usage with array data
def trapezoidal(y_values, x_values, N):
    """
    Approximates the integral using trapezoidal rule for given y_values at given x_values.
    
    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals.

    Returns:
        float: The approximated integral.
    """
    a = x_values[0] #first value
    b = x_values[-1] #last value
    h = (b-a)/N

    integral = (1/2) * (y_values[0] + y_values[-1]) * h  # First and last terms

    for k in range(1, N):
        xk = a + k * h  # Compute x_k explicitly
        yk = np.interp(xk, x_values, y_values)  # Interpolate y at x_k manually in loop
        integral += yk * h

    return integral


# Simpson's rule for array data
def simpsons(y_values, x_values, N):
    """
    Approximates the integral using Simpson's rule for given y_values at given x_values.

    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        N (int): Number of intervals (must be even).

    Returns:
        float: The approximated integral.
    """

    a = x_values[0]
    b = x_values[-1]
    h = (b-a)/N

    integral = y_values[0] + y_values[-1]# First and last y_value terms

    for k in range(1, N, 2):  # Odd indices (weight 4)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 4 * yk

    for k in range(2, N, 2):  # Even indices (weight 2)
        xk = a + k * h
        yk = np.interp(xk, x_values, y_values)
        integral += 2 * yk

    return (h / 3) * integral  # Final scaling


# Romberg integration for array data
def romberg(y_values, x_values, max_order):
    """
    Approximates the integral using Romberg's method for given y_values at given x_values.

    Parameters:
        y_values (array-like): The function values at given x points.
        x_values (array-like): The x values corresponding to y_values.
        max_order (int): Maximum order (controls accuracy).

    Returns:
        float: The approximated integral.
    """
    R = np.zeros((max_order, max_order))
    a = x_values[0]
    b =x_values[-1]
    N = 1
    h = (b - a)/N

    # First trapezoidal estimate
    R[0, 0] = (h / 2) * (y_values[0] + y_values[-1])

    for i in range(1, max_order):
        N = 2**i#Remember: we are recomputing the integral with different N (and therefore h)
        h = (b - a) / N #Look at the github derivation for richardson extrapolation

        sum_new_points = sum(np.interp(a + k * h, x_values, y_values) for k in range(1, N, 2))
        R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_new_points

        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4**j - 1)

    return R[max_order - 1, max_order - 1]


def timing_function(integration_method, x_values, y_values, integral_arg):
    """
    Times the execution of an integration method.

    Parameters:
        integration_method (function): The numerical integration function.
        x_values (array-like): The x values.
        y_values (array-like): The corresponding y values.
        integral_arg (int, optional): EITHER Number of intervals to use (Simpson/Trapz) OR the maximum order of extrapolation (Romberg).

    Returns:
        tuple: (execution_time, integration_result)
    """
    start_time = time.perf_counter()
    result = integration_method(y_values, x_values, integral_arg)
    end_time = time.perf_counter()
    
    return end_time - start_time, result



# Function to integrate
def function(x):
    return x * np.exp(-x)

# Precompute data for fair comparisons
x_data = np.linspace(0, 1, 100000000)  # High-resolution x values
y_data = function(x_data)

# Testing parameters
N = 10000# Number of intervals
max_order = 10 # Romberg's accuracy level

# Measure timing for custom methods
trap_time, trap_result = timing_function(trapezoidal, x_data, y_data, N)
simp_time, simp_result = timing_function(simpsons, x_data, y_data, N)
romb_time, romb_result = timing_function(romberg, x_data, y_data, max_order)

# True integral value
true_value = 0.26424111765711535680895245967707826510837773793646433098432639660507700851

# Compute errors
trap_error = np.abs(true_value - trap_result)
simp_error = np.abs(true_value - simp_result)
romb_error = np.abs(true_value - romb_result)

# Print results with error analysis
print("\nIntegration Method Comparison")
print("=" * 80) # why 80? https://peps.python.org/pep-0008/
print(f"{'Method':<25}{'Result':<20}{'Error':<20}{'Time (sec)':<15}")
print("-" * 80)
print(f"{'Custom Trapezoidal':<25}{trap_result:<20.8f}{trap_error:<20.8e}{trap_time:<15.6f}")
print(f"{'Custom Simpson\'s':<25}{simp_result:<20.8f}{simp_error:<20.8e}{simp_time:<15.6f}")
print(f"{'Custom Romberg':<25}{romb_result:<20.8f}{romb_error:<20.8e}{romb_time:<15.6f}")
print("=" * 80)


#plotting example.Sshowing how we can make a list, populate it and plot it

def function(x):
    #a function that does stuff
    return x/2, x**2

# Initialise lists
traps_array = []
simps_array = []
rombs_array = []
traps_time = []
simps_time = []
rombs_time = []
N_value_array = []



for N in [5, 100, 1000, 10000]:
    # Function to integrate
    def function(x):
        return x * np.exp(-x)

    # Precompute data for fair comparisons
    x_data = np.linspace(0, 1, 100000000)  # High-resolution x values
    y_data = function(x_data)

    # Testing parameters
    N = N# Number of intervals
    max_order = 10 # Romberg's accuracy level

    # Measure timing for custom methods
    trap_time, trap_result = timing_function(trapezoidal, x_data, y_data, N)
    simp_time, simp_result = timing_function(simpsons, x_data, y_data, N)
    romb_time, romb_result = timing_function(romberg, x_data, y_data, max_order)

    # True integral value
    true_value = 0.26424111765711535680895245967707826510837773793646433098432639660507700851

    # Compute errors
    trap_error = np.abs(true_value - trap_result)
    simp_error = np.abs(true_value - simp_result)
    romb_error = np.abs(true_value - romb_result)


    traps_array.append(trap_error)
    simps_array.append(simp_error)
    rombs_array.append(romb_error)
    traps_time.append(trap_time)
    simps_time.append(simp_time)
    rombs_time.append(romb_time)
    N_value_array.append(N)




    
#plot trap error vs. N
fig, ax = plt.subplots(3, figsize=(10,10))

# Trapezoidal Rule
ax[0].scatter(N_value_array, traps_array, color='blue', marker='x', s=80)
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].set_xlabel('N values (log scale)')
ax[0].set_ylabel('Trapezoidal Method Error (log scale)')
ax[0].set_title('Trapezoidal Rule error vs. N')

# Simpson's Rule
ax[1].scatter(N_value_array, simps_array, color='purple', marker='x', s=80)
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xlabel('N values (log scale)')
ax[1].set_ylabel('Simpson’s Method Error (log scale)')
ax[1].set_title('Simpson’s Rule error vs. N')

# Romberg Integration
ax[2].scatter(N_value_array, rombs_array, color='red', marker='x', s=80)
ax[2].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xlabel('N values (log scale)')
ax[2].set_ylabel('Romberg Integration Method Error (log scale)')
ax[2].set_title('Romberg Integration error vs. N')

plt.tight_layout()  # Adjust layout for better readability
plt.show()

#plot accuracy vs compute time
fig, ax = plt.subplots(3, figsize=(10,10))

#Trapezoidal Rule
ax[0].scatter(traps_time, traps_array, color='blue', marker='x', s=80)
ax[0].set_xscale('log')
ax[0].set_yscale('log')
ax[0].set_xlabel('Compute time (log scale)')
ax[0].set_ylabel('Trapezoidal Method Error (log scale)')
ax[0].set_title('Trapezoidal Rule error vs. Compute Time')

#Simpson's Rule
ax[1].scatter(simps_time, simps_array, color='purple', marker='x', s=80)
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xlabel('Compute time (log scale)')
ax[1].set_ylabel('Simpson’s Method Error (log scale)')
ax[1].set_title('Simpson’s Rule error vs. Compute Time')


# Romberg Integration
ax[2].scatter(rombs_time, rombs_array, color='red', marker='x', s=80)
ax[2].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xlabel('Compute Time (log scale)')
ax[2].set_ylabel('Romberg Integration Method Error (log scale)')
ax[2].set_title('Romberg Integration error vs. Compute Time')

plt.tight_layout()
plt.show()