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


def build_vars(points, sampling_frequency, frame_duration):
    result = []
    current_start_cut = 0
    for i in range(frame_duration):
        var = np.var(points[current_start_cut: current_start_cut + sampling_frequency])
        result.append(var)
        current_start_cut += sampling_frequency
    return result


def build_max_frequencies(points, sampling_frequency):
    f, t, Sxx = signal.spectrogram(np.array(points), fs=sampling_frequency, nperseg=int(sampling_frequency))
    result = []
    width = len(Sxx[0])
    for i in range(width):
        freqs = column(Sxx, i)
        maxFreq = np.argmax(freqs)
        result.append(maxFreq)
    return [t, np.array(result)]


def column(matrix, i):
    return [row[i] for row in matrix]


def custom_fft(points, sampling_frequency):
    n = len(points)
    freqs = np.fft.fftfreq(n, d=1. / sampling_frequency)
    mask = freqs > 0
    fft_vals = np.fft.fft(points)
    fft_theo = np.abs(fft_vals / n)
    return [freqs[mask], fft_theo[mask]]


def max_frequencies_with_float_window(points, sampling_frequency, window_size, step):
    seconds = int((len(points) / sampling_frequency))
    offset = 0
    result = {"t": [], "max_freq": []}
    while offset + window_size < seconds:
        result["t"].append(offset)
        freqs, vals = custom_fft(points[int(offset * sampling_frequency): int(
            offset * sampling_frequency + sampling_frequency * window_size)], sampling_frequency)
        max_freq = freqs[vals.argmax()]
        result["max_freq"].append(max_freq)
        offset += step
    return np.array(result["t"]), np.array(result["max_freq"])


def high_filter(points, sampling_frequency, freq):
    n = len(points)
    freqs = np.fft.fftfreq(n, d=1. / sampling_frequency)
    mask = freqs > freq
    fft_vals = np.fft.fft(points)
    s = np.fft.ifft(fft_vals[mask])
    return s
