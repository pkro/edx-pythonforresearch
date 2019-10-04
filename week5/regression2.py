#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 08:13:06 2019

@author: pk
"""
import numpy as np
import scipy.stats as ss
from matplotlib import pyplot as plt

n = 100 # data points
beta_0 = 5 # constant coefficient
beta_1 = 2 # 
np.random.seed(1)
x = 10 * ss.uniform.rvs(size=n) # random uniform distribution between 1-10
'''
"fake" target observatons
basically a linear function y = mx + b
where b = beta_0 (y-intercept) and m = beta_1 (slope)
then adding noise using ss.norm.rvs to get "fake outcomes"
'''
y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale=1, size=n) 

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