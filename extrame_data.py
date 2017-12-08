import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import math as mt
from scipy.optimize import curve_fit
from scipy.signal import argrelextrema

def import_data(path,txt,sle,alt):
    txt_name = path + '/' + txt
    data = np.loadtxt(txt_name)
    v_min = max(data[:,1])
    alt = alt/180.0*mt.pi
    data[:,0] = np.divide(np.linspace(0,sle,np.size(data[:,0])),mt.cos(alt))
    return data[:,0],-data[:,1]+v_min

def func(x,a,b,c,d):
    return a*np.exp(-b*(x-c)**2)+d

def data_plot(path_in,path_out,txt,slew,alt):
    a_data,v_data = import_data(path_in,txt,30,28.3)
    popt,pcov = curve_fit(func,a_data,v_data,bounds=([0,0,10,0],[2,100,25,1]))
    f_data = func(a_data,*popt)
    plt.figure()
    plt.plot(a_data,v_data,label='real')
    plt.plot(a_data,f_data,label='fit')
    plt.xlabel('Slew Angle [Degree]')
    plt.ylabel('Voltage Potantial [V]')
    plt.legend()
    plt.savefig(path_out+'/'+txt[:-4]+'.png')
    plt.close()
    return a_data,v_data,f_data

def local_extrame(a_data,v_data,f_data,a_range):
    d_data = v_data - f_data
    index = np.where((a_data>=a_range[0])*(a_data<=a_range[1]))
    index = index[0]
    in_max = argrelextrema(d_data, np.greater)
    in_max = in_max[0]
    in_min = argrelextrema(d_data, np.less)
    in_min = in_min[0]
    index_max = np.where((in_max>=min(index))*(in_max<=max(index)))
    index_min = np.where((in_min>=min(index))*(in_min<=max(index)))
    index_max = in_max[index_max[0]]
    index_min = in_min[index_min[0]]
    a_max = a_data[index_max]
    a_min = a_data[index_min]
    v_max = v_data[index_max]
    v_min = v_data[index_min]
    return [a_max,v_max],[a_min,v_min]

if __name__ == '__main__':
    path_in = 'C:/My Programs/Python27/PHY517/Lab3/txt_files'
    path_out = 'C:/My Programs/Python27/PHY517/Lab3/image_files'
    txt = 'inter170-145.txt'
    a_data,v_data,f_data = data_plot(path_in,path_out,txt,25,30.8)
    a_range = np.array([15,25])
    max_array,min_array = local_extrame(a_data,v_data,f_data,a_range)
    index = np.where((a_data>=a_range[0])*(a_data<=a_range[1]))
    plt.plot(max_array[0],max_array[1],'or')
    plt.plot(min_array[0],min_array[1],'ob')
    plt.plot(a_data[index[0]],v_data[index[0]])
    plt.plot(a_data[index[0]],f_data[index[0]])
    plt.xlabel('Slew Angle [Degree]')
    plt.ylabel('Voltage Potantial [V]')
    plt.title(txt[:-4])
    plt.savefig('C:/My Programs/Python27/PHY517/Lab3/ext_data/'+txt[:-4]+'.png')
    plt.close()
    np.savetxt('C:/My Programs/Python27/PHY517/Lab3/ext_data/'+txt[:-4]+'_ext_max.txt',max_array)
    np.savetxt('C:/My Programs/Python27/PHY517/Lab3/ext_data/'+txt[:-4]+'_ext_min.txt',min_array)
