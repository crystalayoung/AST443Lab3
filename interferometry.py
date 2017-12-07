#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:42:44 2017

@author: crystalyoung
"""

import numpy as np
import matplotlib.pyplot as plt
import math

from scipy.optimize import minimize

## Import text file data
#text_file = np.loadtxt('single_dish_sat2.txt')
## Get y-axis data and invert it
#y = (text_file[:,1])**(-1)
## These next few variables are used to bring the bottom limit of y to 0.0
#avg_y = np.mean(y[0:5])
##avg2 = np.mean(y[160:182])
##avg = [avg_y, avg2]
##avg = np.mean(avg)
#y = y - avg_y
## The x-values from the text file
#x = text_file[:,0]
## Change the range of x into radians and not time
#a = np.arange(0, (5*math.pi/36), (5*math.pi/36)/len(x)) # 30 degrees in radians is pi/6 radians
##
### Angle determined from Navy website provided on GitHub
#theta = math.pi/4 #radians
### new x value that is scaled to account for elevation differences
#x = a / math.cos(theta)
#
## plot x and y
#plt.plot(x,y)

## Visibility


##-------------------------------
## Import text file data
#text_file = np.loadtxt('inter165-135pt2.txt')
## Get y-axis data and invert it
#y = (text_file[:,1])**(-1)
## These next few variables are used to bring the bottom limit of y to 0.0
#avg_y = np.mean(y[0:15])
#avg2 = np.mean(y[35:46])
#avg = [avg_y, avg2]
#avg = np.mean(avg)
#y = y - avg
## The x-values from the text file
#x = text_file[:,0]
### Change the range of x into radians and not time
#a = np.arange(0, (math.pi/6), (math.pi/6)/len(x)) # 30 degrees in radians is pi/6 radians
##
### Angle determined from Navy website provided on GitHub
#theta = 0.50963614 #radians
### new x value that is scaled to account for elevation differences
#x = a / math.cos(theta)
##
##
### plot x and y
#plt.plot(x,y)
#
#plt.show()
#
####-------------------------------
## Import text file data
#text_file = np.loadtxt('inter170-145.txt')
## Get y-axis data and invert it
#y = (text_file[:,1])**(-1)
## These next few variables are used to bring the bottom limit of y to 0.0
#avg_y = np.mean(y[0:12])
#avg2 = np.mean(y[34:39])
#avg = [avg_y, avg2]
#avg = np.mean(avg)
#y = y - avg
## The x-values from the text file
#x = text_file[:,0]
### Change the range of x into radians and not time
#a = np.arange(0, (5*math.pi/36), (5*math.pi/36)/len(x))#
### Angle determined from Navy website provided on GitHub
#theta = 0.53756141 #radians
### new x value that is scaled to account for elevation differences
#x = a / math.cos(theta)
##
##
### plot x and y
#plt.plot(x,y)
#
#plt.show()

#-------------------------------
# Import text file data
#text_file = np.loadtxt('inter175-145.txt')
## Get y-axis data and invert it
#y = (text_file[:,1])**(-1)
## These next few variables are used to bring the bottom limit of y to 0.0
#avg_y = np.mean(y[0:15])
#avg2 = np.mean(y[40:46])
#avg = [avg_y, avg2]
#avg = np.mean(avg)
#y = y - avg
## The x-values from the text file
#x = text_file[:,0]
### Change the range of x into radians and not time
#a = np.arange(0, (math.pi/6), (math.pi/6)/len(x))##
### Angle determined from Navy website provided on GitHub
#theta = 0.5462881 #radians
### new x value that is scaled to account for elevation differences
#x = a / math.cos(theta)
##
##
### plot x and y
#plt.plot(x,y)
#
#plt.show()

#-------------------------------
## Import text file data
#text_file = np.loadtxt('inter180-150.txt')
## Get y-axis data and invert it
#y = (text_file[:,1])**(-1)
## These next few variables are used to bring the bottom limit of y to 0.0
#avg_y = np.mean(y[0:16])
#avg2 = np.mean(y[36:44])
#avg = [avg_y, avg2]
#avg = np.mean(avg)
#y = y - avg
## The x-values from the text file
#x = text_file[:,0]
### Change the range of x into radians and not time
#a = np.arange(0, (math.pi/6), (math.pi/6)/len(x)) # 30 degrees in radians is pi/6 radians
##
### Angle determined from Navy website provided on GitHub
#theta = 0.5550147 #radians
### new x value that is scaled to account for elevation differences
#x = a / math.cos(theta)
##
##
### plot x and y
#plt.plot(x,y)
##
#plt.show()
##-------------------------------
## Import text file data
#text_file = np.loadtxt('inter190-160.txt')
## Get y-axis data and invert it
#y = (text_file[:,1])**(-1)
## These next few variables are used to bring the bottom limit of y to 0.0
#avg_y = np.mean(y[0:12])
#avg2 = np.mean(y[25:35])
#avg = [avg_y, avg2]
#avg = np.mean(avg)
#y = y - avg
## The x-values from the text file
#x = text_file[:,0]
### Change the range of x into radians and not time
#a = np.arange(0, (math.pi/6), (math.pi/6)/len(x)) # 30 degrees in radians is pi/6 radians
##
### Angle determined from Navy website provided on GitHub
#theta = 0.5585054 #radians
### new x value that is scaled to account for elevation differences
#x = a / math.cos(theta)
##
##
### plot x and y
#plt.plot(x,y)
#
#plt.show()

##-------------------------------
## Import text file data
#text_file = np.loadtxt('inter195-165.txt')
## Get y-axis data and invert it
#y = (text_file[:,1])**(-1)
## These next few variables are used to bring the bottom limit of y to 0.0
#avg_y = np.mean(y[0:17])
#avg2 = np.mean(y[29:32])
#avg = [avg_y, avg2]
#avg = np.mean(avg)
#y = y - avg
## The x-values from the text file
#x = text_file[:,0]
### Change the range of x into radians and not time
#a = np.arange(0, (math.pi/6), (math.pi/6)/len(x)) # 30 degrees in radians is pi/6 radians
##
### Angle determined from Navy website provided on GitHub
#theta = 0.5585054 #radians
### new x value that is scaled to account for elevation differences
#x = a / math.cos(theta)
##
##
### plot x and y
#plt.plot(x,y)
#
#plt.show()

#-------------------------------
#-------------------------------
#-------------------------------
#-------------------------------
#-------------------------------
#-------------------------------
#-------------------------------
######## FIT THE SINC FUNCTION!!!

blambda = [28.22, 32.93, 37.63, 61.15, 65.85, 70.55]
sigma_blambda = [0.94, 0.94, 0.94, 0.94, 0.94, 0.94]

v = [0.4853, 0.3765, 0.2809, 0.1606, 0.1769, 0.2055]
sigma_v = [0.0204, 0.0394, 0.0269, 0.0201, 0.0142, 0.0142]

alpha = 0.02077199 # angular diameter of the Sun
#alpha_max = 
#alpha_min = 

x = np.arange(0, 90, 0.01)
y = (((abs(np.sin(math.pi*alpha*x)))/(x*math.pi*alpha)))
#y = ((0.8087003*(abs(np.sin(math.pi*alpha*x)))/(x*math.pi*alpha))) + 0.026995221

#y = []
#for i in x:
#    new = (
#    y = np.append(new, y)


plt.subplot()
plt.errorbar(blambda, v, xerr = sigma_blambda, yerr = sigma_v, fmt=',')
plt.title("Plot of Visibility vs. Baseline Length")
plt.xlabel("$B_\lambda$")
plt.ylabel("Visibility Amplitude")
plt.xlim(15,85)
plt.plot(x, y)
plt.show()

