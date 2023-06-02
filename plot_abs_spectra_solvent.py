import numpy as np
import os
import matplotlib.pyplot as plt
import global_settings as GS

def plot_on_axes(ax):

    plot_files = [
        os.path.join(GS.data_root_dir, 'gs-aimd/qm2/vee_MD_cumulant_spectrum.dat'),
        os.path.join(GS.data_root_dir, 'gs-aimd/mm_qm1/vee_MD_cumulant_spectrum.dat'),
        os.path.join(GS.data_root_dir, 'gs-aimd/mm_C4/vee_MD_cumulant_spectrum.dat'),
        os.path.join(GS.data_root_dir, 'gs-aimd/mm_star/vee_MD_cumulant_spectrum.dat'),
        os.path.join(GS.data_root_dir, 'gs-aimd/mm_4hb/vee_MD_cumulant_spectrum.dat'),
        os.path.join(GS.data_root_dir, 'gs-aimd/stripped/vee_MD_cumulant_spectrum.dat'),
    ]
    labels = [
        'QM+MM',
        'Full MM',
        'Pi Solvent',
        'Star Methanol',
        'HB Aceptors',
        'Stripped'
    ]
    colors = ['blue', 'red', '#D321FF', 'orange', '#21ADEF', 'black']

    exp_data = np.loadtxt('experimental_abs.txt').T
    ax.fill_between(exp_data[0], 0, exp_data[1], color='#BFC1C1', linestyle=(0, (1, 1)), label='Experiment')

    max_loc = exp_data[0][np.argmax(exp_data[1])]
    for file, label, color in zip(plot_files, labels, colors):
        print(file)
        data = np.loadtxt(file).T
        data[1] /= data[1].max()

        if max_loc is None:
            max_loc = data[0][data[1].argmax()]
        else:
            this_max = data[0][data[1].argmax()]
            data[0] -= (this_max - max_loc)

        ax.plot(data[0], data[1], label=label, color=color)

    ax.legend(loc='upper right', fontsize=plt.rcParams['axes.labelsize']*0.9)
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Intensity (arb. units)')
    ax.set_ylim(-0.005, 1.05)
    ax.set_xlim(1.9, 2.5)
    ax.set_yticks([])
    # ax.set_xticks([1.5, 1.7, 1.9, 2.1, 2.3, 2.5])
    ax.set_xticks([1.9, 2.1, 2.3, 2.5])

if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(8.0,4.5))
    plot_on_axes(ax)
    fig.tight_layout()
    fig.savefig('png/abs_spectra_solvent.png', dpi=500)
    plt.show()