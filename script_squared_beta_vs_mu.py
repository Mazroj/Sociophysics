#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import random

# Defining counting function
def cont(x,p):
    dat = []
    for j in range(p):
      s = 0
      for i in x:
        for k in i:
            if j == k: 
              s += 1
      dat.append(s)
    return(dat)


# In[3]:


#Defining the creation of a new network
def nuevared2d(n,p):
  x = []
  for i in range(n):
    y = []
    for j in range(n):
        y.append(int(p*np.random.uniform(0,1)))
    x.append(y)
  return(x)


# In[4]:


def dat2d(p,datamatfin):
    resultp = []
    for s in range(p):
        smax= 0
        for i in range(len(datamatfin)):
            for j in range(len(datamatfin[0])):
                if datamatfin[i][j] == s:
                    # extreme locations
                    if i == 0 and j == 0:
                        if s == datamatfin[i+1][j] or  s == datamatfin[i][j+1]  :
                            smax += 1
                    if i == len(datamatfin)-1 and j == 0:    
                        if s == datamatfin[i-1][j] or  s == datamatfin[i][j+1]:
                            smax += 1
                    if i == 0 and j == len(datamatfin)-1:
                        if s == datamatfin[i+1][j] or  s == datamatfin[i][j-1]:
                            smax += 1
                    if i == len(datamatfin)-1 and j == len(datamatfin)-1:
                        if s == datamatfin[i-1][j] or  s == datamatfin[i][j-1]:
                            smax += 1

                    # lim locations
                    if i == 0 and j != 0 and j !=  len(datamatfin)-1 :
                        if datamatfin[i][j-1] == s:
                            smax += 1
                    if  i == len(datamatfin) -1  and j != 0 and j !=  len(datamatfin)-1:
                        if  datamatfin[i][j-1] ==s or datamatfin[i-1][j] == s:
                            smax += 1
                    if  j == 0 and i != 0 and i != len(datamatfin)-1 :
                        if datamatfin[i-1][j]== s:
                            smax += 1
                    if j == len(datamatfin) -1  and i !=0 and  i != len(datamatfin)-1:
                        if  datamatfin[i][j-1] ==s or datamatfin[i-1][j] == s:
                            smax += 1 

                    #center
                    if i != 0 and j != 0 and j != len(datamatfin[0])-1 and i != len(datamatfin)-1:
                        if  datamatfin[i][j-1]  ==s or datamatfin[i-1][j] == s or datamatfin[i][j+1] == s or datamatfin[i+1][j] == s :
                            smax += 1
                        else:
                            smax = 1
        resultp.append(smax)
        maxx = max(resultp)
    return(maxx)


# In[5]:


def sizeprop(datamatfin,propaganda):
    s = propaganda
    smax= 0
    for i in range(len(datamatfin)):
        for j in range(len(datamatfin[0])):
            if datamatfin[i][j] == s:
                # extreme locations
                if i == 0 and j == 0:
                    if s == datamatfin[i+1][j] or  s == datamatfin[i][j+1]  :
                        smax += 1
                if i == len(datamatfin)-1 and j == 0:    
                    if s == datamatfin[i-1][j] or  s == datamatfin[i][j+1]:
                        smax += 1
                if i == 0 and j == len(datamatfin)-1:
                    if s == datamatfin[i+1][j] or  s == datamatfin[i][j-1]:
                        smax += 1
                if i == len(datamatfin)-1 and j == len(datamatfin)-1:
                    if s == datamatfin[i-1][j] or  s == datamatfin[i][j-1]:
                        smax += 1

                # lim locations
                if i == 0 and j != 0 and j !=  len(datamatfin)-1 :
                    if datamatfin[i][j-1] == s:
                        smax += 1
                if  i == len(datamatfin) -1  and j != 0 and j !=  len(datamatfin)-1:
                    if  datamatfin[i][j-1] ==s or datamatfin[i-1][j] == s:
                        smax += 1
                if  j == 0 and i != 0 and i != len(datamatfin)-1 :
                    if datamatfin[i-1][j]== s:
                        smax += 1
                if j == len(datamatfin) -1  and i !=0 and  i != len(datamatfin)-1:
                    if  datamatfin[i][j-1] ==s or datamatfin[i-1][j] == s:
                        smax += 1 

                #center
                if i != 0 and j != 0 and j != len(datamatfin[0])-1 and i != len(datamatfin)-1:
                    if  datamatfin[i][j-1]  ==s or datamatfin[i-1][j] == s or datamatfin[i][j+1] == s or datamatfin[i+1][j] == s :
                        smax += 1
                    else:
                        smax = 1
    return (smax)


# In[6]:


def takedat(resultstotal,resprop,repetitions):
    propdat = []
    grp =[]
    for j in range(len(resultstotal[0])):
        suma= []
        sumaprop =[]
        for i in range(repetitions):
            suma.append(resultstotal[i][j])
            sumaprop.append(resprop[i][j])
        me = np.mean(suma)
        mprop = np.mean(sumaprop)
        grp.append(me)
        propdat.append(mprop)
    sigma = abs(np.array(propdat) - np.array(grp))
    return grp,propdat, sigma


# In[7]:


def squarenet(N,config):
    G = nx.grid_2d_graph(int(N**(1/2)), int(N**(1/2)),periodic= False, create_using = None)
    contador =0
    for i in G.nodes():
        G.add_nodes_from([i],opinion= config[contador])
        contador += 1
    return G

def extractopinions(G):
    l = nx.get_node_attributes(G,"opinion")
    opinionvalues = []
    for i in (nx.get_node_attributes(G,"opinion")):
        opinionvalues.append(l[i])
    return opinionvalues

def squarenet(N,config):
    G = nx.grid_2d_graph(int(N**(1/2)), int(N**(1/2)),periodic= False, create_using = None)
    contador =0
    for i in G.nodes():
        G.add_nodes_from([i],opinion= config[contador])
        contador += 1
    return G

def extractopinions(G):
    l = nx.get_node_attributes(G,"opinion")
    opinionvalues = []
    for i in (nx.get_node_attributes(G,"opinion")):
        opinionvalues.append(l[i])
    return opinionvalues

config = []
N= 400
p =25
t = 4000
propaganda = 8
repetitions = 25
for i in range(N):
    config.append(int(p*random.uniform(0,1)))   
G = squarenet(N,config)


# In[42]:
datasigma = []
for intensity in np.linspace(1/p,1,p):
    resresults= []
    resresultsprop = []
    for k in range(repetitions):
        results = []
        resultsprop =[]
        for mu in range(p):
            config = []
            for i in range(N):
                config.append(int(p*random.uniform(0,1)))   
            G = squarenet(N,config)
            for T in range(t):
                for i in range(int(N**(1/2))):
                    for j in range(int(N**(1/2))):
                        if intensity >random.uniform(0,1):
                            if abs(propaganda -  G.nodes[i,j]["opinion"]) <= mu:
                                 G.nodes[i,j]["opinion"]= propaganda
                        else:
                            r = random.choice([-1,1])
                            if i == 0:
                                if r == -1:
                                    if random.uniform(0,1) > 0.5:
                                        d = (G.nodes[int(N**(1/2))-1,j]["opinion"] - G.nodes[i,j]["opinion"])
                                        if abs(d) <= mu:
                                            G.nodes[i,j]["opinion"]=G.nodes[int(N**(1/2))-1,j]["opinion"]
                                    else:
                                        d = (G.nodes[i,int(N**(1/2))-1]["opinion"] - G.nodes[i,j]["opinion"])
                                        if abs(d) <= mu:
                                            G.nodes[i,j]["opinion"]= G.nodes[i,int(N**(1/2))-1]["opinion"]
                            elif j == 0:
                                if r == -1:
                                    if random.uniform(0,1) > 0.5:
                                        d =  (G.nodes[int(N**(1/2))-1,j]["opinion"] - G.nodes[i,j]["opinion"])
                                        if abs(d) <= mu:
                                            G.nodes[i,j]["opinion"]=G.nodes[int(N**(1/2))-1,j]["opinion"]
                                    else:
                                        d = (G.nodes[i,int(N**(1/2))-1]["opinion"] - G.nodes[i,j]["opinion"])
                                        if abs(d) <= mu:
                                            G.nodes[i,j]["opinion"]= G.nodes[i,int(N**(1/2))-1]["opinion"]

                            elif i == int(N**(1/2))-1:
                                if r == 1:
                                    if random.uniform(0,1) > 0.5:
                                        d = (G.nodes[0,j]["opinion"] - G.nodes[i,j]["opinion"])
                                        if abs(d) <= mu:
                                            G.nodes[i,j]["opinion"]=G.nodes[0,j]["opinion"]
                                    else:
                                        d = (G.nodes[i,0]["opinion"]- G.nodes[i,j]["opinion"])
                                        if abs(d) <= mu:
                                            G.nodes[i,j]["opinion"]=G.nodes[i,0]["opinion"]

                            elif j == int(N**(1/2))-1:
                                if r == 1:
                                    if random.uniform(0,1) > 0.5:
                                        d = (G.nodes[0,j]["opinion"] - G.nodes[i,j]["opinion"])
                                        if abs(d) <= mu:
                                            G.nodes[i,j]["opinion"]=G.nodes[0,j]["opinion"]
                                    else:
                                        d = ( G.nodes[i,0]["opinion"] -  G.nodes[i,j]["opinion"])
                                        if abs(d) <= mu:
                                            G.nodes[i,j]["opinion"]= G.nodes[i,0]["opinion"]
                            else:
                                #for x
                                if random.uniform(0,1) > 0.5:
                                    d = (G.nodes[i+r,j]["opinion"] -  G.nodes[i,j]["opinion"])
                                    if abs(d) <= mu:
                                        G.nodes[i,j]["opinion"]= G.nodes[i+r,j]["opinion"]
                                #for y
                                else:
                                    d = ( G.nodes[i,j+r]["opinion"] -  G.nodes[i,j]["opinion"])
                                    if abs(d) <= mu:
                                        G.nodes[i,j]["opinion"]= G.nodes[i,j+r]["opinion"]

            datfin = extractopinions(G)
            datamatfin = np.array(datfin).reshape(int(N**(1/2)),int(N**(1/2)))
            res = dat2d(p,datamatfin)
            resprop = sizeprop(datamatfin,propaganda)
            resultsprop.append(resprop)
            results.append(res)
        resresults.append(results)
        resresultsprop.append(resultsprop)
    op, oprop, sig =takedat(resresults,resresultsprop,repetitions)
    datasigma.append(np.array(sig)/N)

# In[43]:



# In[45]:


df = pd.DataFrame(datasigma)

df.to_csv("data_squared_beta_vs._mu.csv", index=False)
