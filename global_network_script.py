#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt
from timebudget import timebudget
from multiprocessing import Pool
import ipyparallel as ipp


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


# In[ ]:





# In[3]:


def simul_global_evol(tolerance,intensity):
    x = nuevared(size,options)
    for T in range(time):
        for i in range(size):
            r = random.randint(0,size-1)
            if intensity > random.uniform(0,1):
                if abs(propaganda- x[i])<= tolerance:
                    x[i] = propaganda
            else:
                d = (x[r] - x[i])
                if abs(d) <= tolerance:
                    x[i]=x[r]
    return(x)


# In[ ]:





# In[4]:


def run_simulation(ident):
    tolerance = np.linspace(1,options ,options )
    intensity = np.linspace(1/options,1,options)
    for inten in intensity:
        for tole in tolerance:
            x = simul_global_evol(tole,inten)
            df = pd.DataFrame(x)

            df.to_csv(f"Data_global_n/data_global_intensity_i{inten}_t{tole}_{ident}", index=False) 


# In[40]:



    


# In[5]:


#@timebudget
def run_simul(operation,input,pool):
    pool.map(operation,input)
    
    
    
#client_ids = ipp.Client()
#pool = client_ids[:]

size = 1000
options = 100
time = 5000
propaganda = 80
    
    
#processes_count = 10
#processes_pool = Pool(processes_count)
#input = range(10)

#run_simul(run_simulation, input, processes_pool)

    
processes_count = 15
input = range(20,50)
if __name__ == '__main__':
    processes_pool = Pool(processes_count)
    run_simul(run_simulation, input, processes_pool) 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


