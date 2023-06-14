import numpy as np
from os.path import join
import matplotlib.pyplot as plt
import global_settings as GS
from scipy.integrate import simpson
from scipy.interpolate import interp1d

def run():

    AU_2_CM = 219474.63
    AU_2_EV = 27.211399

    plot_files = [
        join(GS.data_root_dir, 'gs-ffmd/mm_qm1/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-ffmd-MZ/mm_qm1/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/stripped/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_4hb/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_star/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_C4/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_qm1/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/qm2/vee_MD_spectral_density.dat'),
    ]
    plot_files_LF = [
        join(GS.data_root_dir, 'gs-ffmd/mm_qm1_low_freq/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-ffmd-MZ/mm_qm1_low_freq/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/stripped_low_freq/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_4hb_low_freq/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_star_low_freq/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_C4_low_freq/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/mm_qm1_low_freq/vee_MD_spectral_density.dat'),
        join(GS.data_root_dir, 'gs-aimd/qm2_low_freq/vee_MD_spectral_density.dat'),
    ]
    labels = [
        'QUBEKit',
        'revQUBEKit',
        'Stripped',
        '4 Peripheral HB',
        '4 Axial Solvent',
        '1 Axial HB',
        'Full MM',
        'QM+MM',
    ]
    fig, ax = plt.subplots()

    # max_loc = exp_data[0][np.argmax(exp_data[1])]
    for file, label in zip(plot_files, labels):
        data = np.loadtxt(file).T
        data[0] *= 1
        data[1] *= 1

        print("FILE: ", file.replace('/vee_MD_spectral_density.dat', ''))

        J_interp = interp1d(data[0], data[1], kind='cubic')
        # ax.scatter(data[0], data[1], marker='.')
        new_x = np.linspace(0, data[0].max()/1000, 10000)
        # new_x = data[0]
        new_y = J_interp(new_x)
        # ax.plot(new_x, new_y)


        #   compute reorganization energy and Stokes shift
        integrand = np.zeros_like(data[0])
        integrand[1:] = data[1, 1:]/data[0, 1:]
        integrand[0] = integrand[1]
        # integrand = data[1, 1:]
        # if label == 'QUBEKit' == 0:
        #     integrand *= 2

        ax.plot(data[0]*AU_2_CM, integrand, label=label)
        reorg_engy = simpson(integrand, data[0])/np.pi
        print('{:>20s}: {:10.5f}'.format(label, reorg_engy*AU_2_EV))

    ax.plot((0, new_x.max()), (0, new_x.max()), color='k')
    ax.legend()
    # ax.set_xlim(0, 300)
    ax.set_ylim(0)
    plt.show()


if __name__ == '__main__':
    run()