# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 14:02:41 2025

@author: G00397054@atu.ie
"""

# -*- coding: utf-8 -*-
"""
@author: Dan Koskiranta
"""

import numpy as np
import matplotlib.pyplot as plt

# Set up figure window & axes with 3D projection
fig = plt.figure(figsize=(16,12))
ax = fig.add_subplot(111, projection = '3d')
# Configure complex sinusoid parameters
# Frequency, Hz
f = 5              
# Sampling frequency, Hz
fs = 1000         
# Duration, s   
duration = 1       
# Total number of samples  
N = int(duration*fs) 
# Create an array with sample numbers 0 to N
n = np.arange(0, N)
# Create another array of discrete times n*T
nT = n/fs
# Put time on x-axis, sine on z-axis and cosine on y-axis
# Add code for x-axis
x = nT
# Add code for z-axis
z = np.sin(2*np.pi*f*n/fs)
# Add code for y-axis
y = np.cos(2*np.pi*f*n/fs)
# Plot the 3 axes & a grey line along the x-axis
ax.plot3D(x, y, z, 'steelblue', linewidth = 2)
ax.plot3D(x, [0]*n, z, color = 'violet', linewidth = 2, alpha = 0.5)
ax.plot3D(x, y, [0]*n, color = 'orange', linewidth = 2, alpha = 0.5)
ax.plot3D((-0.1, N/fs * 1.1), (0, 0), (0, 0), color = 'gray', linewidth = 2)
ax.set_axis_off()
#ax.view_init(30,45)
plt.show()