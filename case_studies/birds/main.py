# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

birddata= pd.read_csv('./bird_tracking.csv')
'''
bird_names=pd.unique(birddata.bird_name)
colors = dict(zip(bird_names, ['r','g','b'])) 
plt.figure(figsize=(7,7))
for bird in bird_names:
    ix = birddata.bird_name==bird
    x, y = birddata.longitude[ix], birddata.latitude[ix]
    plt.plot(x,y, colors[bird]+'.', label=bird)


plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(loc="lower right")
'''

'''
speed = birddata.speed_2d[birddata.bird_name=='Eric']
ix = np.isnan(speed)
plt.hist(speed[~ix], bins=np.linspace(0,30,20), normed=True)
plt.xlabel('speed (m/s)')
plt.ylabel('Frequency')
'''

birddata.speed_2d[birddata.bird_name=='Eric'].plot(kind='hist', range=[0,30])