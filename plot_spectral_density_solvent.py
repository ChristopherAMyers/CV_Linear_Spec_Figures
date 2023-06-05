import numpy as np
from os.path import join
import matplotlib.pyplot as plt
import global_settings as GS
from scipy.integrate import simpson

def plot_on_axes(fig, ax, inset_dims=[0.52, 0.55, 0.4, 0.35]):
    left, bottom, width, height = inset_dims
    ax2 = fig.add_axes([left, bottom, width, height])


    AU_2_CM = 219474.63
    AU_2_EV = 27.211399

    plot_files = [
        join(GS.data_root_dir, 'gs-aimd/qm2/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_qm1/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_C4/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_star/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_4hb/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/stripped/vee_MD_spectral_density.dat'),
    ]
    labels = [
        'QM+MM',
        'Full MM',
        '1 Axial HB',
        '4 Axial Solvent',
        '4 Peripheral HB',
        'Stripped'
    ]
    colors = ['blue', 'red', '#D321FF', 'orange', '#21ADEF', 'black']

    # max_loc = exp_data[0][np.argmax(exp_data[1])]
    for file, label, color in zip(plot_files, labels, colors):
        data = np.loadtxt(file).T
        data[0] *= AU_2_CM
        data[1] *= AU_2_EV

        ax.plot(data[0], data[1], label=label, color=color)
        ax2.plot(data[0], data[1], label=label, color=color)

        #   compute reorganization energy and Stokes shift
        # integrand = np.zeros_like(data[0])
        # integrand[1:] = data[1, 1:]/data[0, 1:]
        # ax.plot(integrand)
        # reorg_engy = simpson(integrand, data[0])/np.pi
        # print('{:>20s}: {:10.5f}'.format(label, reorg_engy))

    # plt.show()
    # ax.legend(loc='upper right')
    ax.set_xlabel('Wavenumber (cm⁻¹)')
    ax.set_ylabel('$J(\omega)$ (eV)')
    ax.set_ylim(0.00, 1.0)
    ax.set_xlim(0, 2000)

    ax2.set_xlim(0, 200)
    ax2.set_ylim(0, 0.05)
    ax2.set_yticks([0, 0.05])
    ax2.set_yticklabels([0.0, 0.05])
    ax2.set_xticks([0, 100, 200])
    # ax.set_yticks([])
    # ax.set_xticks([1.9, 2.1, 2.3, 2.5])

if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(8,4.5))
    plot_on_axes(fig, ax)
    fig.savefig('png/spectral_density_solvent.png', dpi=500)
    fig.tight_layout()
    plt.show()