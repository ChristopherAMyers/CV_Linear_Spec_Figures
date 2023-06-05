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
ax1_plots = plot_abs_spectra_models.plot_on_axes(ax1)
ax1.set_xlabel('')
plot_abs_spectra_models_low_high_freq.plot_on_axes((ax3, ax2))
ax2.set_xlabel('')
ax3.set_xlabel('Energy (eV)')

ax1.text(0.6, 0.85, '(a) Total Absorption', fontsize=18, transform=ax1.transAxes)
ax2.text(0.6, 0.85, '(b) High Frequency', fontsize=18, transform=ax2.transAxes)
ax3.text(0.6, 0.85, '(c) Low Frequency', fontsize=18, transform=ax3.transAxes)

labels = [plot.get_label() for plot in ax1_plots]
ax2.legend(ax1_plots, labels, loc='lower right')

# ax2.set_title('(b) High Frequency',)
# ax3.set_title('(c) Low Frequency', )

fig.tight_layout()
fig.savefig('png/abs_spectra_total_low_high.png', dpi=500)
plt.show()