# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 14:26:04 2018

@author: Ashvini
"""

from astropy.io import fits
from astropy.io import ascii
from astropy.table import Table
import numpy as np
from astropy.cosmology import LambdaCDM
from astropy import units as u
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

lab = fits.open('lab1-data.fits')
data = Table(lab[1].data)

data2 = Table(lab[1].data)
data2.remove_column('REDSHIFT')

data2['name'] = np.arange(len(data))
search = data2[('name','RA','DEC')]

ascii.write(data, 'data.txt', overwrite = True)
ascii.write(search, 'data2.txt', overwrite = True)

sdss = ascii.read('star_data.csv')

i = 0
while i < len(data2):
    if data2['name'][i] not in sdss['NAME']:
        data.remove_row(i)
    i+=1
        
cosmo = LambdaCDM(H0=70 * u.km / u.s / u.Mpc, Om0=0.3, Ode0=0.7)

luminosity_distances = []
for r in data["REDSHIFT"]:
    luminosity_distances.append(cosmo.luminosity_distance(r))

DM = []
for d in luminosity_distances:
    DM.append((5*np.log10(d/(10 * u.pc))))

absMag = []
for mag, dist_mod in zip(sdss['modelMag_i'], DM):
    absMag.append(mag - dist_mod.value)
#%%
ra = data['RA']
dec = data['DEC']

def projection(ra, dec, proj = 'aitoff', org = 0, facecolor = 'LightCyan', mcolor = 'b', alpha = 0.3, title = ''):
    ra = np.remainder(ra+360-org,360) # shift RA values
    ra[ra>180] -=360    # scale conversion to [-180, 180]
    ra=-ra    # reverse the scale: East to the left
    tick_labels = np.array([150, 120, 90, 60, 30, 0, 330, 300, 270, 240, 210])
    tick_labels = np.remainder(tick_labels+360+org,360)
 
    #1 hr = 15 deg    
    labels =[]
    for label in tick_labels: #in degrees, want hrs
        labels.append(str(int(label*(1/15))) + '$^h$')
        
    fig = plt.figure(figsize=(8,4.2))
    ax = fig.add_subplot(111, projection= proj, facecolor = facecolor)
    plt.plot(np.radians(ra),np.radians(dec), 'o', color = mcolor , markersize=4, alpha=alpha)  # convert degrees to radians
    ax.set_title(title, y=1.08, fontsize = 14)        
    ax.set_xticklabels(tick_labels, visible = False)
    ax.set_xticklabels(labels, visible = True)
    ax.set_xlabel("RA")
    ax.xaxis.label.set_fontsize(12)
    ax.set_ylabel("Dec")
    ax.yaxis.label.set_fontsize(12)
    ax.grid(True)
    return fig

projection(ra, dec, org = 120, facecolor = 'azure', mcolor = 'deeppink', alpha = 0.5, title = 'Aitoff Projection of Quasar Sample').savefig('Aitoff Projection.png')
#%%
fig=plt.figure(figsize=(8,8))
gs=GridSpec(6,6) # 6 rows, 6 columns

ax1=fig.add_subplot(gs[0:5:,0]) #histogram of absolute magnitude i
ax2=fig.add_subplot(gs[5,1:6]) #histogram of redshift
ax3=fig.add_subplot(gs[0:5, 1:6]) #redshift vs magnitude i scatterplot

ax3.plot(data['REDSHIFT'], absMag, 'o', color = 'deeppink', markersize=5, alpha=0.5)

ax2.hist(data['REDSHIFT'], bins = 75, color = 'springgreen', alpha=0.5, histtype='bar', ec='g')

ax1.hist(absMag, bins = 50, orientation = 'horizontal', color = 'springgreen', alpha=0.5, histtype='bar', ec='g')

ax3.invert_yaxis()
ax1.invert_yaxis()
plt.title('Redshift vs I-band Absolute Magnitude', y=1.02,
          fontsize = 14)
ax1.set_xlabel('          N',
               fontsize = 14)
ax1.set_ylabel('$M_{i}$', fontsize = 14)
ax2.set_xlabel('Redshift (z)', fontsize = 14)
ax3.grid(which ='both')

ax1.xaxis.tick_top()
ax2.yaxis.tick_right()

x_major_ticks = np.arange(0,5.25, 1)
x_minor_ticks = np.arange(0,5.25, 0.2)

y_major_ticks = np.arange(-31., -21.75, 1)
y_minor_ticks = np.arange(-31, -21.75, 0.2)

ax1.set_ylim(-22, -30)
ax3.set_ylim(-22, -30)

ax2.set_xlim(0, 5)
ax3.set_xlim(0, 5)

ax2.set_ylim(0,45)
ax1.set_xlim(0,50)

ax1.set_xlim(0,60)
ax2.set_ylim(0,50)

ax1.tick_params(which = 'major', direction = 'inout', length = 12)
ax1.tick_params(which = 'minor', direction = 'inout', length = 6) 

ax2.tick_params(which = 'major', direction = 'inout', length = 12)
ax2.tick_params(which = 'minor', direction = 'inout', length = 6)

ax3.tick_params(which = 'major', direction = 'inout', length = 24)
ax3.tick_params(which = 'minor', direction = 'inout', length = 6)

ax2.set_xticks(x_major_ticks)
ax2.set_xticks(x_minor_ticks, minor=True)

ax1.set_yticks(y_major_ticks)
ax1.set_yticks(y_minor_ticks, minor=True)

ax2.set_xticks(x_major_ticks)
ax2.set_xticks(x_minor_ticks, minor=True)

ax3.set_yticks(y_major_ticks)
ax3.set_yticks(y_minor_ticks, minor=True)

ax3.set_xticks(x_major_ticks)
ax3.set_xticks(x_minor_ticks, minor=True)

xticklabels = ax3.get_xticklabels()
plt.setp(xticklabels, visible=False)

yticklabels = ax3.get_yticklabels()
plt.setp(yticklabels, visible=False)

plt.tight_layout(pad=0, w_pad=-1.8
                 , h_pad=-2.2)


fig.savefig('Redshift vs Absolute Magnitude.png')
