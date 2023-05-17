import numpy as np
import os
import matplotlib.pyplot as plt
import global_settings

def plot_on_axes(fig, ax, inset_dims=[0.44, 0.65, 0.3, 0.25]):
    left, bottom, width, height = inset_dims
    ax2 = fig.add_axes([left, bottom, width, height])

    AU_2_CM = 219474.63
    AU_2_EV = 27.211399

    plot_files = [
        global_settings.data_root_dir + 'gs-ffmd/mm_qm1/vee_MD_spectral_density.dat',
        global_settings.data_root_dir + 'gs-ffmd-MZ/mm_qm1/vee_MD_spectral_density.dat',
        global_settings.data_root_dir + 'gs-aimd/mm_qm1/vee_MD_spectral_density.dat',
        global_settings.data_root_dir + 'gs-aimd/qm2/vee_MD_spectral_density.dat',
    ]
    labels = [
        'QUBEKit/Full MM',
        'QUBEKit(MK)/Full MM',
        'AIMD/Full MM',
        'AIMD/QM+MM',
    ]

    colors = ['#C99300', '#259225', 'red', 'Blue']

    # max_loc = exp_data[0][np.argmax(exp_data[1])]
    for file, label, color in zip(plot_files, labels, colors):
        data = np.loadtxt(file).T
        print(data.shape)
        data[0] *= AU_2_CM
        data[1] *= AU_2_EV

        ax.plot(data[0], data[1], label=label, color=color)
        ax2.plot(data[0], data[1], label=label, color=color)

    # ax.legend(loc='upper right')
    ax.set_xlabel('Wavenumber (cm⁻¹)')
    ax.set_ylabel('$J(\omega)$ (eV)')
    ax.set_ylim(0.00, 1.0)
    ax.set_xlim(0, 2000)

    ax2.set_xlim(0, 200)
    ax2.set_ylim(0, 0.05)
    ax2.set_yticks([0, 0.05])
    ax2.set_yticklabels([0.0, 0.05])
    # ax.set_yticks([])
    # ax.set_xticks([1.9, 2.1, 2.3, 2.5])

if __name__ == "__main__":
    fig, ax = plt.subplots(figsize=(8,4.5))
    plot_on_axes(fig, ax)
    fig.tight_layout()
    fig.savefig('png/spectral_density_models.png', dpi=500)
    plt.show()