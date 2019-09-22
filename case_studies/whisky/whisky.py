# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

whisky = pd.read_csv('./whiskies.txt', index_col='RowID')

# print(whisky.iloc[:10, :5])
print (whisky.columns)
flavors = whisky.iloc[:,2:-3]
print(flavors.columns)

corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)


plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.colorbar()