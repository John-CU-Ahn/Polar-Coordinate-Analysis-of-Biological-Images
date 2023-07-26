# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 16:27:14 2023

@author: jahn39
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns
from scipy.optimize import curve_fit

#Add appropriate directories below
dir_PCA = ""
dir_radii = ""
dir_avg = ""

df_PCA = pd.read_csv(dir_PCA, index_col = 0)
df_radii = pd.read_csv(dir_radii,index_col=0)
df_avg = pd.read_csv(dir_avg,index_col=0)
degs = np.arange(0,360,1)
xdata = degs

rows,cols=df_avg.shape

PC1 = df_PCA.iloc[0,:]
PC2 = df_PCA.iloc[1,:]
PC3 = df_PCA.iloc[2,:]
PC4 = df_PCA.iloc[3,:]
PC5 = df_PCA.iloc[4,:]
PC6 = df_PCA.iloc[5,:]
PC7 = df_PCA.iloc[6,:]
PC8 = df_PCA.iloc[7,:]

list_weights = []
for i in range(rows):
    print(i)
    avg_shape = df_avg.iloc[i,:]
    def func(x,a,b,c,d,e,f,g,h):
        return a*PC1 + b*PC2 + c*PC3 + d*PC4 + e*PC5 + f*PC6 + g*PC7 + h*PC8 + avg_shape
    
    ydata = df_radii.iloc[i,:]
    popt,pcov = curve_fit(func,xdata,ydata)
    print(popt)
    list_weights.append(popt)
    
weights = np.asarray(list_weights)
df_w = pd.DataFrame(weights)
df_f = df_w.T
df_f.to_csv("PC weights.csv")