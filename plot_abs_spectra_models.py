import numpy as np
import os
import matplotlib.pyplot as plt
import global_settings as GS

def plot_on_axes(ax: plt.Axes) -> list:

    plot_files = [
        os.path.join(GS.data_root_dir, 'gs-ffmd/mm_qm1/vee_MD_cumulant_spectrum.dat'),
        os.path.join(GS.data_root_dir, 'gs-ffmd-MZ/mm_qm1/vee_MD_cumulant_spectrum.dat'),
        os.path.join(GS.data_root_dir, 'gs-aimd/mm_qm1/vee_MD_cumulant_spectrum.dat'),
        os.path.join(GS.data_root_dir, 'gs-aimd/qm2/vee_MD_cumulant_spectrum.dat'),
    ]
    labels = [
        'QUBEKit/MM',
        'revQUBEKit/MM',
        'AIMD/MM',
        'AIMD/QM+MM',
    ]
    colors = ['#C99300', '#259225', 'red', 'Blue']

    plots = []

    exp_data = np.loadtxt('experimental_abs.txt').T
    # ax.plot(exp_data[0], exp_data[1], color='grey', linestyle=(0, (1, 1)), label='Experiment')
    fill = ax.fill_between(exp_data[0], 0, exp_data[1], color='#BFC1C1', linestyle=(0, (1, 1)), label='Experiment')
    plots.append(fill)

    max_loc = exp_data[0][np.argmax(exp_data[1])]
    for file, label, color in zip(plot_files, labels, colors):
        data = np.loadtxt(file).T
        data[1] /= data[1].max()

        if max_loc is None:
            max_loc = data[0][data[1].argmax()]
        else:
            this_max = data[0][data[1].argmax()]
            data[0] -= (this_max - max_loc)

        line = ax.plot(data[0], data[1], label=label, color=color)
        plots.append(line[0])

    
    ax.set_xlabel('Energy (eV)')
    ax.set_ylabel('Intensity (arb. units)')
    ax.set_ylim(-0.005, 1.05)
    ax.set_xlim(1.9, 2.5)
    ax.set_yticks([])
    # ax.set_xticks([1.5, 1.7, 1.9, 2.1, 2.3, 2.5])
    ax.set_xticks([1.9, 2.1, 2.3, 2.5])

    return plots

if __name__ == "__main__":
    fig, ax = plt.subplots(figsize=(8.0,4.5))
    plot_on_axes(ax)
    ax.legend(loc='upper right', fontsize=plt.rcParams['axes.labelsize']*0.9)
    fig.tight_layout()
    fig.savefig('png/abs_spectra_models.png', dpi=500)
    plt.show()