import matplotlib.pyplot as plt
import numpy as np


def plot_signal(axes, points, range_between_points):
    point_times = []
    current = 0
    data = np.asarray(points)
    data_length = len(data)
    for i in range(data_length):
        point_times.append(current)
        current += range_between_points
    axes.plot(point_times, points)
    axes.set_xlabel('t, s')
    axes.set_ylabel('?, ?')
    custom_style(axes, data, range_between_points)


def plot_var(axes, points):
    axes.plot(points)
    axes.set_xlabel('t, s')
    axes.set_ylabel('D[X]')
    data = np.asarray(points)
    custom_style(axes, data, 1)


def custom_specgram(axes, points, sampling_frequency, frequency_limit=50):
    data = np.asarray(points)
    axes.specgram(data, 256, sampling_frequency, noverlap=100, cmap='jet')
    axes.set_ylim([0, frequency_limit])
    axes.set_xlabel('t, s')
    axes.set_ylabel('F, Hz')

    seconds = len(points) / sampling_frequency
    x_ticks = np.arange(0, int(seconds), int(seconds / 5))
    axes.set_xticks(x_ticks)
    y_ticks = np.arange(0, frequency_limit, int(frequency_limit / 5))
    axes.set_yticks(y_ticks)
    axes.tick_params(labelsize=6)


def custom_style(axes, data, range_between_points):
    data_length = len(data)
    axes.grid()
    x_length = int(data_length * range_between_points)
    x_ticks = np.arange(0, x_length, int(x_length / 5))
    axes.set_xticks(x_ticks)
    min_y = data.min()
    max_y = data.max()
    y_ticks = np.arange(min_y, max_y, int((max_y - min_y) / 5))
    axes.set_yticks(y_ticks)
    axes.tick_params(labelsize=6)
