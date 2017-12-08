#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 14:22:41 2017

@author: chris & crystal
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
###Used to view an entire array without ...
np.set_printoptions(threshold=np.nan)

#xdata = np.array([28.22,32.93,37.629,61.148,65.851,70.555])
#xdata = xdata*2
#sigma_x = np.array([0.94,.94,.94,.94,.94,.94])
#sigma_x = 2*sigma_x
xdata = np.array([63.32991469,65.38253268,73.9971596,116.5685227,129.1459469,129.7358448])
sigma_x = np.array([4.087788808,1.720592967,4.352777813,15.37787214,4.942839567,11.3741552])
ydata = np.array([0.4853,0.3765,0.2809,0.1606,0.1769,0.2055])
sigma_y = np.array([0.0204,0.0394,0.0269,0.0201,0.0142,0.0142])

def func(x,p1): # HERE WE DEFINE A SIN FUNCTION THAT WE THINK WILL FOLLOW THE DATA DISTRIBUTION
    return (abs(np.sin(x*p1*math.pi))/(math.pi*x*p1))

# Here you give the initial parameters for p0 which Python then iterates over
# to find the best fit
popt, pcov = curve_fit(func,xdata,ydata,p0=0.01,sigma=sigma_y) #THESE PARAMETERS ARE USER DEFINED

print 'alpha =', (popt) # This contains your two best fit parameters
perr = np.sqrt(np.diag(pcov))
print 'error =', (perr)
e1 = perr[0]
## Performing sum of squares
p1 = popt[0]

residuals = ydata - func(xdata,p1)
fres = sum(residuals**2)

print 'chi sqaure =', (fres) #THIS IS YOUR CHI-SQUARE VALUE!

xaxis = np.linspace(1,161,161) # we can plot with xdata, but fit will not look good 
curve_y = func(xaxis,p1)
plt.errorbar(xdata,ydata,xerr=sigma_x,yerr=sigma_y,fmt='.',label='Data')
plt.plot(xaxis,curve_y,'-',label='Sinc Fit: alpha = %.4f +/- %.4f' %(p1,e1))
plt.xlim(xmin=0,xmax=150)
plt.xlabel('$B_\lambda$')
plt.ylabel('Visibilty')
plt.title('Visibility vs Baseline')
plt.legend()
plt.show()

print 'V=0 at B_lamda=',xaxis[np.where(curve_y==np.min(curve_y))]
