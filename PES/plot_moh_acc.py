import matplotlib.pyplot as plt
import numpy as np
plt.style.use('../style.mplstyle')

def plot_on_axes(ax, plot_legent=False):
    data = np.loadtxt('moh_acceptor_data.txt').T
    # titles = ['MM/MM-QUBEKit', 'MM/MM-QUBEKit(MK)', 'QM/MM (Solvated)', 'CAM-B3LYP/6-31G*']
    titles = ['QUBEKit/QM1', 'QUBEKit(MK)/QM1', 'AIMD/QM1', 'AIMD/QM2']
    colors = ['#BA6023', '#4D943C', '#E03223', '#0101F5']

    for i, y in enumerate(data[1:]):
        ax.plot(data[0], y/4.184, label=titles[i], color=colors[i])

    ax.hlines(0, data[0].min(), data[0].max(), linestyle='--', color='k')
    ax.set_xlim(1.3, 2.3)
    ax.set_ylim(-16, 2)
    ax.set_yticks(np.arange(-16, 2, 2))
    ax.set_xlabel('N - H Distance (Ang.)')
    ax.set_ylabel('Interaction Energy (kCal/mol)')
    # ax.set_xticklabels(ax.get_xticks(), rotation=0, weight='bold', size=12)
    if plot_legent:
        ax.legend(fontsize=plt.rcParams['axes.labelsize']*0.9)

if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(7, 5))
    plot_on_axes(ax, True)
    fig.tight_layout()
    fig.savefig(__file__.replace('.py', '.png').replace('plot_', ''), dpi=300)
    plt.show()