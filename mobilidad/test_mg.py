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
colors = itertools.cycle(["red", "black", "black", "black", "black"])

height = 500
width = 500
grupos = 2
# gm = gauss_markov(20, dimensions=(height, width))
#gm = reference_point_group(50, dimensions=(height, width), aggregation=0.8)
#gm2 = reference_point_group(50, dimensions=(height, width), aggregation=0.47)
#gm3 = reference_point_group(10, dimensions=(height, width), aggregation=0.49)
#gm4 = reference_point_group(10, dimensions=(height, width), aggregation=0.45)
#gm5 = reference_point_group(10, dimensions=(height, width), aggregation=0.45)

gm = tvc([10, 5, 5 ,5 ,5,5], dimensions=(height, width), velocity=(0.1, 1.), aggregation=[1,0.5], epoch=[100,100], safepoint=[410,300])
gm2 = tvc(10, dimensions=(height, width), velocity=(0.1, 1.), aggregation=[1,0.5], epoch=[5,10], safepoint=[320,100])
gm3 = tvc(10, dimensions=(height, width), velocity=(0.1, 1.), aggregation=[1,0.5], epoch=[25,75], safepoint=[100,300])
gm4 = tvc(10, dimensions=(height, width), velocity=(0.1, 1.), aggregation=[1,0.5], epoch=[15,30], safepoint=[500,400])
gm5 = tvc(10, dimensions=(height, width), velocity=(0.1, 1.), aggregation=[1,0.5], epoch=[25,45], safepoint=[60,90])

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
    
    sleep(0.01)
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