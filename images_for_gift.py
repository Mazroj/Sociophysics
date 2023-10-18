#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


for T in range(10000)
    df = pd.read_csv(f'Data_global_gift/data_global_time{T}')
    df1 = df.to_numpy().tolist()
    
    
    plt.figure(figsize =(6,5))
    plt.hist(df1,bins = options)
    plt.xlabel('Opinion')
    plt.ylabel('Frecuency')
    plt.xlim(0,100)
    plt.ylim(0,500)
    plt.savefig(f'animation_global_n1000_p100/simul_glo_n1000_p100_t{T}.png')
    plt.close()


# In[ ]:




