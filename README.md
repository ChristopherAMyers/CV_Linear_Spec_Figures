# CV_Linear_Spec_Figures

This repo contains the plotting scripts used to make the figures in the linear spectroscopy paper:

## Requirements
These scripts were gnerated with 
* Python 3.10.6
* Numpy 1.23.2
* Matplotlib 3.6.3

## Instructions
To generate the figures for the paper, run the following scripts:
#### Resonance-Raman Spectra
```plot_raman_models.py```
#### Simulation Models Spectral Density and Absorption Spectra
```plot_all_models.py```
#### Solvation Models Spectral Density and Absorption Spectra
```plot_all_solvent.py```
#### Low and High Frequency Filtering Absorption Spectra
```plot_abs_spectra_models_low_high_freq.py```
#### Time resolved spectra and broadening/VEE vs time
```plot_all_time_resolved.py```
#### Interaction Potential energy for methanol-CV H-bonding
```PES/plot_both.py```
#### H-Bonding distances over time
```hbonds/plot_hbonds.py```

The resulting figures will be stored in the `png` directory

## Customization
The style used for all figures is controlled by `style.mplstyle`, but some scripts use internal rcParams for that particular plot.

Global settings, including the root directory where all data is loaded from, is controlled by `global_settings.py`, which is imported by all scripts.
