# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:15:06 2018
ASTR 414 HW2, Problem 2
@author: Ashvini Krishnan
netid: akrshnn6
"""
import numpy as np
import matplotlib.pyplot as plt

"""Part a:"""
#Function to generate random true distances to uniformly distributed supernovas
def truedist():
#Generation of random radii with a uniform distribution
    radii = (np.random.uniform(low=0, high = 1, size = 100))
#Stretch those radii to the spherical probability distribution and return the distances
    true_distances = []
    for value in radii:
        true_distances.append(((8*value)**(1/3))*10**3)
    return true_distances
    
sum=0
count = 0
#Find the average of many averages of different random uniformly distributed distances for a "super average"
for value in range(0, 100000):
         sum+=np.average(truedist())
         count+=1

avg = str(sum/count)
print("Average True Distance: " + avg)


"""Part b:"""
true_distances = truedist()
m = []
count = 0
abs_magnitudes = np.random.normal(-19, 1, 100) 
for i in range(len(true_distances)):
    m.append(5*np.log10(true_distances[i]*10**5)+abs_magnitudes[i])

count = 0
app_mags = []
dist = []
for i in range(len(true_distances)):
    if m[i]<=20:
        app_mags.append(m[i])
        dist.append(true_distances[i])
        count+=1
        
print("Original Average Apparent Magnitude: " + str(np.average(m)))
print("Detected Average Apparent Magnitude: " + str(np.average(app_mags)))
print("Number of Detected Supernovas: " + str(count))

        
plt.figure()
plt.scatter(dist, app_mags)
plt.gca().invert_yaxis()
plt.title('True Distance (Mpc) vs Apparent Magnitude')
plt.xlabel('True Distance (Mpc)')
plt.ylabel('Apparent Magnitude')
plt.xlim(0, 2000)

"""Part c:"""
obs_distances = []
for i in app_mags:
    obs_distances.append((10**(((i+19)/5)+1))*10**-6)
    
velocity = []
for i in obs_distances:
    velocity.append(72*i)

plt.figure()
plt.scatter(obs_distances, velocity)
plt.title('Observed Distance (Mpc) vs Velocity')
plt.xlabel('Observed Distance (Mpc)')
plt.ylabel('Velocity')