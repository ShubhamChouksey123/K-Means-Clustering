#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


'''
function that check that our solution is reached a stagnent value 
by checking that each the distance betwen the new Centroid and the old Centroid
'''  
def SteadStatereached(Centroid, prevCentroid, k):
    for i in range (k):
        for j in range (len(Centroid[0])):
            if(abs(Centroid[i][j] - prevCentroid[i][j]) > 0.05):
                return True
    return False


# In[3]:


'''
function that assigns labels to each data point by finding its distances with all CEntoids and assigning it in the cluster 
with minimum distance
'''  
def findNewLabel(Centroid, k, X):
    labels = [0]*len(X)
    for i in range(len(X)):
        a = 0
        b = 0
        for j in range(len(Centroid[0])):
            a += pow(abs(Centroid[0][j] - X[i][j]), 2)
            b += pow(abs(Centroid[1][j] - X[i][j]), 2)
        if(a > b):
            labels[i] = 1
    return labels


# In[4]:


def findnewCentroid(lebels, X, rows , cols):
    a = [0]*cols
    b = [0]*cols
    count = 0
    for i in range(len(X)):
        if(labels[i] == 0):
            count = count+1
            for j in range(cols):
                a[j] += X[i][j]
        else:
            for j in range(cols):
                b[j] += X[i][j]
    
    for j in range(cols):
        if(count != 0):
            a[j] = a[j]/count
        if(len(X) - count != 0):
            b[j] = b[j]/(len(X) - count)
        
    Centroid = []
    Centroid.append(a)
    Centroid.append(b)
    return Centroid


# In[5]:


if __name__ == "__main__" : 
  
    df = pd.read_csv("cancer.csv", usecols = ["radius_mean", "texture_mean",  "perimeter_mean",	"area_mean",	
        "smoothness_mean",	"compactness_mean",	"concavity_mean",	"concave points_mean",	"symmetry_mean",	
        "fractal_dimension_mean",	"radius_se",	"texture_se",	"perimeter_se",	"area_se",	"smoothness_se",	
        "compactness_se",	"concavity_se",	"concave points_se",	"symmetry_se",	"fractal_dimension_se",	
        "radius_worst",	"texture_worst",	"perimeter_worst",	"area_worst",	"smoothness_worst",	"compactness_worst",	
        "concavity_worst",	"concave points_worst",	"symmetry_worst",	"fractal_dimension_worst" ])

    X = df.iloc[:, ].values
    
    X = X.astype(float)

    X = np.array(X)
    k  = 2 
    
    Centroid = []
    for i in range(k):
        Centroid.append(X[i])
    Centroid = np.array(Centroid)
    # we have made a array of size 2 * 30 containing the centroids 
    
    rows = k
    cols = len(Centroid[0])
    
    prevCentroid = [[float('inf')]*cols]*rows 
    itr = 0
    MaxItr = 100
    labels =[0]*len(X)
    
    while itr < MaxItr and SteadStatereached(Centroid, prevCentroid, k):
        itr = itr +1
        labels = findNewLabel(Centroid, k, X) 
        prevCentroid = Centroid
        Centroid = findnewCentroid(labels, X, rows, cols)
    
    
    colors = ["g.", "r. ", "c." , "b.", "k.", "o."]

    for i in range(len(X)):
        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 7)

    print("Corrdinates of Centroid are :")
    for i in range(k):
        print("(", Centroid[i][0] ," , ",Centroid[i][1], " )" )
        plt.scatter(Centroid[i][0], Centroid[i][1], c = "#1a1a2e", marker="x", s = 100)

    count = 0    
    for i in range(len(labels)):
        if labels[i] == 0:
            count = count+1 

    print("Number of points in Cluster 1 and 2 are : ", count ," & ", len(X)-count , "respectively")    
    plt.xlabel("Radius_Mean")
    plt.ylabel("Texture_Mean")
    plt.show()


# In[ ]:




