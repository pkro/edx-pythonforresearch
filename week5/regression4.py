#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 08:13:06 2019

@author: pk
"""
import numpy as np
import scipy.stats as ss
from matplotlib import pyplot as plt


n = 500 # data points
beta_0 = 5 # constant coefficient (y-intercept)
beta_1 = 2 # covariate
beta_2 = -1 # second covariate
np.random.seed(1)

x_1 = 10 * ss.uniform.rvs(size=n)
x_2 = 10 * ss.uniform.rvs(size=n)

y = beta_0 + beta_1 * x_1 + beta_2 * x_2 + ss.norm.rvs(loc=0, scale=1, size=n)


X = np.stack([x_1, x_2], axis=1)

from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.scatter(X[:,0], X[:,1], y, c=y)
ax.set_xlabel("$x_1$")
ax.set_ylabel("$x_2$")
ax.set_zlabel("$y$")

from sklearn.linear_model import LinearRegression

lm = LinearRegression(fit_intercept=True)
lm.fit(X,y)
LinearRegression(copy_X= True, fit_intercept=True, n_jobs=1, normalize=False)

print(f'intercept (beta_0) prediction: {lm.intercept_}')
print(f'coef 1 (beta_1) prediction: {lm.coef_[0]}')
print(f'coef 1 (beta_2) prediction: {lm.coef_[1]}')
            