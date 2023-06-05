import numpy as np
import os
import matplotlib.pyplot as plt
import global_settings
# plt.style.use('shao-yu')

figsize = np.array([7.3,8.5])*0.8
fig, ax = plt.subplots(figsize=figsize)
# left, bottom, width, height = [0.44, 0.65, 0.3, 0.25]

AU_2_CM = 219474.63
AU_2_EV = 27.211399

plot_files = [
    global_settings.data_root_dir + 'gs-ffmd/mm_qm1/vee_MD_resonance_raman.dat',
    global_settings.data_root_dir + 'gs-ffmd-MZ/mm_qm1/vee_MD_resonance_raman.dat',
    global_settings.data_root_dir + 'gs-aimd/mm_qm1/vee_MD_resonance_raman.dat',
    global_settings.data_root_dir + 'gs-aimd/qm2/vee_MD_resonance_raman.dat',
]
labels = [
    'QUBEKit/MM',
    'revQUBEKit/MM',
    'AIMD/MM',
    'AIMD/QM+MM',
]
colors = ['#C99300', '#259225', 'red', 'Blue']
spacing = 0.2

exp_data = np.loadtxt('experimental_raman.txt').T
exp_data[1] /= np.max(exp_data[1])
exp_data += len(plot_files)*(1.0 + + spacing)
ax.plot(exp_data[0], exp_data[1], color='k', label='Exp.')
ax.text(330, np.max(exp_data[1])-0.3, 'Experimental', size=18)


reference_max = None
for n, (file, label, color) in enumerate(zip(plot_files, labels, colors)):
    data = np.loadtxt(file)
    data[:, 0] *= AU_2_CM
    data[:, 1] *= AU_2_EV
    keep_idx = (data[:, 0] >= 300)*(data[:, 0] <= 900)
    data = data[keep_idx].T
    if reference_max is None:
        reference_max = np.max(data[1])
    data[1] /= reference_max
    data[1] += n*(1.0 + spacing)

    ax.plot(data[0], data[1], label=label, color=color)

    top = (n+1)*(1.0 + spacing)
    bot = n*(1.0 + spacing)
    text_loc = bot + (top-bot)*0.5
    ax.text(330, text_loc, label, size=18, color=color)

# ax.legend(loc='upper right')
ax.set_xlabel('Wavenumber (cm⁻¹)')
ax.set_ylabel('Intensity (arb. units)')
ax.set_ylim(0.00)
ax.set_xlim(300, 900)
ax.set_yticks([])
fig.tight_layout()
fig.savefig('png/raman_models.png', dpi=500)
plt.show()