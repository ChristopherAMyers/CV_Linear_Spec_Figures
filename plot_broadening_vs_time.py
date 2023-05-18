import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as PathEffects
from scipy.interpolate import interp1d
from scipy.optimize import root
import os
import global_settings


def plot_on_axes(ax):

    #   global plot properties
    fontsize = plt.rcParams['axes.labelsize']
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


    time_between_steps = (100) #  in fempto seconds
    spectra_files = (
        global_settings.data_root_dir + 'time_resolved/gs-aimd_lowFreq/stripped/spectra_data.npy', 
        global_settings.data_root_dir + 'time_resolved/gs-aimd_lowFreq/mm_4hb/spectra_data.npy', 
        global_settings.data_root_dir + 'time_resolved/gs-aimd_lowFreq/mm_C4/spectra_data.npy', 
        global_settings.data_root_dir + 'time_resolved/gs-aimd_lowFreq/mm_qm1/spectra_data.npy', 
        global_settings.data_root_dir + 'time_resolved/gs-aimd_lowFreq/qm2/spectra_data.npy'
        )
    titles = ('Stripped', 'H-Bonds', 'Pi Solvent', 'QM-1', 'QM-2')
    colors = ['black', '#21ADEF', '#D321FF', 'red', 'blue']
    

    for i, file in enumerate(spectra_files):
        print("Processing: ", file)
        data = np.load(file)

        dims = data.shape
        sorted_data = np.zeros((dims[0]*dims[1], 3))
        times = np.arange(len(data))*time_between_steps/1000 + 4
        broadenings = []
        for n, spectra in enumerate(data):
            freq = spectra[:, 0]
            intensity = spectra[:, 1]/np.max(spectra[:, 1])

            #   interpolate spectra and search for where the intensity is equal to 1/2
            interpolated_spectra = interp1d(freq, intensity - 0.5, bounds_error=False, fill_value=0.0)
            max_freq = freq[np.argmax(intensity)]
            root1 = root(interpolated_spectra, max_freq - 0.005)
            root2 = root(interpolated_spectra, max_freq + 0.005)
            broadenings.append((root2.x - root1.x))


        ax.plot(times, broadenings, color=colors[i], label=titles[i])

    ax.set_xlim(times.min(), times.max())
    ax.set_ylim(0, 0.16)
    ax.set_yticks(np.arange(0, 0.17, 0.04))
    ax.set_ylabel('Energy (eV)')
    ax.set_xlabel('Time (ps)')
    ax.legend(fontsize=fontsize, ncol=2)

if __name__ == "__main__":
    figsize = np.array((9, 5))
    fig, ax = plt.subplots(figsize=figsize, sharey=True)
    plot_on_axes(ax)
    fig.tight_layout()
    fig.savefig('png/broadening_vs_time.png', dpi=500)
    plt.show()