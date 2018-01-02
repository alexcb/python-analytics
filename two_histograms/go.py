data = []
with open('logs', 'r') as fp:
    for l in fp.readlines():
        l = l.strip()
        try:
            cond, duration = l.split()
        except ValueError:
            continue
        duration = float(duration)
        cond = cond == 'true'
        data.append({'cond': cond, 'duration': duration})


import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

true_durations = [x['duration'] for x in data if x['cond']]
false_durations = [x['duration'] for x in data if not x['cond']]

bins = np.linspace(0, 2, 25)

combined = False

if combined:
    plt.hist(true_durations, bins, alpha=0.5, label='true', normed=True, facecolor='green')
    plt.hist(false_durations, bins, alpha=0.5, label='false', normed=True, facecolor='blue')
    plt.legend(loc='upper right')
    plt.grid(True)

else:
    f, sp = plt.subplots(2, sharex=True, sharey=True)
    sp[0].hist(true_durations, bins, alpha=0.5, label='true', normed=True, facecolor='green')
    sp[0].grid(True)
    sp[0].legend(loc='upper right')
    sp[0].set_ylabel('percentage of calls')

    sp[1].hist(false_durations, bins, alpha=0.5, label='false', normed=True, facecolor='blue')
    sp[1].grid(True)
    sp[1].legend(loc='upper right')
    sp[1].set_ylabel('percentage of calls')
    sp[1].set_xlabel('call duration (seconds)')

plt.show()


