import numpy as np
import json
import matplotlib.pyplot as plt
plt.style.use('shao-yu')

def smooth(data, N, func=np.mean):
    new_data = []
    for n in range(len(data) - N):
        new_data.append(func(data[n: n+N]))

    return np.array(new_data)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(6, 8))

data = json.load(open('gs_aimd.json', 'r'))

#   We realized that the data had a bunch of Nan's when
#   the h-bond did not occur. This affected the averaging,
#   so we replaced the data with the ALL the distances 
#   of the star methanol
# data2 = json.load(open('gs_ffmd_MK.json', 'r'))
data2 = json.load(open('gs_ffmd_MK_FIXED.json', 'r'))

#   add second dataset to the first
keys = list(data2.keys())
for key in keys:
    data["MK_" + key] = data2[key]

labels = {'Amine_as_an_Acceptor':       'Acceptor/AIMD', 
          'Amine_as_a_Donor':           'Donor/AIMD', 
          'Amine_as_an_Donor_(FF)':     'Donor/QUBEKit', 
          'MK_Amine_as_an_Acceptor':    'Acceptor/revQUBEKit', 
          'MK_Amine_as_a_Donor':        'Donor/revQUBEKit',
          }
#   time to start trajectory at, in picoseconds 
start_times = [20, 20, 0, 0, 20]
saved_data = {}

for i, key in enumerate(('Amine_as_an_Acceptor', 'Amine_as_a_Donor', 'MK_Amine_as_an_Acceptor', 'MK_Amine_as_a_Donor', 'Amine_as_an_Donor_(FF)')):

    plt_data = data[key]
    time = np.array(plt_data['time'])
    keep = time >= start_times[i]
    time = time[keep] - start_times[i]
    
    # avg_dist = np.array(plt_data['smoothed_avg_distances'])[keep]
    # std_dist = np.array(plt_data['smoothed_std_distances'])[keep]
    n_smoothed = plt_data['n_smooth']

    #   compute our own smoothing
    avg_dist = smooth(np.array(plt_data['raw_distances']), n_smoothed, np.mean)[keep]
    std_dist = smooth(np.array(plt_data['raw_distances']), n_smoothed, np.std)[keep]
    time += n_smoothed * 4 / 1000
    label = labels[key]
    
    #   remove the part where the h-bond does not occur
    if key == 'MK_Amine_as_an_Acceptor':
        avg_dist[0:10000] = np.nan
        std_dist[0:10000] = np.nan

    avg_plt, = ax1.plot(time, avg_dist, label=label)
    std_plt, = ax2.plot(time, std_dist, label=label)

    #   this was before we realized that the data had a bunch of NaN's
    # if key == 'MK_Amine_as_an_Acceptor':
    #     ax1.plot((time[11764], time[12286]), (avg_dist[11764], avg_dist[12286]), linestyle='--', color=avg_plt.get_color())
    #     ax2.plot((time[11764], time[12286]), (std_dist[11764], std_dist[12286]), linestyle='--', color=avg_plt.get_color())

ax2.legend(loc='upper left')
ax1.set_ylabel('Average N-O Distance (Ang.)')
# ax1.set_xlabel('Simulation Time (ps)')
ax1.set_xlim(0, 60)
ax1.set_ylim(2.5, 2.9)

ax2.set_ylabel('Std. Dev. N-O Distance (Ang.)')
ax2.set_xlabel('Simulation Time (ps)')
ax2.set_xlim(0, 60)
ax2.set_ylim(0.00, 0.27)


fig.tight_layout()
fig.savefig('../png/hbonds_with_errors.png', dpi=300)

plt.show()


