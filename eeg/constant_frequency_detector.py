import numpy as np
import eeg.data_builder as dbuilder


# минимальнаяи максимальная чатстоты, в которых рассматриваются отрезки с постоянной частотой
class FrequencySpan:
    def __init__(self, min_freq, max_freq):
        self.min_freq = min_freq
        self.max_freq = max_freq


def find(points, sampling_frequency, frequency_span, min_const_freq_duration=0.5, window_size=0.5, step=0.02):
    def append_line(dict, current_freq, time_duration):
        if dict.get(current_freq) is not None:
            dict[current_freq].append(time_duration)
        else:
            dict[current_freq] = [time_duration]

    def clear_not_span_freqs(res_dict):
        keys_for_remove = []
        for key in res_dict.keys():
            if frequency_span.min_freq < key < frequency_span.max_freq:
                continue
            else:
                keys_for_remove.append(key)

        for key in keys_for_remove:
            res_dict.pop(key)

    def clear_empty_values(res_dict):
        keys_for_remove = []
        for key in res_dict.keys():
            if len(res_dict[key]) == 0:
                keys_for_remove.append(key)

        for key in keys_for_remove:
            res_dict.pop(key)

    def filter_result(res):
        clear_not_span_freqs(res)
        for key in res.keys():
            i = 0
            while i < len(res[key]):
                if res[key][i][1] - res[key][i][0] < min_const_freq_duration:
                    res[key].remove(res[key][i])
                else:
                    i += 1
        clear_empty_values(res)

    filtered_signa = dbuilder.butter_highpass_filter(points, sampling_frequency, 2)
    t, max_freqs = dbuilder.max_frequencies_with_float_window(filtered_signa, sampling_frequency, window_size, step)
    time_between_points = t[len(t) - 1] / len(max_freqs)  # временое расстояние между точеками в секундах
    result = {}
    i = 1
    while i < len(max_freqs):
        current_freq = max_freqs[i - 1]
        current_time_duration = [(i - 1) * time_between_points, 0]
        for j in range(i, len(max_freqs)):
            if max_freqs[i - 1] == max_freqs[i]:
                i += 1
            else:
                current_time_duration[1] = (i - 1) * time_between_points
                append_line(result, current_freq, current_time_duration)
                i += 1
                break

    filter_result(result)
    return result
