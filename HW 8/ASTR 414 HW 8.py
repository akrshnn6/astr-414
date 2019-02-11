# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 17:30:15 2018

@author: ashvi
"""

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from matplotlib.colors import LogNorm
import time
start_time = time.time()

bias = fits.open('D_n20131112t1127_c13_r1472p01_biascor.fits')
flat = fits.open('D_n20131112t1127_r_c13_r1472p01_dflatcor.fits')
data = fits.open('DECam_00380036_09.fits')


#%%

files = [flat, data, bias]
filenames = ['flat', 'data', 'bias']
colors = ['gray','gray', 'white']
alpha = [0.9, 0.5, 1]
ec = ['gray', 'k', 'k']

#%%
for f, n in zip(files, filenames):
    fig = plt.figure(figsize = (3.2, 5))
    plt.imshow(f[0].data, cmap = 'gray', norm = LogNorm())
    plt.title(("%s%s" % (n[0].upper(), n[1:])) + ' Frame')
    fig.savefig(("%s%s" % (n[0].upper(), n[1:]))+ ' image.png')

#%%
    
files1 = []
for f in files:
    files1.append(f[0].data.flat)

def normalize(v):
    return (v-np.min(v))/(np.max(v)-np.min(v))
#    return v/np.max(v)

files = files1
files1 = []
for f in files:
    files1.append(normalize(f))
files = files1
#%%
nbins = 200
fig = plt.figure(figsize = (10, 5))
for f, n, c, a, e in zip(files, filenames, colors, alpha, ec):
    plt.hist(f, nbins, log = True, color = c, alpha = a, ec= e, label = n)
plt.title('Histograms of Pixel Values')
plt.xlabel('Normalized Pixel Values of Data, Bias, and Flat Frames')
plt.ylabel('Log(Pixel)')
plt.text(0.92, 10**5.3, 'Nbins = ' + str(nbins))
plt.legend(loc = 'upper right')
plt.savefig('hw8 histogram.png')

#%%
print("--- %s seconds ---" % (time.time() - start_time))