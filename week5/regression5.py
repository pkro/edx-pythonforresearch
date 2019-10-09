#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 08:13:06 2019

@author: pk
"""
import numpy as np
import scipy.stats as ss
from matplotlib import pyplot as plt

# MSE: Mean Square of Error
# MSE = average of (observed outcome - prediction) ^ 2

n = 500 # data points
beta_0 = 5 # constant coefficient (y-intercept)
beta_1 = 2 # covariate
beta_2 = -1 # second covariate
np.random.seed(1)

x_1 = 10 * ss.uniform.rvs(size=n)
x_2 = 10 * ss.uniform.rvs(size=n)

y = beta_0 + beta_1 * x_1 + beta_2 * x_2 + ss.norm.rvs(loc=0, scale=1, size=n)

X = np.stack([x_1, x_2], axis=1)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.5, random_state=1)
lm = LinearRegression(fit_intercept=True)     
lm.fit(X_train, y_train)
LinearRegression(copy_X= True, fit_intercept=True, n_jobs=1, normalize=False)

print(f'intercept (beta_0) prediction: {lm.intercept_}')
print(f'coef 1 (beta_1) prediction: {lm.coef_[0]}')
print(f'coef 1 (beta_2) prediction: {lm.coef_[1]}')

print(lm.score(X_test, y_test))
