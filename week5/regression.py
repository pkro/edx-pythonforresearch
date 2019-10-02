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

plt.figure()
plt.plot(x,y,"o", ms=5)
# the linear "prediction" function, see above
xx = np.array([0,10])
plt.plot(xx, beta_0 + beta_1 * xx)
plt.xlabel("x")
plt.xlabel("y")
print(f'x-mean: {x.mean()}')
print(f'y-mean: {y.mean()}')

'''
Simple linear regression:
predict quantitative variable Y on basis of single predictor variable X
Y = B0 + B1*X+E(psylon)
ŷ ("y hat") = predicted value
"hat" (^) indicates that value is estimated using data
B0 ("Beta naught")
Observations:
(x1, y1), (x2, y2), .... (xn, yn)

Estimating model parameters:
    minimizing least-square criterion

e (lower case e) = residual (Abweichung vom gewünschten Ergebnis)
ei = yi - ŷi
 -> residual of datapoint y at index i is value of datapoint minus predicted data
 
RSS = residual sum of squares

RSS = e1**2 + e2**2 + ... en**2

def compute_rss(y_estimate, y):
  return sum(np.power(y-y_estimate, 2))
def estimate_y(x, b_0, b_1):
  return b_0 + b_1 * x
rss = compute_rss(estimate_y(x, beta_0, beta_1), y)
   
'''


