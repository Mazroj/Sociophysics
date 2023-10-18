#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


#Defining the creation of a new network
def nuevared(size,options):
    x = []
    for i in range(size):
        x.append(int(random.uniform(0,options)))
    return(x)

# Defining counting function
def cont(x,p):
    dat = []
    for j in range(p):
      s = 0
      for i in x:
        if j == i: 
          s += 1
      dat.append(s)
    return(dat)


#This Function give the Smax, the S of propaganda and sigma
def smax_sprop_sigma(mean_result_per_tolerance,propaganda):
    smax = np.max(mean_result_per_tolerance)
    sprop = mean_result_per_tolerance[propaganda]
    sigma = abs(smax - sprop)
    return smax, sprop, sigma

    


# In[ ]:


def simul_global_evol(tolerance,intensity,options):
    x = nuevared(size,options)
    T = 0
    while T < time:
        
        for i in range(size):
            r = random.randint(0,size-1)
            if intensity > random.uniform(0,1):
                if abs(propaganda- x[i])<= tolerance:
                    x[i] = propaganda
                else:
                    d = (x[r] - x[i])
                    if abs(d) <= tolerance:
                        x[i]=x[r]
                        
        crit = np.unique(np.array(x))
        
        df = pd.DataFrame(x)

        df.to_csv(f"Data_global_n/data_global_intensity_i{inten}_t{tole}_{ident}", index=False) 
        
        
        
        if len(crit) == 1:
            break
        T += 1
    return


# In[ ]:


tolerance = 23
intensity = 0.5
size = 1000
options = 100
time = 10000
propaganda = 80

simul_global_evol(tolerance,intensity, options)

