#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 08:13:06 2019

@author: pk
"""
import numpy as np
import scipy.stats as ss
from matplotlib import pyplot as plt

'''
simulate data froom 2 normal distributions



'''
dist1_middle = -5
dist2_middle = 5

dist1_size = 50
dist2_size = 50

dist1 = np.random.normal(loc=dist1_middle, scale=5.0, size=dist1_size)
                         
print(dist1)

plt.plot(dist1, 'ro')