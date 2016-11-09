from time import sleep
from pymobility.models.mobility import random_waypoint, gauss_markov
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np

height = 100
width = 100
gm = gauss_markov(20, dimensions=(height, width))
positions = next(gm)
xy = gm.__next__()











# size of the crowd
N = 2

def gen_data():
    """ init position and speed of each people """
    return positions

def init():
    pathcol.set_offsets([[], []])
    return pathcol,

def update(i, pathcol, data):
    pathcol.set_offsets(next(gm))
    sleep(0.01)
    return [pathcol]

fig = plt.figure()
ax = plt.axes(xlim=(0, width), ylim=(0, height))
pathcol = plt.scatter([], [])
data = gen_data()
anim = animation.FuncAnimation(fig, update, init_func=init,
                               fargs=(pathcol, data), interval=0, blit=True)
plt.show()