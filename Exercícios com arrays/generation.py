import numpy as np
import numpy.random as npr

#1

nda_int= np.arange(5,32,3)
print(nda_int)

nda_rand = npr.randint(3,77,9)
print(nda_rand)

nda_soma = nda_int + nda_rand
print(nda_soma)

#2
#Mudando a dimensão
nda_2D = nda_soma.reshape(3,3)

# Converter para float
nda_2D_float = nda_2D.astype(float)

# Calculando a transposta 
transposta = np.transpose(nda_2D_float)

#3

nda_3x3 = nda_int.reshape(3,3)

nda_3x3 = nda_3x3 * nda_2D_float

#4
a1D_5 = npr.randint(3,77,50)

a1D_6 = npr.randint(13,98,50)

def números_comuns(a,b):
    lista = []
    for element in a:
       if element in b:
            lista.append(element)
    return lista

def elementos_não_comuns(a,b):
    lista = []
    for element in a:
       if element not in b:
           lista.append(element)
    return lista
    
