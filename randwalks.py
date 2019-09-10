# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from matplotlib import pyplot as plt

steps = 10000
delta_x = np.random.normal(0,1,(2,steps))

'''
delta_x = np.array([[ 0.70231111,  2.51238433,  0.07851146,  1.23513001, -0.53920435],
                    [ 0.36144448, -1.15862057,  1.39301675, -0.81534148,  0.37274394]])
'''

delta_x = np.concatenate(([[0],[0]], delta_x), axis=1)
X = np.cumsum(delta_x, axis=1)


plt.plot(X[0], X[1], "ro-")
'''
for i_x, i_y in zip(X[0], X[1]):
    plt.text(i_x, i_y, '({0:.2f}, {1:.2f})'.format(i_x, i_y))
 '''
plt.show()