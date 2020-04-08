import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from scipy import stats

def compNullNormal(normalXYCorr, normalXDist, normalYDist, xlabel, ylabel, title=''):

    nullCorr = nullCorrDistBoot(normalXDist, normalYDist)

    plt.bar([1, 2], [np.mean(nullCorr), normalXYCorr[0]], yerr=[np.var(nullCorr), 0])
    plt.xticks([1, 2], ['null dist', 'dist'])
    plt.xlabel(xlabel, fontsize=15)
    plt.ylabel(ylabel, fontsize=15)
    plt.title('title')

def nullCorrDistBoot(normalXDist, normalYDist, nIterations=10000):

    corr_list = []
    for i in range(nIterations):
        if isinstance(normalXDist, pd.core.series.Series):
            shuffled = normalXDist.sample(frac=1).reset_index(drop=True)  # shuffle the distribution
        else:
            shuffled = random.shuffle(normalXDist)

        r = stats.pearsonr(shuffled, normalYDist)
        corr_list.append(r[0])

    return corr_list
