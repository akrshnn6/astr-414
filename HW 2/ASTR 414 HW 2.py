# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 12:50:12 2018
ASTR 414 Homework 2, Problem 1
@author: Ashvini Krishnan
netid: akrshnn6
"""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

fig = plt.figure()

mu = 10 # mean of distribution, E
sigma = 2 # standard deviation of distribution
nu = 100 # number of samples
# O = observed y value
plt.figure()
np.random.seed(12)
x = mu + sigma * np.random.randn(nu)

binwidth = 0.5
# the histogram of the data
n, bin_edges, patches = plt.hist(x, bins = np.arange(min(x), max(x)+ binwidth, binwidth), normed=1, facecolor='purple', alpha=0.5)
bin_centers = 0.5*(bin_edges[1:] + bin_edges[:-1])

# add a 'best fit' line
y = mlab.normpdf(bin_centers, mu, sigma)
plt.plot(bin_centers, y, 'g--')

plt.errorbar(bin_centers, y, yerr = y-n, marker = '.', fmt='g.')


plt.xlabel('X')
plt.ylabel('Probability')

count = 0
count2=0
for observed in y[range(7,12)]:
    count +=((observed-mu)/sigma)**2
    count2+=1

reduced_Chi_squared = count/(count2*nu)
plt.title('Gaussian Distribution, # of Samples = ' + str(nu))
plt.text(4,0.27,'Reduced Chi Squared:')
plt.text(4,0.24,str(reduced_Chi_squared))


# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()

#For # of Samples =1M
plt.figure()
nu=10**6
np.random.seed(12)
x = mu + sigma * np.random.randn(nu)

binwidth = 0.5
# the histogram of the data
n, bin_edges, patches = plt.hist(x, bins = np.arange(min(x), max(x)+ binwidth, binwidth), normed=1, facecolor='purple', alpha=0.5)
bin_centers = 0.5*(bin_edges[1:] + bin_edges[:-1])

# add a 'best fit' line
y = mlab.normpdf(bin_centers, mu, sigma)
plt.plot(bin_centers, y, 'g--')

plt.errorbar(bin_centers, y, yerr = y-n, marker = '.', fmt='g.')


plt.xlabel('X')
plt.ylabel('Probability')

count = 0
count2=0
for observed in y[range(7,12)]:
    count +=((observed-mu)/sigma)**2
    count2+=1

reduced_Chi_squared = count/(count2*nu)
plt.title('Gaussian Distribution, # of Samples = ' + str(nu))
plt.text(0,0.175,'Reduced Chi Squared:')
plt.text(0,0.15,str(reduced_Chi_squared))


# Tweak spacing to prevent clipping of ylabel
plt.subplots_adjust(left=0.15)
plt.show()
