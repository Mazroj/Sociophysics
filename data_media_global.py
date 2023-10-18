#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd


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


total_smax = []
total_sprop =[]
total_sigma = []

sample = 10
total_sigma = []
total_smax = []
total_sprop = []
for ident in range(sample):
    df = pd.read_csv(f'prefinal_data/sigma_data_n100_p10_rep{ident}.csv')
    dfm = pd.read_csv(f'prefinal_data/smax_data_n100_p10_rep{ident}.csv')
    dfp = pd.read_csv(f'prefinal_data/smax_data_n100_p10_rep{ident}.csv')
    df1 = df.to_numpy()
    dfm1 = dfm.to_numpy()
    dfp1 = dfp.to_numpy()
    total_smax.append(dfm1)
    total_sigma.append(df1)
    total_sprop.append(dfp1)
    
    
    
smax_mean = meansize(total_smax)
sprop_mean = meansize(total_sprop)
sigma_mean = meansize(total_sigma)

df_smax = pd.DataFrame(smax_mean)
df_smax.to_csv(f"smax_data_n100_p10.csv", index=False)

df_sprop = pd.DataFrame(sprop_mean)
df_sprop.to_csv(f"sprop_data_n100_p10.csv", index=False)

df_sigma = pd.DataFrame(sigma_mean)
df_sigma.to_csv(f"sigma_data_n100_p10.csv", index=False)

