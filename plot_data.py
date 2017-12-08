import os
import sys
import numpy as np
import math as mt
import matplotlib.pyplot as plt

def create_list(path,extenstions):
    file_list = [fn for fn in os.listdir(path) if any(fn.endswith(ext) for ext in extenstions)]
    return file_list

def data_plot(path_in,path_out,txt_list):
    n = 0
    for txt in txt_list:
        file_name = path_in+ '/' +txt
        sle = float(input('Please input slew angle for '+txt+' (degree):\n'))
        alt = float(input('Please input altitude angle for '+txt+' (degree):\n'))
        alt = alt/180.0*mt.pi
        data = np.loadtxt(file_name)
        data[:,0] = np.divide(np.linspace(0,sle,np.size(data[:,0])),mt.cos(alt))
        data_min = min(-data[:,1])
        plt.figure()
        plt.plot(data[:,0],-data[:,1]-data_min)
        plt.xlabel('Slew Angle [Degree]')
        plt.ylabel('Voltage Potantial [V]')
        plt.title(txt[:-4])
        plt.savefig(path_out+'/'+txt[:-4]+'.png')
        plt.close()
        n+=1
    return 'Totally plots %d file(s)' %n
