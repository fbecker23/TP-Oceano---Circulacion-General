
"""
funciones_estadisticas.py

Funciones utilitarias para el TP:
- cross_correlation: calcula correlación cruzada normalizada y lags
- effective_sample_size: estima N_eff considerando autocorrelación lag-1 (Py)
"""
import numpy as np

def cross_correlation(x, y, maxlag=None):
    x = (x - np.nanmean(x)) / np.nanstd(x)
    y = (y - np.nanmean(y)) / np.nanstd(y)
    if maxlag is None:
        maxlag = len(x) - 1
    corr = np.correlate(y, x, mode='full') / len(x)
    lags = np.arange(-len(x)+1, len(x))
    # take centered part
    center = len(corr) // 2
    start = center - maxlag
    end = center + maxlag + 1
    return lags[start:end], corr[start:end]

def effective_sample_size(x):
    """
    Approximate effective sample size using lag-1 autocorrelation (Py).
    N_eff = N * (1 - rho1) / (1 + rho1)
    """
    x = np.asarray(x)
    x = x[~np.isnan(x)]
    N = len(x)
    if N < 3:
        return N
    rho1 = np.corrcoef(x[:-1], x[1:])[0,1]
    N_eff = N * (1 - rho1) / (1 + rho1)
    return max(1, N_eff)
