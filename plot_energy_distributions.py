import numpy as np
from scipy.stats import skew, kurtosis
import matplotlib.pyplot as plt
plt.style.use('shao-yu')
# fig, ax = plt.subplots(figsize=(8.0,4.5))


#    data file                            label          color
plot_info = (
    ('../gs-aimd/qm2/vee_traj1.dat',      'QM+MM',       'blue'),
    ('../gs-aimd/mm_qm1/vee_traj1.dat',   'Full MM',     'red'),
    ('../gs-aimd/mm_C4/vee_traj1.dat',    'Pi Solvent',  '#D321FF'),
    ('../gs-aimd/mm_4hb/vee_traj1.dat',   'HB Acceptors', '#21ADEF'),
    ('../gs-aimd/stripped/vee_traj1.dat', 'Stripped',    'green'),
)

fig, ax_grid = plt.subplots(1, len(plot_info), figsize=(14.0,4.5), sharey=True)

for ax, (file, label, color) in zip(ax_grid, plot_info):
    # if 'HB' not in label:
    #     continue
    print(file)
    data = np.loadtxt(file).T
    mean = np.mean(data[0])
    std = np.std(data[0])
    bins = np.linspace(mean - 0.3, mean + 0.3, 41)
    counts, bin_edges = np.histogram(data[0], bins, density=True)
    # bin_centers = 0.5*(bin_edges[0:-1] + bin_edges[1:])
    # ax.plot(bin_centers, counts, color=color, label=label)

    ax.hist(data[0], bins=bins, label=label, color=color, density=True, alpha=1, edgecolor='k')

    x = np.linspace(mean - 4*std, mean + 4*std, 1000)
    gauss = 1.0/np.sqrt(2*np.pi*std**2)*np.exp(-(x - mean)**2/(2*std**2))
    ax.plot(x, gauss, color='black')

    ax.set_xlim(mean - 0.3, mean + 0.3)
    ax.set_title(label)

    sk = skew(data[0])
    kurt = kurtosis(data[0])
    ax.text(0.05, 0.9, '$\mu_1 = ${:5.2f}'.format(mean), transform = ax.transAxes, size=14)
    ax.text(0.05, 0.8, '$\sigma = $  {:5.2f}'.format(std), transform = ax.transAxes, size=14)
    ax.text(0.60, 0.9, '$\\tilde{{\mu}}_3 = ${:5.2f}'.format(sk), transform = ax.transAxes, size=14)
    ax.text(0.60, 0.8, '$\\tilde{{\mu}}_4 = ${:5.2f}'.format(kurt), transform = ax.transAxes, size=14)


fig.supxlabel('Energy (eV)')
fig.supylabel('Density (eV$^{-1}$)')
fig.tight_layout()
plt.subplots_adjust(wspace=0.0,
                    hspace=0.05)
fig.savefig('png/energy_distributions.png', dpi=300)
plt.show()