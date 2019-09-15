#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 20:21:36 2019

@author: pk
"""
import random
from collections import Counter

import numpy as np
import scipy



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

winner = majority_vote([1,1,2,3,3])
print(winner)