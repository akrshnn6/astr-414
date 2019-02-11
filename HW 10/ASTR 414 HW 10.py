# -*- coding: utf-8 -
"""
Created on Sat Apr 14 12:50:20 2018

@author: ashvi
"""

import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.nddata import Cutout2D
import time
from matplotlib_scalebar.scalebar import ScaleBar
from matplotlib_scalebar.scalebar import IMPERIAL_LENGTH

start_time = time.time()
fig = plt.figure()
red_DES = fits.open('Reduced DES image.fits')
data = red_DES[0].data

#%%
fig = plt.figure(figsize = (10,10))

position = (1132, 2225)
size = (230, 230)
cutout = Cutout2D(data, position, size)
scalebar = ScaleBar(0.26, 'in', IMPERIAL_LENGTH)
plt.gca().add_artist(scalebar)
plt.imshow(cutout.data, vmin=250, vmax=900, cmap = 'gray')
plt.title('Image Stamp')
bbox_props = dict(boxstyle="larrow", fc="white", ec="None", lw=-5)
t = plt.text(135, 140, "         Target         ", ha="center", va="center", rotation=(-50),
            size=10,
            bbox=bbox_props)
plt.savefig('Image Stamp.jpeg')

#%%
print("--- %s seconds ---" % (time.time() - start_time))