import os
import struct
import numpy as np


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
        result_dict[i].append(val)
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
    points_in_second = int(sampling_frequency)
    seconds = int(len(points) / sampling_frequency)
    result = []
    offset = 0
    for i in range(seconds):
        fft_vals = np.fft.fft(points[offset:offset + points_in_second])
        offset += points_in_second
        fft_theo = 2.0 * np.abs(fft_vals.real / points_in_second)
        max_freq = np.argmax(fft_theo[0:  50])
        result.append(max_freq)
    return np.array(result)
