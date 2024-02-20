import numpy as np
import random
import pandas as pd
#import matplotlib.pyplot as plt

class Global:
    
    def __init__(self,size,options):
        self.size = size
        self.options = options
        
    
    #Defining the creation of a new network
    def nuevared(self):
        '''
        Creat an array connected globally and gives an opinion value.
        '''
        x = np.random.randint(1,self.options+1,size=self.size)
        return(x)
    
    
    #Definig the algoritm of interaction of agents
    def interaction(self,list1, tolerance, intensity, propaganda):
        '''
        Defines the interaction of network from time t to time t+1 (iteration)
        '''
       
        list2 = np.random.randint(0,len(list1),size = self.size)
        list3 = list1[list2]
        
        # Create an array with parameters intensity and tolerance
        intensity_array = intensity*np.ones(len(list1))
        tolerance_array = tolerance*np.ones(len(list1))
        propaganda_array = propaganda*np.ones(len(list1))
        random_r = np.random.random(size =len(list1))
        
        # Acts like an if but for an array to work in all elements at the same time
        inter_mass = np.where(random_r < intensity_array , 1,np.zeros(len(list1)))
        
        # Interaction with mass media
        distance = np.abs(list1 - propaganda_array)
        conditions = np.logical_and(inter_mass == 1 , distance < tolerance_array)
        list4 = np.where(conditions, propaganda, list1)

        # Interaction with agents
        distance = np.abs(list1 - list3)
        conditions = np.logical_and(inter_mass == 0 , distance < tolerance_array)
        list5 = np.where(conditions, list3, list4)
        return list5
    
    # Defining simulation algorithm
    def simul_global_evol(self,tolerance,intensity,time,propaganda):
        list1 = self.nuevared()
        T = 0
        his = []
        while T < time:
            
            # Iterates simulation
            list5 = self.interaction(list1, tolerance,intensity, propaganda)
            list1 = list5
            
            # Define Stop Condition
            if T % 500 ==0 :
                his.append(list5.copy())

            if len(his) >= 6:
                if (his[-1]== his[-3]).all() and T >3000  :
                    break
            T += 1

        return(list1)


#Obtain information from the netwok, smax and sprop

def most_frequent_value(arr,propaganda):
    values, counts = np.unique(arr, return_counts=True)
    smax = np.max(counts)
    sprop_index = np.where(values == int(propaganda))[0]
    sprop = counts[sprop_index]
    return smax, sprop
