import numpy as np
import datetime
from numpy import convolve
import matplotlib.pyplot as plt
import matplotlib.dates

t, y = np.loadtxt(
    'input.data',
    converters={
        0: matplotlib.dates.strpdate2num('%Y-%m-%dT%H:%M:%SZ'),
        },
    unpack=True,
    )

daily = {}

for tt, yy in zip(t, y):
    tt = matplotlib.dates.num2date(tt)
    d = str(tt.date())
    if d not in daily:
        daily[d] = 0
    daily[d] += yy

for date, total in sorted(daily.items()):
    print date, total

plt.plot_date(t, y, '.')
plt.xlabel('Date')
#plt.savefig('output.png', bbox_inches='tight')
plt.show()

