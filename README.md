# CV_Linear_Spec_Figures

This repo contains the plotting scripts used to make the figures in the linear spectroscopy paper:

### Requirements
These scripts were gnerated with 
* Python 3.10.6
* Numpy 1.23.2
* Matplotlib 3.6.3

### Instructions
To generate the figures for the paper, run the following scripts:
* plot_raman_models.py
* plot_all_models.py
* plot_all_solvent.py
* plot_abs_spectra_models_low_high_freq.py
* plot_all_time_resolved.py
* PES/plot_both.py
* hbonds/plot_hbonds.py

The resulting figures will be stored in the `png` directory

### Customization
The style used for all figures is controlled by `style.mplstyle`, but some scripts use internal rcParams for that particular plot.

Global settings, including the root directory where all data is loaded from, is controlled by `global_settings.py`, which is imported by all scripts.
