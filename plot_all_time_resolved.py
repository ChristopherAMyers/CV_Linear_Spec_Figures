import matplotlib.pyplot as plt
import numpy as np
import global_settings
import plot_time_resolved_lowFreq
import plot_broadening_vs_time
import plot_vee_over_time

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

fig = plt.figure(figsize=np.array((11, 14))*0.7, layout='constrained')
subfigs = fig.subfigures(nrows=2, ncols=1, height_ratios=[1,1.8])

#   time resolved low-frequency broadening
n_cols = len(plot_time_resolved_lowFreq.spectra_files)
ax_grid = subfigs[0].subplots(nrows=1, ncols=n_cols, sharey=True)
ax_grid[0].set_yticks([10, 20, 30, 40, 50])
plot_time_resolved_lowFreq.plot_on_axes(ax_grid, actually_plot=True)
subfigs[0].supxlabel('Energy (eV)', fontsize=plt.rcParams['axes.labelsize'], ha='center')
# subfigs[0].text(0.52, -0.02, 'Energy (eV)', ha='center', va='center', fontsize=fontsize*1.2)
ax_grid[0].set_title('\n\n' + ax_grid[0].get_title())


#   Boradening over time
ax_time = subfigs[1].subplots(2, 1, sharex=True)
subfigs[1].subplots_adjust(hspace=-1)
plot_broadening_vs_time.plot_on_axes(ax_time[0])
ax_time[0].set_xlabel('')
ax_time[0].text(0.03, 0.85, "(B) Low-Frequency Broadening", transform=ax_time[0].transAxes, fontsize=18)

#   VEE over time
# ax_evt = subfigs[2].subplots()
plot_vee_over_time.plot_on_axes(ax_time[1])
ax_time[1].set_xlim(4, 56)
ax_time[1].set_xticks([10, 20, 30, 40, 50])
ax_time[1].legend(ncols=2, loc=(0.03, 0.2), fontsize=16)
ax_time[1].text(0.03, 0.85, "(C) VE Energies", transform=ax_time[1].transAxes, fontsize=18)


subfigs[0].text(0.021, 2.27, '(A) Low-Frequency Absorption Spectra over Time', transform=ax_time[0].transAxes, fontsize=18)



# plt.subplots_adjust(wspace=0.08, hspace=1, bottom=0.155, left=0.09, right=0.974, top=0.95) 
# plt.subplot_tool()
fig.savefig('png/all_time_resolved.png', dpi=300)
plt.show()