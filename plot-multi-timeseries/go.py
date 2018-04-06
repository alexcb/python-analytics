import datetime

import matplotlib as mpl
mpl.use('Agg') # dont use X

import numpy as np
import matplotlib.pylab as plt

data = {
    'a': {
        't': ['2010-10-10', '2010-10-11', '2010-10-12', '2010-10-13', '2010-10-15',],
        'y': [          12,           51,           59,           21,           99,],
        },
    'b': {
        't': ['2010-10-10', '2010-10-11', '2010-10-12', '2010-10-13', '2010-10-14',],
        'y': [         399,          234,          123,           95,           28,],
        },
    'c': {
        't': ['2010-10-08', '2010-10-11', '2010-10-12', '2010-10-13', '2010-10-14',],
        'y': [          32,           21,           19,           81,           39,],
        },
    }

def datestr_to_datetime(s):
    return datetime.datetime.strptime(s, "%Y-%m-%d")


colors = mpl.cm.rainbow(np.linspace(0, 1, len(data)))
fig, ax = plt.subplots()

ax.autoscale(enable=True)
for color, (name, d) in zip(colors, sorted(data.items())):
    t = [datestr_to_datetime(x) for x in d['t']]
    y = d['y']
    ax.plot(t, y, '-o', label=name)

# rotate dates to avoid overlapping
# plt.xticks(rotation=30)

# only display every second tick
for label in ax.xaxis.get_ticklabels()[::2]:
    label.set_visible(False)

fig.set_size_inches(18.5, 10.5)
fig.legend()
fig.savefig('output.png', bbox_inches='tight')
plt.close()
