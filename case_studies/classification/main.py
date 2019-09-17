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

'''
points = np.array( [(x,y) for x in range(1,4) for y in range(1,4)] )
outcomes = np.array([0,0,0,0,1,1,1,1,1,1])

p = np.array([1, 1.0])

print(knn_predict(p, points, outcomes))

plt.plot(points[:,0], points[:,1],'ro');

plt.plot(p[0], p[1], 'go');
'''


n = 20
points, outcomes = generate_synth_data(n)
plt.figure()
plt.plot(points[:n,0], points[:n,1],'ro')
plt.plot(points[n:,0], points[n:,1],'bo')
plt.show()
print(outcomes)
