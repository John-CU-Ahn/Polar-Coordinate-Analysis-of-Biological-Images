# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 15:02:26 2023

@author: jahn39
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def roLine(series, window):
    le = len(series)
    
    sli = int((window-1)/2)
    beg_window = pd.Series(series[0:sli])
    
    sli_e = le-sli + 1
    end_window = pd.Series(series[sli_e:])
    
    a = pd.Series(series)
    
    win_list = pd.concat([end_window,a,beg_window])
    
    
    new_list = []
    norm_i = sli
    for i in range(le):
        norm_i = norm_i + 1
        
        b = int(norm_i-(window-1)/2)
        e = int(norm_i+(window-1)/2)
        
        avrg = win_list[b:e].mean()
        new_list.append(avrg)
    
    if window == 0:
        new_list = series
    
    return new_list

def repRoLine(series, window, repeat):
    y = series
    for i in range(repeat):
        y = roLine(y,window)
    new_list = y
    
    if window == 0:
        new_list = series
    
    return new_list

#Add directory of PC weights
directory = ""
df = pd.read_csv(directory,index_col=0)

rows, cols = df.shape

y1 = df.iloc[0,:]
y2 = df.iloc[1,:]
y3 = df.iloc[2,:]
y4 = df.iloc[3,:]

y1 = repRoLine(y1, 10, 3)
y2 = repRoLine(y2, 10, 3)
y3 = repRoLine(y3, 10, 3)
y4 = repRoLine(y4, 10, 3)

y5 = df.iloc[4,:]
y6 = df.iloc[5,:]
y7 = df.iloc[6,:]
y8 = df.iloc[7,:]

y5 = repRoLine(y5, 10, 3)
y6 = repRoLine(y6, 10, 3)
y7 = repRoLine(y7, 10, 3)
y8 = repRoLine(y8, 10, 3)

x = np.arange(0,cols,1)

plt.plot(x,y1,alpha=0.75,label="PC 1")
plt.plot(x,y2,alpha=0.75,label="PC 2")
plt.plot(x,y3,alpha=0.75,label="PC 3")
plt.plot(x,y4,alpha=0.75,label="PC 4")
plt.legend()
plt.savefig("PC1-4.jpg")
plt.show()


plt.plot(x,y5,color = 'tab:brown', alpha=0.75,label="PC 1")
plt.plot(x,y6,color = 'tab:gray',alpha=0.75,label="PC 2")
plt.plot(x,y7,color = 'tab:cyan',alpha=0.75,label="PC 3")
plt.plot(x,y8,color = 'tab:pink',alpha=0.75,label="PC 4")
plt.legend()
plt.savefig("PC5-8.jpg")
plt.show()





