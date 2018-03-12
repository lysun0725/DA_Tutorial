import numpy as np
from params_maooam import ndim
import aotensor as aotensor_mod
import integrator

def compute_tltensor(eta):
    tensor = aotensor_mod.aotensor
    j_mat = np.zeros([ndim,ndim])
   
    eta2 = np.append(eta,1.) 
    for n in np.arange(0,np.shape(tensor)[0]):
        i = tensor[n][0]
        j = tensor[n][1]
        k = tensor[n][2]
        v = tensor[n][3]
    
        if j!=0:
            j_mat[i-1,j-1] = j_mat[i-1,j-1] + v*eta2[k-1]
        
        if k!=0:
            j_mat[i-1,k-1] = j_mat[i-1,k-1] + v*eta2[j-1]

    return j_mat






    
    
        

