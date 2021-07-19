import matplotlib.pyplot as plt

def frange(start,stop,by):
    while start < stop:
        yield start
        start += by

vac_hosp_rate = 0.01
nonvac_hosp_rate = 0.1

vac_rates = []
ratio = []

num_vac_hosp_per_1000 = []
num_nonvac_hosp_per_1000 = []

for vac_rate in frange(0.01, 0.99, 0.01):
    vac_hosp = vac_hosp_rate*vac_rate
    nonvac_hosp = nonvac_hosp_rate*(1.0-vac_rate)

    num_vac_hosp_per_1000.append(vac_hosp*1000)
    num_nonvac_hosp_per_1000.append(nonvac_hosp*1000)

    vac_rates.append(vac_rate)
    total_hospitalizations = vac_hosp+nonvac_hosp
    ratio.append(vac_hosp/total_hospitalizations)

f, sp = plt.subplots(3, sharex=True, sharey=False, figsize=(10.0, 10.0))
sp[0].plot(vac_rates, num_nonvac_hosp_per_1000)
sp[0].set_ylabel('number of non vac hosp per 1000')
sp[1].plot(vac_rates, num_vac_hosp_per_1000)
sp[1].set_ylabel('number of vac hosp per 1000')
sp[2].plot(vac_rates, ratio)
sp[2].set_ylabel('probability hosp patient is vacced')
sp[2].set_xlabel('vac rate')
plt.savefig('combined.png', bbox_inches='tight')
plt.cla()
