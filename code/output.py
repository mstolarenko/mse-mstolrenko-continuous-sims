import math
import numpy as np
import matplotlib.pyplot as plt
import numerical_solvers as ns


'''General functions for formatting, printing and plotting output'''


def Plot(X,Y,c,m=''):
    # TODO: (Extend and edit as you see fit to help visualize your work)
    plt.plot(X,Y, 'bo', color=c, marker=m, linestyle='-')
    plt.show()
