import numpy as np
import os
import matplotlib.pyplot as plt

script_dir = os.path.abspath(os.path.dirname(__file__))
plt.style.use(script_dir + '/style.mplstyle')

plot_files = [
    script_dir + '/../gs-ffmd/mm_qm1_high_freq/vee_MD_cumulant_spectrum.dat',
    script_dir + '/../gs-ffmd-MZ/mm_qm1_high_freq/vee_MD_cumulant_spectrum.dat',
    script_dir + '/../gs-aimd/mm_qm1_high_freq/vee_MD_cumulant_spectrum.dat',
    script_dir + '/../gs-aimd/qm2_high_freq/vee_MD_cumulant_spectrum.dat',

    script_dir + '/../gs-ffmd/mm_qm1_low_freq/vee_MD_cumulant_spectrum.dat',
    script_dir + '/../gs-ffmd-MZ/mm_qm1_low_freq/vee_MD_cumulant_spectrum.dat',
    script_dir + '/../gs-aimd/mm_qm1_low_freq/vee_MD_cumulant_spectrum.dat',
    script_dir + '/../gs-aimd/qm2_low_freq/vee_MD_cumulant_spectrum.dat',
]
labels = [
    'QUBEKit/MM',
    'QUBEKit(MK)/MM',
    'AIMD/MM',
    'AIMD/QM+MM',

    'QUBEKit/MM',
    'QUBEKit(MK)/MM',
    'AIMD/MM',
    'AIMD/QM+MM',
]

fig, ax_grid = plt.subplots(2, 1, figsize=(8.0,8.5))
colors = ['#C99300', '#259225', 'red', 'Blue', '#C99300', '#259225', 'red', 'Blue']

exp_data = np.loadtxt('experimental_abs.txt').T
# ax.plot(exp_data[0], exp_data[1], color='grey', linestyle=(0, (1, 1)), label='Experiment')
# ax.fill_between(exp_data[0], 0, exp_data[1], color='#BFC1C1', linestyle=(0, (1, 1)), label='Experiment')

max_loc = exp_data[0][np.argmax(exp_data[1])]
max_loc = 2.1
i = 0
for file, label, color in zip(plot_files, labels, colors):
    data = np.loadtxt(file).T
    data[1] /= data[1].max()

    if max_loc is None:
        max_loc = data[0][data[1].argmax()]
    else:
        this_max = data[0][data[1].argmax()]
        data[0] -= (this_max - max_loc)

    plot_num = int(i / 4)
    ax = ax_grid[plot_num]
    ax.plot(data[0], data[1], label=label, color=color)
    i += 1

    if plot_num == 0:
        ax.legend(loc='upper right')
    if plot_num == 1:
        ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Intensity (arb. units)')
    ax.set_ylim(-0.005, 1.05)
    ax.set_xlim(1.9, 2.5)
    ax.set_yticks([])
    # ax.set_xticks([1.5, 1.7, 1.9, 2.1, 2.3, 2.5])
    ax.set_xticks([1.9, 2.1, 2.3, 2.5])

    if plot_num == 0:
        ax.text(0.65, 0.15, 'High Frequency', fontsize=22, transform=ax.transAxes)
    else:
        ax.text(0.65, 0.15, 'Low Frequency', fontsize=22, transform=ax.transAxes)

fig.tight_layout()
fig.savefig('png/abs_spectra_models_low_high.png', dpi=500)
plt.show()