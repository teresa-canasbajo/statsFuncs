import numpy as np
import scipy

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

def mean_confidence_interval_plusminus(data):

    sample_mean = np.mean(data)
    sample_95ci = 1.96 * scipy.stats.sem(data)
    # sample_min = sample_mean - sample_95ci
    # sample_max = sample_mean + sample_95ci

    return sample_mean, sample_95ci

def confidence_interval_percentile(data, top=97, bottom=2.5):

    mean = np.mean(data)
    sorted_data = sorted(data)

    position_top = int((top/100) * len(data))
    position_bottom = int((bottom/100) * len(data))

    ci_low = sorted_data[position_bottom]
    ci_up = sorted_data[position_top]

    return mean, ci_low, ci_up

def mean_sem(data):

    mean, se = np.mean(data), scipy.stats.sem(data)
    high = mean + se
    low = mean - se

    return mean, high, low




