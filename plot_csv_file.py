#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:51:10 2017

@author: chris
"""

#############################################################################
# Code to import a text file and plot it. Used to plot radio data for
# AST443 - Lab3 
#############################################################################

### Use numpy to load text
import numpy as np
### For plotting
import matplotlib.pyplot as plt
### For pi and other math operations
import math
### For finding local maximum and minimum
#from scipy.signal import argrelextrema

###Used to view an entire array without ...
np.set_printoptions(threshold=np.nan)

### Load text file for sulfur measurements
x, y = np.loadtxt('/Users/chris/Documents/astro_lab/lab3/inter190-160.csv', delimiter=',', skiprows=1, unpack=True)
### Change x from time to radians
x = np.arange(0,math.pi*30/180,(math.pi*30/180)/len(x))
### Adjust for altitude
x = x/np.cos(0.5585053606)
### Invert y and bring to zero
y = y**(-1)
baseline = (np.mean(y[0:120])+np.mean(y[250:500]))/2
y = y-baseline

### Plot y vs x
plt.plot(x,y)
plt.xlabel('Angle (rad)')
plt.ylabel('Amplitude')
### Change Baseline if needed
plt.title('Measured Fringes From The Sun (Baseline=30")')
plt.show()

### Measure the space between fringes to get a more accurate B_lambda
a1=  x[np.where(np.logical_and(y<1.6809449e-02,y>1.68094488e-02))]
b1 =x[np.where(np.logical_and(y<3.27082022e-02,y>3.27082020e-02))]
print 'B_Lambda =', (a1-b1)**(-1)

