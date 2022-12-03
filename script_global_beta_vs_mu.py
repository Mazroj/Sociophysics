#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random 

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

#Defining the creation of a new network
def nuevared(n,p):
  x = []
  for i in range(n):
    x.append(int(random.uniform(0,p)))
  return(x)

#Defining code to get data from results
def takedat(resultstotal,repetitions):
    qwtotal = []
    qwtotalprop =[]
    for i in range(repetitions):
        qw =[]
        qwprop= []
        for e in resultstotal[i]:
            q = max(e)
            qer = e[propaganda]
            qw.append(q)
            qwprop.append(qer)
        qwtotal.append(qw)
        qwtotalprop.append(qwprop)
    sigmaaa = []
    for i in range(repetitions):
        sigma=[]
        for j in range(len(qwtotal[0])):
            sig = abs(qwtotal[i][j] - qwtotalprop[i][j])
            sigma.append(sig)
        sigmaaa.append(sigma)
    grp=[]
    grpprop =[]
    sigmafin =[]
    for j in range(len(qwtotal[0])):
        suma= []
        sumprop =[]
        sumsigma=[]
        for i in range(len(qwtotal)):
            suma.append(qwtotal[i][j])
            sumprop.append(qwtotalprop[i][j])
            sumsigma.append(sigmaaa[i][j])
        me = np.mean(suma)
        meprop = np.mean(sumprop)
        grp.append(me)
        grpprop.append(meprop)
        ssigma = np.mean(sumsigma)
        sigmafin.append(ssigma)
    return grp, grpprop, sigmafin


# In[ ]:


n = input("Set the size of the global network:")       ## Size of network
p = input("Set the number of options:")          ## Number of options
t = 5000        ## Iteration time
propaganda = int(p*0.8)    ## Option exposed by external force
repetitions = 50


# In[ ]:


##Intensity of External force (probability)
datasigm = []
for intensity in (np.linspace(1/p,1,p)):
    x= nuevared(n,p)
    resultstotal = []
    for rep in range(repetitions):
      results= []
      for w in range(1,p+1):
          x = nuevared(n,p)
          for T in range(t):
              for i in range(n):
                  r = random.randint(0,n-1)
                  if intensity > random.uniform(0,1):
                    if abs(propaganda- x[i])<= w:
                      x[i] = propaganda
                  else:
                    d = (x[r] - x[i])
                    if abs(d) <= w:
                      x[i]=x[r]
          ree = cont(x,p)
          results.append(ree)
      resultstotal.append(results)
    grp, grpprop, sigmafin = takedat(resultstotal,repetitions)
    sigmafin1 = np.array(sigmafin)/n
    datasigm.append(sigmafin1)


df = pd.DataFrame(datasigm)

df.to_csv("data_global_beta_vs._mu.csv", index=False)
