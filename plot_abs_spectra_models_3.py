import matplotlib.pyplot as plt
import numpy as np
import global_settings as GS
import plot_abs_spectra_models_low_high_freq
import plot_abs_spectra_models

fontsize = 14
rcParams = {
    'xtick.labelsize': fontsize,
    'ytick.labelsize': fontsize,
    'font.weight': 'bold',
    'axes.labelsize': fontsize + 2,
    'axes.labelweight': 'extra bold',
    'figure.labelsize': fontsize,
    'figure.labelweight': 'bold',
}
plt.rcParams.update(rcParams)

fig, (ax1, ax2, ax3) = plt.subplots(3, figsize=(7, 11), sharex=False)

# left, bottom, width, height
plot_abs_spectra_models.plot_on_axes(ax1)
ax1.set_xlabel('')
plot_abs_spectra_models_low_high_freq.plot_on_axes((ax3, ax2))
ax2.set_xlabel('')
ax3.set_xlabel('Energy (eV)')

fig.tight_layout()
fig.savefig('png/abs_spectra_total_low_high.png', dpi=500)
plt.show()