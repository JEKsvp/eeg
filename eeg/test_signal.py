import numpy as np


def get_test_signal():
    mu, sigma = 0, 1
    s = np.random.normal(mu, sigma, 10000)
    x = np.linspace(-10*np.pi, 10*np.pi, 2000)

    result = np.append(s[:2000], s[2000:4000] + np.sin(x))
    result = np.append(result, s[4000:6000])
    result = np.append(result, s[6000:8000] + np.sin(x))
    result = np.append(result, s[8000:10000])
    return [np.linspace(0, 5, 10000), result]