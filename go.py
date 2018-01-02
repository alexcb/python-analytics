import numpy as np
import datetime
from numpy import convolve
import matplotlib.pyplot as plt

def fill_missing_seconds(values):
    t = []
    y = []
    for i in xrange(len(values)-1):
        tt, yy = values[i,]
        next_t = values[i+1,0]
        t.append(tt)
        y.append(yy)

        tt += 1
        while tt < next_t:
            t.append(tt)
            y.append(0.0)
            tt += 1
    return np.column_stack((t, y))

def moving_average(values, window):
    t = []
    y = []
    for i in xrange(len(values)-window):
        yy = float(values[i:(i+window), 1].sum()) / float(window)
        tt = values[i,0]
        t.append(tt)
        y.append(yy)
    return np.column_stack((t, y))


data = np.loadtxt('input.data')
data = fill_missing_seconds(data)
data = moving_average(data, 60*30)
t = data[:,0]
y = data[:,1]

t = [datetime.datetime.fromtimestamp(x) for x in t]

plt.plot(t,y)
plt.savefig('output.png', bbox_inches='tight')
plt.show()

