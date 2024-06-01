# -*- coding: utf-8 -*-
"""
Created on Mon May  1 22:56:59 2023

@author: hp
"""

import numpy as np
import matplotlib.pyplot as plt
# reading the data from the csv file
rawinput = np.genfromtxt('data5 (1).csv', delimiter=',')
# deriving the distribution of values by binning them with equal widths in the range from 2 to 5
# ohist is the numbers of entries in each bin, oedge is the bin boundaries
ohist, oedge = np.histogram(rawinput, bins=32, range=[2, 5.0])
# calculating bin centre locations and bin widths
xdst = 0.5*(oedge[1:]+oedge[:-1])
wdst = oedge[1:]-oedge[:-1]
# normalising the distribution
# ydst is a discrete PDF
ydst = ohist/np.sum(ohist)
# cdst is the cumulative distribution
cdst = np.cumsum(ydst)

plt.figure(figsize=(10, 7))
# Plotting the PDF
plt.bar(xdst, ydst, width=0.9*wdst, color='#1ac9e6')
plt.xlabel('Weights', fontsize=15)
plt.ylabel('Probability', fontsize=15)

# Finding the mean value(W)
w = np.sum(xdst*ydst)
# Printing the mean value(W)
print('Mean (W) = ', w)
# Plotting the mean value(W)
plt.plot([w, w], [0.0, max(ydst)], c='#ffa600', label='Mean value')
text = ''' Mean (W): {}'''.format(w.astype(float))
plt.text(x=w, y=max(ydst), s=text, fontsize=17, c='#ffa600', fontweight='bold')

# finding the value of X, which is the fraction of babies born weighting between 0.8W and 1.2W
hdst = ydst*((xdst >= 0.8*w) & (xdst <= 1.2*w))
plt.bar(xdst, hdst, width=0.9*wdst, color='#176ba0',
        label='Newborns between \n 0.8W and 1.2W')
x = np.sum(hdst)
# Printing the value of X
print('X =', x)
hsum = x*100.0
text = '''{}% of babies are weighed \n between 0.8W and 1.2W'''.format(
    hsum.astype(float))
plt.text(x=3.5, y=0.093, s=text, fontsize=16, c='tomato', fontweight='bold')
# Title for the graph
plt.title('Weights of Newborns', fontsize=18, fontweight='bold')
# Adding legend
plt.legend(loc='upper left', fontsize=14)
# Saving the greaph in png format
plt.savefig('plot5.png')
