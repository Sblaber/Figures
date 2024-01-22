# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Get started with interactive Python!
# Supports Python Modules: builtins, math,pandas, scipy 
# matplotlib.pyplot, numpy, operator, processing, pygal, random, 
# re, string, time, turtle, urllib.request
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp
from scipy import integrate

# Parameters
m = 0.1  # mass
gamma = 1  # damping coefficient
k_B = 1.0  # Boltzmann constant
T = 1.0  # temperature
dt = 0.01  # time step
total_time = 10.0  # total simulation time

# Initial conditions
v0 = 0.0  # initial velocity
t_values = np.arange(0, total_time, dt)
v_values = np.zeros_like(t_values)
x_Brownian = np.zeros_like(t_values)

# Numerical solution using Euler method
for i in range(1, len(t_values)):
    xi = np.random.normal(0, np.sqrt(2 * gamma * k_B * T * dt))
    v_values[i] = v_values[i - 1] + (-gamma * v_values[i - 1] + xi) * dt / m
    x_Brownian[i] = x_Brownian[i-1] + gamma**(-1.0)*xi*dt

x = integrate.cumtrapz(v_values,t_values,initial = 0)
# Plotting the results
plt.plot(t_values, x,'k', label='Position Underdamped')
plt.plot(t_values, x_Brownian,'r--', label='Position Brownian')

plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()
plt.show()
