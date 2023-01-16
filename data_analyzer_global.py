#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[ ]:


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

#Defining mean value of values between list
#This function is defined to obtain the mean value of numbers in the same position in diferent lists
def meansize(listadelistas):
    mean_final = []
    for columns in range(len(listadelistas[0][0])):
        mean_rows = []
        for rows in range(len(listadelistas[0])):
            suma_rep = 0
            for rep in range(len(listadelistas)):
                suma_rep += listadelistas[rep][columns][rows]
            meanv = suma_rep/len(listadelistas)
            mean_rows.append(meanv)
        mean_final.append(mean_rows)
    return mean_final


# In[ ]:


options = 10
propaganda = 8
intensity = np.linspace(1/options,1,options)
tolerance = np.linspace(1,options ,options )

total_smax = []
total_sprop =[]
total_sigma = []
for ident in range(50):
    smax_data = []
    sprop_data = []
    sigma_data = []
    for inten in intensity:
        smaxdata_per_tolerance = []
        spropdata_per_tolerance = []
        sigmadata_per_tolerance = []
        for tole in tolerance:
            df = pd.read_csv(f'Data_global_n100/data_global_intensity_i{inten}_t{tole}_{ident}')
            df1 = df.to_numpy().tolist()
            count_nodes_option = cont(np.transpose(df1)[0],options)
            smax, sprop, sigma = smax_sprop_sigma(count_nodes_option,propaganda)
            smaxdata_per_tolerance.append(smax)
            spropdata_per_tolerance.append(sprop)
            sigmadata_per_tolerance.append(sigma)
        smax_data.append(smaxdata_per_tolerance)
        sprop_data.append(spropdata_per_tolerance)
        sigma_data.append(sigmadata_per_tolerance)
    total_smax.append(smax_data)
    total_sprop.append(sprop_data)
    total_sigma.append(sigma_data)

    
smax_mean = meansize(total_smax)
sprop_mean = meansize(total_sprop)
sigma_mean = meansize(total_sigma)
        
    
df_smax = pd.DataFrame(smax_mean)
df_smax.to_csv("smax_data_n100_p10.csv", index=False)

df_sprop = pd.DataFrame(sprop_mean)
df_sprop.to_csv("sprop_data_n100_p10.csv", index=False)

df_sigma = pd.DataFrame(sigma_mean)
df_sigma.to_csv("sigma_data_n100_p10.csv", index=False)

