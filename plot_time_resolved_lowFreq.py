import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
import global_settings as GS
from os.path import join
plt.style.use('shao-yu')

#   global plot properties
fontsize = 18
rcParams = {
    'xtick.labelsize': fontsize,
    'ytick.labelsize': fontsize,
    'font.weight': 'bold',
    'axes.labelsize': fontsize + 2,
    'axes.labelweight': 'extra bold',
    'figure.labelsize': fontsize,
    'figure.labelweight': 'bold',
}
# plt.rcParams.update(rcParams)

time_step = 4
time_between_steps = (100) #  in fempto seconds
spectra_files = (
        join(GS.data_root_dir, 'time_resolved/gs-aimd_lowFreq/stripped/spectra_data.npy'), 
        join(GS.data_root_dir, 'time_resolved/gs-aimd_lowFreq/mm_star/spectra_data.npy'), 
        join(GS.data_root_dir, 'time_resolved/gs-aimd_lowFreq/mm_C4/spectra_data.npy'), 
        join(GS.data_root_dir, 'time_resolved/gs-aimd_lowFreq/mm_qm1/spectra_data.npy'), 
        join(GS.data_root_dir, 'time_resolved/gs-aimd_lowFreq/qm2/spectra_data.npy'),
    )
# spectra_files = spectra_files[0:2]
titles = ('Stripped', 
          '1 Axial HB', 
          '4 Axial Solvent', 
          'Full MM', 
          'QM+MM',
        )

def plot_on_axes(ax_grid, actually_plot=True):
    fontsize = plt.rcParams['axes.labelsize']
    if len(spectra_files) == 1:
        ax_grid = [ax_grid]

    experimental_center = 2.10
    for i, file in enumerate(spectra_files):
        print("Processing: ", file)
        data = np.load(file)
        ax = ax_grid[i]
        
        dims = data.shape
        sorted_data = np.zeros((dims[0]*dims[1], 3))
        for n, spectra in enumerate(data):
            center = spectra[:, 0][np.argmax(spectra[:, 1])]
            freq = spectra[:, 0] + (experimental_center - center)
            intensity = spectra[:, 1]/np.max(spectra[:, 1])
            times = np.ones_like(freq)*n*time_between_steps

            sorted_data[n*dims[1]:(n+1)*dims[1], 0] = freq
            #   correlation function is 8ps in length, so we shift by half that
            sorted_data[n*dims[1]:(n+1)*dims[1], 1] = times/1000 + 4.0
            sorted_data[n*dims[1]:(n+1)*dims[1], 2] = intensity

        #   the actuall contour plot part
        if actually_plot:
            ax.tricontourf(sorted_data[:, 0], sorted_data[:, 1], sorted_data[:, 2], 100, cmap='jet')


        ax.set_xlim(1.95, 2.25)
        ax.set_xticks((2.0, 2.1, 2.2))

        #   custom tick labels are needed to prevent overlaps between subplots
        # ax.set_xticklabels([' ', ' ', ' '])
        # ax.set_xlim(1.9, 2.3)
        # ax.text(0.0, -0.1, '1.9', ha='left', fontsize=fontsize, transform=ax.transAxes)
        # ax.text(0.5, -0.1, '2.1', ha='center', fontsize=fontsize, transform=ax.transAxes)
        # ax.text(1.0, -0.1, '2.3', ha='right', fontsize=fontsize, transform=ax.transAxes)

        ax.set_title(titles[i], fontsize=16)

        #   set to True to enable titles ON the contour plot itself
        if False:
            txt = ax.text(0.05, 0.27, titles[i],
                        verticalalignment='top', horizontalalignment='left',
                        transform=ax.transAxes,
                        color='white', fontsize=fontsize*1.3)
            txt.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='k')])

        if i == 0:
            ax.set_yticks([10, 20, 30, 40, 50])
            ax.set_ylabel('Time (ps)')
            
    # plt.draw()

if __name__ == "__main__":
    length = 1.5*len(spectra_files) + 0.5
    figsize = np.array((length, 2.9))*1.2
    fig, ax_grid = plt.subplots(1, len(spectra_files), figsize=figsize, sharey=True)
    plot_on_axes(ax_grid, actually_plot=False)
    fig.supxlabel('Energy (eV)')
    fig.tight_layout()
    fig.subplots_adjust(left=0.084, bottom=0.205, right=0.987, top=0.917, wspace=0.06, hspace=0.2)

    plt.subplots_adjust(wspace=0.08)    #   space between subplots
    fig.savefig('png/time_resolved_lowFreq.png', dpi=500)
    plt.show()