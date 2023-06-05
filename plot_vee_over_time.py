import numpy as np
import os
import matplotlib.pyplot as plt
import global_settings as GS

plot_files = [
    os.path.join(GS.data_root_dir + 'gs-aimd/stripped/vee_traj1.dat'), 
    os.path.join(GS.data_root_dir + 'gs-aimd/mm_4hb/vee_traj1.dat'), 
    os.path.join(GS.data_root_dir + 'gs-aimd/mm_C4/vee_traj1.dat'), 
    os.path.join(GS.data_root_dir + 'gs-aimd/mm_star/vee_traj1.dat'), 
    os.path.join(GS.data_root_dir + 'gs-aimd/mm_qm1/vee_traj1.dat'), 
    os.path.join(GS.data_root_dir + 'gs-aimd/qm2/vee_traj1.dat'),
]
titles = ('Stripped', '4 Peripheral HB', '4 Axial Solvent', '1 Axial Solvent', 'MM', 'QM+MM')
colors = ['black', '#21ADEF', '#D321FF', 'orange', 'red', 'blue']

def plot_on_axes(ax):

    for file, label, color in zip(plot_files, titles, colors):
        print("Processinf: ", file)
        data = np.loadtxt(file).T
        n_smoth = 2000
        energies = []
        stds = []
        for n in range(len(data[0]) - n_smoth):
            energies.append(np.mean(data[0, n:n+n_smoth]))
            stds.append(np.std(data[0, n:n+n_smoth]))
        energies, stds = np.array(energies[:-1]), np.array(stds[:-1])
        times = np.arange(0, len(energies))*4/1000 + 4

        ax.plot(times, energies, label=label, color=color)
        # ax.fill_between(times, energies + stds, energies - stds, alpha=0.3, color=color)

    ax.set_xlabel('Time (ps)')
    ax.set_ylabel('Energy (eV)')

if __name__ == "__main__":
    fig, ax = plt.subplots()
    plot_on_axes(ax)
    ax.legend(loc='upper left')
    fig.tight_layout()
    fig.savefig('png/vee_time.png', dpi=300)
    plt.show()