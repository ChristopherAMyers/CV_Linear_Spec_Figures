import matplotlib.pyplot as plt
import os

script_dir = os.path.abspath(os.path.dirname(__file__))
plt.style.use(script_dir + '/style.mplstyle')

data_root_dir = '/Users/cmyers/Library/CloudStorage/OneDrive-UniversityofCaliforniaMerced/crysel_violet/spectra/'

os.makedirs('png', exist_ok=True)