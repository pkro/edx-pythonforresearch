# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from sklearn.cluster.bicluster import SpectralCoclustering

whisky = pd.read_csv('./whiskies.txt')
flavors = whisky.iloc[:,2:-3]
corr_whisky = pd.DataFrame.corr(flavors.transpose())


model = SpectralCoclustering(n_clusters=6, random_state=0)
model.fit(corr_whisky)

whisky['Group'] = pd.Series(model.row_labels_, index=whisky.index)

whisky = whisky.iloc[np.argsort(model.row_labels_)]

correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations = np.array(correlations)

print(correlations)

plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")
plt.colorbar()

