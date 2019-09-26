# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

birddata= pd.read_csv('./bird_tracking.csv')

bird_names=pd.unique(birddata.bird_name)
'''
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

# birddata.speed_2d[birddata.bird_name=='Eric'].plot(kind='hist', range=[0,30])

import datetime
'''
date_str = birddata.date_time[0]
date_str[:-3]
date = datetime.datetime.strptime(date_str[:-3], '%Y-%m-%d %H:%M:%S')
print(type(date))

conv_time = datetime.datetime.strptime

birddata['datetime'] = (birddata.date_time
                        .str.slice(0,-3)
                        .apply(conv_time, args=['%Y-%m-%d %H:%M:%S']))

'''
conv_time = datetime.datetime.strptime
timestamps = []
for k in range(len(birddata)):
    timestamps.append(conv_time(birddata.date_time.iloc[k][:-3], '%Y-%m-%d %H:%M:%S'))
    
birddata['timestamp'] = pd.Series(timestamps, index=birddata.index)



data = birddata[birddata['bird_name']=='Eric']
times = data.timestamp
elapsed_time = [time-times[0] for time in times]
elapsed_days = np.array(elapsed_time) / datetime.timedelta(days=1)

next_day = 1
inds = []
daily_mean_speed = []

for i, t in enumerate(elapsed_days):
    if t < next_day:
        inds.append(i)
    else:
        daily_mean_speed.append(np.mean(data.speed_2d[inds]))
        next_day += 1
        inds = []
        
'''        
plt.figure(figsize=(8,6))
plt.plot(daily_mean_speed)
plt.xlabel("Day")
plt.ylabel("Mean speed (m/s)")
plt.show()
'''
import cartopy.crs as ccrs
import cartopy.feature as cfeature

proj = ccrs.Mercator()

plt.figure(figsize=(10,10))
ax = plt.axes(projection=proj)
ax.set_extent((-25.0, 20.0, 52.0, 10.0))
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle=":")
for name in bird_names:
    ix = birddata.bird_name==name
    x,y = birddata.longitude[ix], birddata.latitude[ix]
    ax.plot(x,y,'.', transform=ccrs.Geodetic(), label=name)
    
plt.legend(loc="upper left")
plt.show()

        
        
        
        
        
        
        
        
        
        
        
        
        