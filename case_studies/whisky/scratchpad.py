#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 08:22:37 2019

@author: pk
"""

import pandas as pd
import numpy as np
import string

# from sklearn import

age = pd.Series({str(a): np.random.choice(range(1,99)) for a in range(1,5)})
# print(age)

data = {'name': ['peter','paul','mary'],
        'age': [np.random.choice(range(1,99)) for x in range(3)],
        'ZIP': [np.random.choice(range(1000,9999)) for x in range(3)]}

d = pd.DataFrame(data)
print(age)
agerev = age.reindex(reversed(age.index))
print(agerev)

x = pd.Series([1,2,3,4,5], index=list(string.ascii_lowercase[:5]))
y = pd.Series(range(6,11), index=list(string.ascii_lowercase[:5]))

print(x-y)
