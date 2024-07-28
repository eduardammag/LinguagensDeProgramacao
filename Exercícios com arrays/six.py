import numpy as np

def task_6():
    nda_A = np.arange(1, 10, 2)
    nda_B = np.arange(0, 10, 2).reshape((5, 1))
    
    print(nda_B * nda_A)