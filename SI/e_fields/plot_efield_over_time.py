import numpy as np
import matplotlib.pyplot as plt
# plt.style.use('my_style')
plt.style.use('shao-yu')

fig, ax = plt.subplots()
field_dir = 'data/'
# names = ('Ex_gs_aimd.npy', 'Ey_gs_aimd.npy', 'Ez_gs_aimd.npy')
# labels = ('$E_x$', '$E_y$', '$E_z$')
# colors = ['#0411FA', '#20B051', '#FB1900', '#FDB600', '#8172B2', '#64B5CD']


names =  ['Emag_gs_aimd.npy', 'Emag_gs_aimd_star.npy']
names += ['Ez_gs_aimd.npy', 'Ez_gs_aimd_star.npy']
labels = ('$|E|$ All', '$|E|$ 1 Axial', '$E_z$ All', '$E_z$ 1 Axial')
colors = ['blue', 'deepskyblue', 'red', 'salmon']
n_smooth = 250
nuclei = 0
for name, label, color in zip(names, labels, colors):
    data = np.load(field_dir + name)
    dim = data.shape[0]
    data_smooth = np.convolve(data[:, nuclei], np.ones(n_smooth)/n_smooth, 'same')

    times = np.arange(dim)*4/1000
    crop_range = (times > 20)*(times < 100)
    times = times[crop_range] - 20  +  4*n_smooth/1000 / 2
    data = data[crop_range]
    data_smooth = data_smooth[crop_range]
    ax.plot(times, data_smooth, label=label, color=color)


ax.hlines(0.0, times.min(), times.max(), color='k', linestyles='--', alpha=0.5)
ax.set_xlim(0, 60)
ax.set_xlabel('Simulation Time (ps)')
ax.set_ylabel('Electric Field (a.u.)')
fig_name = 'Efield_over_time.png'
ax.set_ylim(-0.05, 0.11)

ax.set_title('Electric Field at Amine Nitrogen Atom')

ax.legend(ncol=2)
fig.tight_layout()
fig.savefig(fig_name, dpi=300)
plt.show()