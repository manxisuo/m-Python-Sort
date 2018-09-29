# _*_ coding: utf-8 _*_
from random import randint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def rand_int_array(length=10, start=1, end=50):
    return [randint(start, end) for i in range(length)]


def animate(arr, arr_gen, interval = 1000):
    fig, ax = plt.subplots()
    ax.set_xlim(0, len(arr))
    ax.set_ylim(min(arr) - 10, max(arr) + 10)
    (line1,) = plt.plot([], [], c='r', ls='', marker='o', alpha=0.618, animated=True)
    (line2,) = plt.plot([], [], c='b', ls='', marker='o', alpha=0.618, animated=True)

    xdata = np.arange(len(arr))

    def update(frame):
        ydata, indexes = frame
        line1.set_data(xdata, ydata)
        line2.set_data(indexes, np.asarray(ydata)[indexes])
        return line1, line2

    ani = FuncAnimation(fig, update, frames=arr_gen, init_func=None,
                        blit=True, interval=interval, repeat=False)
    # ani.save('c.gif', dpi=80, writer='imagemagick')
    plt.show()
