#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:21:36 2019

@author: pk
"""
import random
from collections import Counter

import numpy as np
from scipy import stats as ss
from matplotlib import pyplot as plt


def distance(p1, p2):
    return np.sqrt(np.sum(np.power(p1-p2, 2)))

def majority_vote(votes):
    vote_counts = dict(Counter(votes))
    winners = []
    max_count = max(vote_counts.values())

    for key, val in vote_counts.items():
        if val == max_count:
            winners.append(key)
    
    return random.choice(winners)

def majority_vote_short(votes):
    return ss.mstats.mode(votes)[0]

def find_nearest_neighbors(p, points, k=5):
    distances = np.array([distance(x, p) for x in points])
    indices = np.argsort(distances)
    # closest = list(zip(points[indices[:k]], distances[indices[:k]]))
    # return closest
    return indices[:k]

def knn_predict(p, points, outcomes, k=5):
    ind = find_nearest_neighbors(p, points, k)
    return majority_vote(outcomes[ind])

def generate_synth_data(n = 50):
    ''' generate two sets of points from bivariate distribution'''
    class1_points = ss.norm(0,1).rvs((n,2))
    class2_points = ss.norm(1,1).rvs((n,2))
    points = np.concatenate((class1_points, class2_points), axis=0)
    outcomes = np.concatenate((np.repeat(0,n), np.repeat(1,n)))
    
    return points, outcomes

def make_prediction_grid(predictors, outcomes, limits, h, k):
    ''' classify each point in prediction grid'''
    (x_min, x_max, y_min, y_max) = limits
    xs = np.arange(x_min, x_max, h)
    ys = np.arange(y_min, y_max, h)
    xx, yy = np.meshgrid(xs, ys)
    
    prediction_grid = np.zeros(xx.shape, dtype=int)
    for i,x in enumerate(xs):
        for j,y in enumerate(ys):
            p = np.array([x,y])
            prediction_grid[j,i] = knn_predict(p, predictors, outcomes, k)
    
    return (xx, yy, prediction_grid)

def plot_prediction_grid (xx, yy, prediction_grid, filename):
    """ Plot KNN predictions for every point on the grid."""
    from matplotlib.colors import ListedColormap
    background_colormap = ListedColormap (["hotpink","lightskyblue", "yellowgreen"])
    observation_colormap = ListedColormap (["red","blue","green"])
    plt.figure(figsize =(10,10))
    plt.pcolormesh(xx, yy, prediction_grid, cmap = background_colormap, alpha = 0.5)
    plt.scatter(predictors[:,0], predictors [:,1], c = outcomes, cmap = observation_colormap, s = 50)
    plt.xlabel('Variable 1'); plt.ylabel('Variable 2')
    plt.xticks(()); plt.yticks(())
    plt.xlim (np.min(xx), np.max(xx))
    plt.ylim (np.min(yy), np.max(yy))
    plt.savefig(filename)
            
(predictors, outcomes) = generate_synth_data()

k=5; filename="knn5.pdf"; limits=(-3,4,-3,4); h=0.1
(xx,yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h,k)

plot_prediction_grid(xx,yy,prediction_grid, filename)

k=50; filename="knn50.pdf"; limits=(-3,4,-3,4); h=0.1
(xx,yy, prediction_grid) = make_prediction_grid(predictors, outcomes, limits, h,k)

plot_prediction_grid(xx,yy,prediction_grid, filename)

'''
points = np.array( [(x,y) for x in range(1,4) for y in range(1,4)] )
outcomes = np.array([0,0,0,0,1,1,1,1,1,1])

p = np.array([1, 1.0])

print(knn_predict(p, points, outcomes))

plt.plot(points[:,0], points[:,1],'ro');

plt.plot(p[0], p[1], 'go');



n = 20
points, outcomes = generate_synth_data(n)
plt.figure()
plt.plot(points[:n,0], points[:n,1],'ro')
plt.plot(points[n:,0], points[n:,1],'bo')
plt.show()
print(outcomes)
'''
