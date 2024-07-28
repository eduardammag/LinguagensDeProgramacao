import numpy as np

def task_7():
    nda_8 = np.matrix([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
    nda_I3 = np.eye(3)
    
    determinante = np.linalg.det(nda_8)
    nda_inv = np.linalg.inv(nda_8)

    nda_size = np.shape(nda_8)

    inv_test = nda_inv * nda_8
    
    for i in range(0, nda_size[0]):
        for j in range(0, nda_size[0]):
            if (inv_test[i, j] < 0.001):
                inv_test[i, j] = 0 
            
    print( nda_8, "\n")
    print( nda_inv, "\n")
    print( inv_test, "\n")
