# -*- coding: utf-8 -*-
"""
Created on Thu Jan 19 14:53:19 2023

@author: jahn39
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


def colAvrg(df):
    list_avrgs = []
    
    rows,cols = df.shape
    
    for i in range(cols):
        #print(r)
        sli = df.iloc[:,i]
        
        avrg = np.average(sli)
        list_avrgs.append(avrg)
    
    return list_avrgs



def colDevFromMean(df,d_avrgs):
    list_dev = []
    
    rows,cols = df.shape
    
    count = -1
    for i in range(rows):
        count = count + 1
        print(count)
        sli = df.iloc[count,:]
        
        one_row_devis = list(np.subtract(d_avrgs,sli))
            
        list_dev.append(one_row_devis)
    #shape should be each row is a frame, each column is a degree
    #430 frames/rows, 360 degrees/columns
    return list_dev

#Type in appropriate directory below
directory = ""
df = pd.read_csv(directory,index_col=0)

rows,cols = df.shape

degs = np.arange(0,360,1)
d_avrgs = colAvrg(df)

plt.plot(degs,d_avrgs)
plt.show()


sli = df.iloc[0,:]

devs = df

df_devs = df.T

new_header = df_devs.columns

x = df_devs.iloc[:, :].values
x = StandardScaler().fit_transform(x) # normalizing the features

#normalized radii
norm_radii = pd.DataFrame(x,columns=new_header)

#PCA

n_numb = 50
pca_radii = PCA(n_components=n_numb)
principalComponents_radii = pca_radii.fit_transform(x)


PC_labels = []
for i in range(n_numb):
    nb = i+1
    lb = 'PC ' + str(nb)
    PC_labels.append(lb)

PC_df = pd.DataFrame(data = principalComponents_radii, columns = PC_labels)


#Variation explained per principal component
pca_radii_val = list(pca_radii.explained_variance_ratio_)

x_n = np.arange(n_numb)
plt.figure(figsize=(12, 7)) 
plt.bar(x_n, pca_radii_val,align='center')
plt.xticks(x_n, PC_labels,rotation='vertical')
plt.ylabel('Variance explained')
plt.savefig('Variance explained.jpeg')
plt.show()


plt.rcParams.update({'font.size': 18})
plt.rcParams["figure.figsize"] = (20,15)
for i in range(8):
    name = i + 1
    PC = PC_df.iloc[:,i]    
    plt.plot(degs,PC,label = 'PC_'+str(name))
    

plt.xlabel('Degrees')
plt.ylabel('Radii length')
plt.legend()
plt.savefig("Top 8 pc modes.jpeg")
plt.show()



top8PCA = []
for i in range(8):
    PC = PC_df.iloc[:,i]
    top8PCA.append(PC)

t8p = pd.DataFrame(top8PCA)
print(t8p)
t8p.to_csv('Top 8 PCA modes.csv')