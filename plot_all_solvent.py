import matplotlib.pyplot as plt
import numpy as np
import global_settings
import plot_spectral_density_solvent
import plot_abs_spectra_solvent

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

fig, (ax1, ax2) = plt.subplots(2, figsize=(7, 8))

# left, bottom, width, height
plot_spectral_density_solvent.plot_on_axes(fig, ax1, [0.45, 0.78, 0.4, 0.17])
plot_abs_spectra_solvent.plot_on_axes(ax2)

fig.tight_layout()
fig.savefig('png/all_solvent.png', dpi=500)
plt.show()