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

y = beta_0 + beta_1 * x + ss.norm.rvs(loc=0, scale=1, size=n) 

rss = []
slopes = np.arange(-10, 15, 0.001)
for slope in slopes:
    rss.append(np.sum((y-beta_0 - slope * x) ** 2))

# find index with lowest value of rss
ind_min = np.argmin(rss)

'''
plt.figure()
plt.plot(slopes, rss)
plt.xlabel("Slope")
plt.ylabel("RSS")
print("Estimate from the slope:", slopes[ind_min])
'''
import statsmodels.api as sm
'''
OLS = ordinary least squares
y = dependent variable
x = predictor variable

==============================================================================
Dep. Variable:                      y   R-squared:                       0.977
Model:                            OLS   Adj. R-squared:                  0.977
Method:                 Least Squares   F-statistic:                     4115.
Date:                Fri, 04 Oct 2019   Prob (F-statistic):           7.47e-82
Time:                        07:47:29   Log-Likelihood:                -130.72
No. Observations:                 100   AIC:                             265.4
Df Residuals:                      98   BIC:                             270.7
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          5.2370      0.174     30.041      0.000       4.891       5.583
x1             1.9685      0.031     64.151      0.000       1.908       2.029
==============================================================================
Omnibus:                        2.308   Durbin-Watson:                   2.206
Prob(Omnibus):                  0.315   Jarque-Bera (JB):                1.753
Skew:                          -0.189   Prob(JB):                        0.416
Kurtosis:                       3.528   Cond. No.                         11.2
==============================================================================
const coef: y-intercept (outcome when all predictors (here just x1) are 0 ) - standard linear algebra
x1 coef: for every increase of 1 of x1, y is increased 1.97
std err: how precisely the values have been estimated

sampling distributions of the parameter: collection of intercept / slope estimates from many
slighty different datasets (if you create new datasets and run the fitting multiple times)

_______95 % confidence interval________
|                                      | 
1.9675       +-       1.96   *     0.031

variance explained:
    TSS = total sum of squares (sum of squared differences between outcome yi and mean outcome)
    RSS = residual sum of squares, sum of squared differences between ŷi ("yi hat") and outcomes
    predicted by the model ŷi
    
    if the model is useful at all, RSS < TSS
r-squared statistic ("R^2 value"): proportion (0-1) of "variance explained"
    -> (TSS - RSS) / TSS
    if r-squared statistic near 0, model didnot explain variability in outcome
    therefore larger values are better: the residual sum of squares is low compared to the total sum of squares.
    

'''
mod = sm.OLS(y,x) 
est = mod.fit()
print(est.summary())

# add intercept
X = sm.add_constant(x)
mod = sm.OLS(y,X) 
est = mod.fit()


print(est.summary())