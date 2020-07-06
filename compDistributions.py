import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

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


def substract2Dist(dist1, dist2):

    # calculate difference
    diff_dist = dist1-dist2

    # calculate p value
    bootP = np.sum(diff_dist > 0) / len(diff_dist);
    print(bootP)
    if bootP < .5:
        bootTwoTailedP = bootP * 2;
    else:
        bootTwoTailedP = (1 - bootP) * 2;

    # plot
    plt.figure(figsize=(5, 5))

    sns.distplot(dist1, label='Bin1')
    sns.distplot(dist2, label='Bin2')
    sns.distplot(diff_dist, label='difference')
    sns.despine()
    plt.legend()
    plt.title('p = ' + str(bootTwoTailedP))
    plt.show()

def sigDistribution(dist, extra_title=' ', xlim=None, ylim=None):


    # calculate p value
    bootP = np.sum(dist > 0) / len(dist);
    print(bootP)
    if bootP < .5:
        bootTwoTailedP = bootP * 2;
    else:
        bootTwoTailedP = (1 - bootP) * 2;

    # plot
    plt.figure(figsize=(5, 5))

    plt.hist(dist, label='Distribution')
    sns.despine()

    if xlim is not None:
        plt.xlim(xlim)
    if ylim is not None:
        plt.ylim(ylim)

    plt.legend()
    plt.title('p = ' + str(bootTwoTailedP) + extra_title)
    plt.show()

