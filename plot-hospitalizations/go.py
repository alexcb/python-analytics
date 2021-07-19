import matplotlib.pyplot as plt

def frange(start,stop,by):
    while start < stop:
        yield start
        start += by

vac_hosp_rate = 0.01
nonvac_hosp_rate = 0.1

vac_rates = []
num_hospitalization = []
vac_vs_total_ratio = []
nonvac_vs_total_ratio = []
ratio = []
invratio = []

for vac_rate in frange(0.01, 1.0, 0.01):
    vac_hosp = vac_hosp_rate*vac_rate
    nonvac_hosp = nonvac_hosp_rate*(1.0-vac_rate)

    vac_rates.append(vac_rate)
    total_hospitalizations = vac_hosp+nonvac_hosp
    num_hospitalization.append(total_hospitalizations*1000.0)
    vac_vs_total_ratio.append(vac_hosp/total_hospitalizations)
    nonvac_vs_total_ratio.append(nonvac_hosp/total_hospitalizations)
    ratio.append(vac_hosp/nonvac_hosp)

    invratio.append(nonvac_hosp/vac_hosp)

print(vac_rates)

plt.plot(vac_rates, num_hospitalization)
plt.xlabel('vac rate')
plt.ylabel('number of hospitalizations per 1000')
plt.savefig('total-per-1000.png', bbox_inches='tight')
plt.cla()

plt.plot(vac_rates, vac_vs_total_ratio)
plt.xlabel('vac rate')
plt.ylabel('ratio of vaccinated hospitalizations vs total hospitalizations')
plt.savefig('vac-hospitalizations-vs-total-hospitalizations.png', bbox_inches='tight')
plt.cla()

plt.plot(vac_rates, nonvac_vs_total_ratio)
plt.xlabel('vac rate')
plt.ylabel('ratio of nonvaccinated hospitalizations vs total hospitalizations')
plt.savefig('nonvac-hospitalizations-vs-total-hospitalizations.png', bbox_inches='tight')
plt.cla()

plt.plot(vac_rates, ratio)
plt.xlabel('vac rate')
plt.ylabel('ratio of vaccinated vs nonvaccinated hospitalizations')
plt.savefig('vac-hospitalizations-vs-nonvac-hospitalizations.png', bbox_inches='tight')
plt.cla()

plt.plot(vac_rates, invratio)
plt.xlabel('vac rate')
plt.ylabel('ratio of nonvaccinated vs vaccinated hospitalizations')
plt.savefig('nonvac-hospitalizations-vs-vac-hospitalizations.png', bbox_inches='tight')
plt.cla()
