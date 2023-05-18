import numpy as np
import json
import matplotlib.pyplot as plt
plt.style.use('shao-yu')

fig, ax = plt.subplots()

data = json.load(open('gs_aimd.json', 'r'))

file_names = ['hbonds_amine_acceptor.txt', 'hbonds_amine_donor.txt', 'hbonds_amine_donor.txt']
labels = ['Amine as an Acceptor', 'Amine as a Donor', 'Amine as an Donor (FF)']
saved_data = {}

for i, plt_data in enumerate(data.values()):

    time = np.array(plt_data['time'])
    keep = time >= 20
    time = time[keep] - 20
    avg_dist = np.array(plt_data['smoothed_avg_distances'])[keep]
    std_dist = np.array(plt_data['smoothed_std_distances'])[keep]
    n_smoothed = plt_data['n_smooth']
    time += n_smoothed * 4 / 1000
    label = labels[i]
    print(time[0])


    ax.plot(time, avg_dist, label=label)
    ax.fill_between(time, avg_dist - std_dist, avg_dist + std_dist, alpha = 0.5)

ax.legend(loc='upper left')
ax.set_ylabel('N-O Distance (Ang.)')
ax.set_xlabel('Simulation Time (ps)')
ax.set_xlim(0, 60)
fig.tight_layout()
fig.savefig('../png/hbonds.png', dpi=300)

plt.show()


