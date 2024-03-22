import numpy as np
import matplotlib.pyplot as plt

'''Functions for exact and numerical integration of IVPs'''


def exact(X):
    return (1/6.0)*(2*np.sin(3.0*X))+(3*(np.cos(2.0*X)+3))


def dy_dx(X,y):
    return (-np.sin(2.0*X))+np.cos(3.0*X)
