#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 08:13:06 2019

@author: pk
"""
import numpy as np
import scipy.stats as ss
from matplotlib import pyplot as plt

beta_0 = 5
beta_1 = 2

rss = []
slopes = np.arange(-10, 15, 0.001)
for slope in slopes:
    rss.append(np.sum((y-beta_0 - slope * x) ** 2))

# find index with lowest value of rss
ind_min = np.argmin(rss)

plt.figure()
plt.plot(slopes, rss)
plt.xlabel("Slope")
plt.ylabel("RSS")
print("Estimate from the slope:", slopes[ind_min])