import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
from eeg.init_values import *


def plot_signal(axes, points, sampling_frequency):
    range_between_points = 1 / sampling_frequency
    t = []
    current = 0
    data = np.asarray(points)
    data_length = len(data)
    for i in range(data_length):
        t.append(current)
        current += range_between_points
    axes.plot(np.array(t) + (frame_duration * offset), points)
    axes.set_xlabel('t, s')
    axes.set_ylabel('U, V')


def plot_var(axes, points, t):
    axes.plot(t, points)
    axes.set_xlabel('t, s')
    axes.set_ylabel('D[X]')


def custom_specgram(axes, points, sampling_frequency, frequency_limit=50):
    cmap = plt.cm.gray_r
    my_cmap = cmap(np.arange(cmap.N))
    my_cmap[:, -1] = np.linspace(1, 1, cmap.N)
    my_cmap = ListedColormap(my_cmap)
    data = np.asarray(points)
    axes.specgram(data, sampling_frequency, sampling_frequency, noverlap=0, cmap=my_cmap)
    axes.set_ylim([0, frequency_limit])
    axes.set_xlabel('t, s')
    axes.set_ylabel('F, Hz')

    seconds = len(points) / sampling_frequency
    x_ticks = np.arange(0, seconds, seconds / 5)
    axes.set_xticks(x_ticks)
    y_ticks = np.arange(0, frequency_limit, int(frequency_limit / 5))
    axes.set_yticks(y_ticks)
    axes.tick_params(labelsize=6)


def plot_fft(axes, x, y):
    axes.plot(x, y)


def custom_style(axes, data, sampling_frequency):
    data_length = len(data)
    axes.grid()
    range_between_points = 1 / sampling_frequency
    x_length = data_length * range_between_points
    x_ticks = np.arange(0, x_length, x_length / 5)
    axes.set_xticks(x_ticks)
    min_y = data.min()
    max_y = data.max()
    y_ticks = np.arange(min_y, max_y, (max_y - min_y) / 5)
    axes.set_yticks(y_ticks)
    axes.tick_params(labelsize=8)
