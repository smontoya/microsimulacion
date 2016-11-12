from time import sleep
from mobility import *
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.cm as cm
import itertools
import numpy as np

x = np.arange(5)
ys = [i+x+(i*x)**3 for i in range(10)]
colors = iter(cm.rainbow(np.linspace(0, 1, len(ys))))
colors = itertools.cycle(["red", "blue", "green", "purple", "black"])

height = 1000
width = 1000
grupos = 2
# gm = gauss_markov(20, dimensions=(height, width))
gm = reference_point_group(50, dimensions=(height, width), aggregation=0.8)
gm2 = reference_point_group(50, dimensions=(height, width), aggregation=0.47)
gm3 = reference_point_group(50, dimensions=(height, width), aggregation=0.49)
gm4 = reference_point_group(50, dimensions=(height, width), aggregation=0.45)
gm5 = reference_point_group(50, dimensions=(height, width), aggregation=0.45)

xy = gm.__next__()







# size of the crowd
N = 2

def gen_data():
    """ init position and speed of each people """
    return next(gm), next(gm2), next(gm3), next(gm4), next(gm5)

def init():
    pathcol.set_offsets([[], []], )
    pathcol2.set_offsets([[], []], )
    pathcol3.set_offsets([[], []], )
    pathcol4.set_offsets([[], []], )
    pathcol5.set_offsets([[], []], )
    return pathcol, pathcol2, pathcol3, pathcol4, pathcol5

def update(i, pathcol, *args):
    # i = 0
    # for path in args:
    #     print(i)
    #     i += 1
    pathcol.set_offsets(next(gm))
    pathcol2.set_offsets(next(gm2))
    pathcol3.set_offsets(next(gm3))
    pathcol4.set_offsets(next(gm4))
    pathcol5.set_offsets(next(gm5))
    
    sleep(0.00001)
    return [pathcol, pathcol2, pathcol3, pathcol4, pathcol5]

fig = plt.figure()
ax = plt.axes(xlim=(0, width), ylim=(0, height))
pathcol = plt.scatter([], [], color=next(colors))
pathcol2 = plt.scatter([], [], color=next(colors))
pathcol3 = plt.scatter([], [], color=next(colors))
pathcol4 = plt.scatter([], [], color=next(colors))
pathcol5 = plt.scatter([], [], color=next(colors))
data = gen_data()
anim = animation.FuncAnimation(fig, update, init_func=init,
                               fargs=(pathcol, pathcol2, pathcol3, pathcol4, pathcol5, data), interval=0, blit=True)
plt.show()