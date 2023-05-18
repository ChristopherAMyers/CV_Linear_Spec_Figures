import matplotlib.pyplot as plt
import numpy as np
import plot_moh_acc, plot_moh_don
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

fontsize = 14
rcParams = {
    'xtick.labelsize': fontsize,
    'ytick.labelsize': fontsize,
    'font.weight': 'bold',
    'axes.labelsize': fontsize + 2,
    'axes.labelweight': 'extra bold',
    'figure.labelsize': fontsize,
    'figure.labelweight': 'bold',
}
plt.rcParams.update(rcParams)

fig, (ax1, ax2) = plt.subplots(2, figsize=(6, 8))

# left, bottom, width, height
plot_moh_acc.plot_on_axes(ax1)
plot_moh_don.plot_on_axes(ax2)

#   add legend
handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right', fontsize=fontsize, facecolor='white', framealpha=0.8, frameon=True, bbox_to_anchor=(0.2, 0.44, 0.5, 0.5), edgecolor='white')



#   add image to plot
im_donor = plt.imread('pymol_donor.png')
im_acceptor= plt.imread('pymol_acceptor.png')

#   x, y, width, height
newax1 = fig.add_axes([0.122, 0.088 ,0.2,0.2], anchor='NE', zorder=1)
newax1.imshow(im_donor)
newax1.axis('off')
newax2 = fig.add_axes([0.724, 0.8 ,0.25,0.2], anchor='NE', zorder=1)
newax2.imshow(im_acceptor)
newax2.axis('off')

# ax1.text(0.9, 0.5, 'Amine as an Acceptor', transform=ax1.transAxes)


fig.tight_layout()
fig.savefig('../png/pes_both.png', dpi=300)
plt.show()