import numpy as np

def task_5(nda_five, nda_six):
    nda_seven = np.hstack((nda_five, nda_six))
    
    media = nda_seven.mean()
    desv_pad = nda_seven.std()
    var = nda_seven.var()
    
    print(f"Média: {media}\nDesvio Padrão: {desv_pad}\nVariância: {var}\n")
    
    nda_size = np.shape(nda_seven)
    odd_num = np.arange(1, nda_size[0], 2)
    even_num = np.arange(0, nda_size[0], 2)
    
    for i in range(0, nda_size[0]):
        if (nda_seven[i] % 2 == 0):
            nda_seven[i] = 1
        else:
            nda_seven[i] = -1
            
    print(nda_seven)
