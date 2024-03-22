import math
import numpy as np
import matplotlib.pyplot as plt

import functions as fn
import numerical_solvers as ns
import output as out


def main():
    xmin = 0
    xmax = 5
    h = 0.25
    steps = int((xmax-xmin))/h
    plt.figure(figsize=(14,8))

    # calculate the exact analytical solution and plot it
    X_exact, Y_exact = ns.exact(fn.exact, xmin, xmax, steps)
    out.Plot(X_exact,Y_exact, 'red')
    plt.show()

    # calculate the numerical solutions and plot them
    X1,Y1 = ns.rk1(fn.dy_dx, xmin, xmax, steps, 1, h)
    out.Plot(X1,Y1,'#6666a3','*')

    X2,Y2 = ns.rk2(fn.dy_dx, xmin, xmax, steps, 1, h)
    out.Plot(X2,Y2,'#323284','D')

    X3,Y3 = ns.rk4(fn.dy_dx, xmin, xmax, steps, 1, h)
    out.Plot(X3,Y3,'#000066','o')


if __name__ == "__main__":
    main()