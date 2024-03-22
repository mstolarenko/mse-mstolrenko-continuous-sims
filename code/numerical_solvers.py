import math
import numpy as np
import matplotlib.pyplot as plt

'''Numerical Integrators'''


def exact(df, xmin, xmax, steps,sm = 1):
    X = np.linspace(xmin, xmax, int(steps*sm+1))
    Y = df(X)
    return X,Y


def rk1(df, xmin, xmax, steps, y_start, h):
    X = np.linspace(xmin, xmax, int(steps+1))
    Y = np.zeros(len(X))
    Y[0] = y_start
    for i in range(1, len(X)):
        Y[i] = Y[i-1] + h * df(X[i-1],Y[i-1])

    return (X,Y)


def rk2(df, xmin, xmax, steps, y_start, h):
    # TODO: Implement RK2, create numpy arrays and populate them.    # still need to do
    X = np.linspace(xmin, xmax, int(steps+1))
    Y = np.zeros(len(X))
    Y[0] = y_start
    for i in range(1, len(X)):
        Y[i] = Y[i-1] + h * df(X[i-1]+h/2, Y[i-1]+h/2*df(X[i-1], Y[i-1]))
    return (X,Y)


def rk4(df, xmin, xmax, steps, y_start, h):
    X = np.linspace(xmin, xmax, int(steps+1))
    Y = np.zeros(len(X))
    Y[0] = y_start
    for i in range(1, len(X)):
        Y[i] = Y[i -1] + h * (1.0/6) * (df(X[i-1], Y[i-1]) +
                        2.0 * df(X[i-1] + h/2, Y[i-1] + h/2 * df(X[i-1], Y[i-1])) +
                        2.0 * df(X[i-1] + h/2, Y[i-1] + h/2 * df(X[i-1] + h/2, Y[i-1] + h/2 * df(X[i-1], Y[i-1]))) +
                        df(X[i-1] + h, Y[i-1] + h * df(X[i-1] + h/2, Y[i-1] + h/2 * df(X[i-1] + h/2, Y[i-1] + h/2 * df(X[i-1], Y[i-1])))))

    return (X,Y)




