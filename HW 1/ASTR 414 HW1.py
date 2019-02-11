# -*- coding: utf-8 -*-
"""
Spyder Editor
ASTR 414 HW1 Ashvini Krishnan
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# wavelength range, m
lmin_wv, lmax_wv =10**-12, 10**3
# frequency range, Hz
lmin_nu, lmax_nu = 10**5.5, 10**20.5
# energy range, eV
lmin_eV, lmax_eV = 10**-9, 10**6 

# Setup a plot such that only the bottom spine is shown
def setup(ax):
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.yaxis.set_major_locator(ticker.NullLocator())
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00)
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', width=0.75)
    ax.tick_params(which='minor', length=2.5)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 1)
    ax.patch.set_alpha(0.0)
    
x = [10^-2,10^-3,10^-4,10^-5,10^-6]

plt.figure(figsize=(8, 6))
n = 8
plt.plot(x,x)

#Wavelength
ax = plt.subplot(n, 1, 2)
setup(ax)
ax.set_xlim(lmax_wv, lmin_wv)
ax.set_xscale('log')
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=20))
ax.text(0.0, 0.1, "Wavelength (m)",
        fontsize=15, transform=ax.transAxes)


bbox_props = dict(boxstyle="rarrow,pad=0.3", fc="cyan", ec="b", lw=2)
t = ax.text(10**-11.5, 1.2, "γ Rays", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

bbox_props = dict(boxstyle="rarrow,pad=0.3", fc="cyan", ec="b", lw=2)
t = ax.text(10**-10.8, 0.7, "    Hard X-Rays  ", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.3", fc="cyan", ec="b", lw=2)
t = ax.text(10**-8.7, 1.2, "    Soft X-Rays   ", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.3", fc="cyan", ec="b", lw=2)
t = ax.text(10**-7.3, 0.7, "Ultraviolet", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.3", fc="cyan", ec="b", lw=2)
t = ax.text(10**-4.72, 0.7, "        Infrared        ", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.3", fc="cyan", ec="b", lw=2)
t = ax.text(10**-3.2, 1.2, "             Microwaves             ", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

bbox_props = dict(boxstyle="larrow,pad=0.3", fc="cyan", ec="b", lw=2)
t = ax.text(10, 0.7, "             Radio Waves             ", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.3", fc="None", ec="b", lw=0)
t = ax.text(10**-6.3, 1.07, "Visible", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)


bbox_props = dict(boxstyle="square,pad=0.3", fc="None", ec="b", lw=0)
t = ax.text(10**-4.7, 2, "Electromagnetic Spectrum", ha="center", va="center", rotation=0,
            size=20,
            bbox=bbox_props)

ylim = .5
ymax = 0.9
plt.axvline(x=7.5*10**(-7.05), ymin= ylim, ymax=ymax, color='red', linestyle='-')
plt.axvline(x=7.05*10**(-7.05), ymin = ylim, ymax=ymax, color='orange', linestyle='-')
plt.axvline(x=6.6*10**(-7.05), ymin = ylim,  ymax=ymax, color='yellow', linestyle='-')
plt.axvline(x=6.15*10**(-7.05), ymin = ylim, ymax=ymax, color='green', linestyle='-')
plt.axvline(x=5.7*10**(-7.05), ymin = ylim, ymax=ymax, color='blue', linestyle='-')
plt.axvline(x=5.25*10**(-7.05), ymin = ylim, ymax=ymax, color='indigo', linestyle='-')
plt.axvline(x=4.8*10**(-7.05), ymin = ylim, ymax=ymax, color='violet', linestyle='-')

#Frequency
ax = plt.subplot(n, 1, 3)
setup(ax)
ax.set_xlim(lmin_nu, lmax_nu)
ax.set_xscale('log')
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=20))
ax.text(0.0, 0.1, "Frequency (Hz)",
        fontsize=15, transform=ax.transAxes)

bbox_props = dict(boxstyle="square,pad=0.3", fc="White", ec="g", lw=1)
t = ax.text(10**5.5, 0.85, "1km", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

t = ax.text(10**8.5, 0.85, "1m", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

t = ax.text(10**11.5, 0.85, "1mm", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

t = ax.text(10**14.5, 0.85, "1μm", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

t = ax.text(10**17.5, 0.85, "1nm", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

t = ax.text(10**18.5, 0.85, " 1Å ", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

t = ax.text(10**20.5, 0.85, "1pm", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

#Energy
ax = plt.subplot(n, 1, 4)
setup(ax)
ax.set_xlim(lmin_eV, lmax_eV)
ax.set_xscale('log')
ax.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=20))
ax.text(0.0, 0.1, "Energy (eV)",
        fontsize=15, transform=ax.transAxes)

bbox_props = dict(boxstyle="square,pad=0.3", fc="White", ec="g", lw=1)
t = ax.text(10**-8.5, 0.85, "1MHz", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.3", fc="White", ec="g", lw=1)
t = ax.text(10**-5.5, 0.85, "1GHz", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.3", fc="White", ec="g", lw=1)
t = ax.text(10**0, -0.4, "1eV", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.3", fc="White", ec="g", lw=1)
t = ax.text(10**2, -0.4, "1keV", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

bbox_props = dict(boxstyle="square,pad=0.3", fc="White", ec="g", lw=1)
t = ax.text(10**6, -0.4, "1MeV", ha="center", va="center", rotation=0,
            size=10,
            bbox=bbox_props)

# Push the top of the top axes outside the figure because we only show the
# bottom spine.
plt.subplots_adjust(left=0.05, right=0.95, bottom=0.05, top=1.05)

x = [1,2,3]

plt.show()