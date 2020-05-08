import numpy as np
import scipy

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

def alternative_mean_confidence_interval(data):

    sample_mean = np.mean(data)
    sample_95ci = 1.96 * scipy.stats.sem(data)
    # sample_min = sample_mean = sample_95ci
    # sample_max = sample_mean + sample_95ci

    return sample_mean, sample_95ci
