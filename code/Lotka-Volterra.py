import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.integrate import odeint

y0 = [2, 1]                                 # initial value x0=2; initial value y0=1
t = np.linspace(0,20,num=200)               # (xmax-xmin)/h = 20/0.1 = 200 steps
a = 1; b = 1; c = 1; d = 1                  # initial value arguments; modify for different results

initial_values = [a, b, c, d]


def sim(variables, t, initial_values):
    x = variables[0]
    y = variables[1]
    a = initial_values[0]; b = initial_values[1]; c = initial_values[2]; d = initial_values[3]
    X = a * x - b * y * x
    Y = d * x * y - c * y
    return[X, Y]


y = odeint(sim, y0, t, args=(initial_values,))          # args is a tuple, must have a blank slot since array was made
f, (ax1) = plt.subplots(1)
f.set_figwidth(5)
f.set_figheight(5)
line1, = ax1.plot(t,y[:,0], color='orange', label="Machines")
line2, = ax1.plot(t,y[:,1], color='purple', label="Mitchells")
plt.title("Predator-Prey Simulation")
plt.legend(handles=[line1, line2])
plt.show()

