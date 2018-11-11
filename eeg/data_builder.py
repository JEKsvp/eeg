import os
import struct
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def build_channels(file, offset, bytes_in_value, number_of_channels, sampling_frequency, frame_duration):
    points_in_interval = int(sampling_frequency * frame_duration * number_of_channels)
    points_in_interval = points_in_interval if points_in_interval % 2 == 0 else points_in_interval - 1
    result = []
    file.seek(int(offset * points_in_interval * bytes_in_value))
    for point_value in range(int(points_in_interval)):
        buffer = file.read(bytes_in_value)
        A = struct.unpack('h', buffer)
        result.append(A[0])
    file.close()
    i = 0
    result_dict = {}
    for i in range(number_of_channels):
        result_dict[i] = []
    for val in result:
        result_dict[i].append(val / 1000)
        i += 1
        if i == 4:
            i = 0
    return result_dict


def build_vars(points, group_size):
    result_size = int(len(points) / group_size)
    result = []
    current_start_cut = 0
    for i in range(result_size):
        var = np.var(points[current_start_cut: current_start_cut + group_size])
        result.append(var)
        current_start_cut += group_size
    return result


def build_max_frequencies(points, sampling_frequency):
    f, t, Sxx = signal.spectrogram(np.array(points), fs=sampling_frequency)
    result = []
    width = len(Sxx[0])
    for i in range(width):
        freqs = column(Sxx, i)
        maxFreq = np.max(freqs)
        result.append(maxFreq)
    return [t, np.array(result)]


def column(matrix, i):
    return [row[i] for row in matrix]
