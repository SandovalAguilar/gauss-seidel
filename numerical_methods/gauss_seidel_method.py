import numpy as np

'''
def Gauss_Seidel(A, b, iter_n, initial_guess=0):
    n = len(A)
    
    D = np.diag(A)
    L = np.tril(A) - np.diag(D)
    U = np.triu(A) - np.diag(D)
    
    x_i = initial_guess * np.ones(n)
    x_ii = x_i.copy()
    
    for _ in range(iter_n):
        for k in range(n):
            x_ii[k] = (b[k] - U[k].dot(x_i) - L[k].dot(x_ii)) / D[k]
        x_i = x_ii.copy()
        
    return x_i
'''

class gaussSeidel:
    pass