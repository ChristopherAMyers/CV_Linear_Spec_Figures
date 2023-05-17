import numpy as np
import os
import matplotlib.pyplot as plt
plt.style.use('shao-yu')
fig, ax = plt.subplots(figsize=(8,4.5))

plot_files = [
    '../gs-aimd/mm_qm1/vee_MD_cumulant_spectrum.dat',
    '../gs-ffmd-MZ/full_trajectory/vee_MD_cumulant_spectrum.dat',
    '../gs-ffmd-MZ/36-20ps-crop/vee_MD_cumulant_spectrum.dat',
    # 'gs-ffmd-MZ/20-40ps-crop/vee_MD_cumulant_spectrum.dat',
]
labels = [
    'AIMD-QM1 (40/20 ps)',
    'FFMD-QM1 \n(MK, 36/44 ps)',
    'FFMD-QM1 \n(MK, 36/20 ps)',
    # 'FFMD-QM1 \n(MK, 20/40 ps)',
]

colors = ['red', 'lightseagreen', 'orange']

exp_data = np.loadtxt('experimental_abs.txt').T
ax.plot(exp_data[0], exp_data[1], color='grey', linestyle=(0, (1, 1)), label='Experiment')

max_loc = exp_data[0][np.argmax(exp_data[1])]
for file, label, color in zip(plot_files, labels, colors):
    data = np.loadtxt(file).T
    data[1] /= data[1].max()

    if max_loc is None:
        max_loc = data[0][data[1].argmax()]
    else:
        this_max = data[0][data[1].argmax()]
        data[0] -= (this_max - max_loc)

    ax.plot(data[0], data[1], label=label, color=color)

ax.legend(loc='upper left')
ax.set_xlabel('Energy eV')
ax.set_ylabel('Intensity (arb. units)')
ax.set_ylim(-0.005, 1.2)
ax.set_xlim(1.5, 2.5)
ax.set_yticks([])
ax.set_xticks([1.5, 1.7, 1.9, 2.1, 2.3, 2.5])
fig.tight_layout()
fig.savefig('png/abs_spectra_MZ_charges.png', dpi=300)
plt.show()