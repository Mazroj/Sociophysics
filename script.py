import pandas as pd
import numpy as np
import discrete_opinion as dp
from mpi4py import MPI

def most_frequent_value(arr,propaganda):
    values, counts = np.unique(arr, return_counts = True)
    smax = np.max(counts)
    sprop_index = np.where(values == propaganda)[0][0]
    sprop = counts[sprop_index]

    return smax, sprop

world_comm = MPI.COMM_WORLD
world_size = world_comm.Get_size()
my_rank = world_comm.Get_rank()

#workloads = [100//world_size for i in range(world_size)]
#for i in range(100 % world_size):
#    workloads[i] += 1
#my_start = 0
#for i in range(my_rank):
 #   my_start += workloads[i]
#my_end = my_start + workloads[my_rank]

for prop in range(100, 101):

    ob1 = dp.Global(size = 1000, options = 100)  #initialize
    tol = np.arange(0,100,1) # Define tolerance vector
    resres1 = [] #store results smax
    resres2 = [] #store resutls sprop

    for rep in range(50):
        res1 = np.empty(100)  #store smax
        res2 = np.empty(100)  #store sprop

        for i in tol:
            lisq = ob1.simul_global_evol(i,0.5, 150000 , prop)
            smax, sprop = most_frequent_value(lisq, prop)
            res1[i] = smax
            res2[i] = sprop

        resres1.append(res1)
        resres2.append(res2)


    df_smax = pd.DataFrame(resres1)
    df_sprop = pd.DataFrame(resres2)

    df_smax.to_csv(f"data/smax_vs_mu_p{prop}.csv", index = False)
    df_sprop.to_csv(f"data/sprop_vs_mu_p{prop}.csv", index = False)

    print("Finishing for prop: ", prop)
