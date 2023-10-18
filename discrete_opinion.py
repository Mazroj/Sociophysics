import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

class Global:
    
    def __init__(self,size,options):
        self.size = size
        self.options = options
        
    
    #Defining the creation of a new network
    def nuevared(self,tip, mean = 50, sdev = 10):
        '''
        Creat an array connected globally and gives an opinion value.
        '''
        if tip == 'uniform':
            x = np.random.randint(0,self.options,size=self.size)
        elif tip == 'normal':
            normal_values = np.random.normal(loc=mean, scale=sdev, size = self.size)

            # Round the floating-point values to integers between 1 and 100
            x = np.clip(np.round(normal_values), 1, 100)
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
        inter_mass = np.where(random_r < intensity_array , True,np.zeros(len(list1)))
        
        # Interaction with mass media
        distance = np.abs(list1 - propaganda_array)
        conditions = np.logical_and(inter_mass , distance < tolerance_array)
        list4 = np.where(conditions, propaganda_array, list1)

        # Interaction with agents
        distance = np.abs(list1 - list3)
        conditions = np.logical_and(inter_mass != True , distance < tolerance_array)
        list5 = np.where(conditions, list3, list4)
        
        return list5
    
    # Defining simulation algorithm
    def simul_global_evol(self,tolerance,intensity,time,propaganda, mean, sdev,tipe = 'uniform'):
        list1 = self.nuevared(tipe,mean,sdev)
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
    
    #Obtaion information from the netwok, smax and sprop
    def most_frequent_value(self,arr,propaganda):
        values, counts = np.unique(arr, return_counts=True)
        smax = np.max(counts)
        sprop_index = np.where(values == propaganda)[0][0]
        sprop = counts[sprop_index]

        return smax, sprop
    

    
class Cycle:
    
    def __init__(self,size,options):
        self.size = size
        self.options = options
        
    def new_network(self, k):
        '''
        Create a cycle network of size and options determined with an aleatory state of opinion and with k neighbors
        '''
        # Create an empty adjacency matrix
        adjacency_matrix = np.zeros((self.size, self.size), dtype=int)

        # Connect each agent to its k neighbors on each side
        for i in range(self.size):
            for j in range(1, k+1):
                adjacency_matrix[i, (i - j) % self.size] = 1  # Connect to the left neighbor
                adjacency_matrix[i, (i + j) % self.size] = 1  # Connect to the right neighbor

        # Create a graph from the adjacency matrix
        G = nx.from_numpy_array(adjacency_matrix)

        opinions = np.random.randint(0, self.options, size=self.size)

        node_attributes = {node: opinion for node, opinion in zip(G.nodes, opinions)}

        # Set the attributes to the graph nodes
        nx.set_node_attributes(G, node_attributes, 'opinion')

        return G


    
    def interaction(self,graph, tolerance, intensity, propaganda):
        '''
        Simulate the interaction between mass media or agents
        '''
        for node in graph.nodes():
            if random.random() < intensity:
                if abs(graph.nodes[node]['opinion'] - propaganda) < tolerance:
                    graph.nodes[node]['opinion'] = propaganda
            else:
                neighbors = list(graph.neighbors(node))
                neighbor = random.choice(neighbors)
                if abs(graph.nodes[node]['opinion'] - graph.nodes[neighbor]['opinion']) < tolerance:
                    graph.nodes[node]['opinion'] = graph.nodes[neighbor]['opinion']

        return graph
    

    def inter_simul(self,time, tolerance, intensity, propaganda, k):
        '''
        Iterates simulation time times
        '''
        a = self.new_network(k)
        T = 0
        while T < time:
            a = self.interaction(a, tolerance, intensity, propaganda)
            T += 1

        return a
    
    
    