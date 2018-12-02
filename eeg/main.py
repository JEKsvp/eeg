from eeg.init_values import *
import matplotlib.pyplot as plt
import eeg.data_builder as dbuilder
import eeg.plotter as custom_plt
import numpy as np

figure, axes = plt.subplots(nrows=4, ncols=4)
figure.subplots_adjust(hspace=0.5, wspace=.3)
custom_plt.plot_signal(axes[0, 0], channels[0], sampling_frequency)
custom_plt.plot_signal(axes[1, 0], channels[1], sampling_frequency)
custom_plt.plot_signal(axes[2, 0], channels[2], sampling_frequency)
custom_plt.plot_signal(axes[3, 0], channels[3], sampling_frequency)

custom_plt.custom_specgram(axes[0, 1], dbuilder.high_filter(channels[0], sampling_frequency, 2), sampling_frequency, frequency_limit=spec_max_frequency)
custom_plt.custom_specgram(axes[1, 1], dbuilder.high_filter(channels[1], sampling_frequency, 2), sampling_frequency, frequency_limit=spec_max_frequency)
custom_plt.custom_specgram(axes[2, 1], dbuilder.high_filter(channels[2], sampling_frequency, 2), sampling_frequency, frequency_limit=spec_max_frequency)
custom_plt.custom_specgram(axes[3, 1], dbuilder.high_filter(channels[3], sampling_frequency, 2), sampling_frequency, frequency_limit=spec_max_frequency)

vars0 = dbuilder.build_vars(channels[0], int(sampling_frequency), frame_duration)
vars1 = dbuilder.build_vars(channels[1], int(sampling_frequency), frame_duration)
vars2 = dbuilder.build_vars(channels[2], int(sampling_frequency), frame_duration)
vars3 = dbuilder.build_vars(channels[3], int(sampling_frequency), frame_duration)
custom_plt.plot_var(axes[0, 2], vars0, range(offset * frame_duration, offset * frame_duration + frame_duration))
custom_plt.plot_var(axes[1, 2], vars1, range(offset * frame_duration, offset * frame_duration + frame_duration))
custom_plt.plot_var(axes[2, 2], vars2, range(offset * frame_duration, offset * frame_duration + frame_duration))
custom_plt.plot_var(axes[3, 2], vars3, range(offset * frame_duration, offset * frame_duration + frame_duration))

t1, max_freqs_1 = dbuilder.max_frequencies_with_float_window(dbuilder.high_filter(channels[0], sampling_frequency, 2), sampling_frequency, 1, 0.5)
t2, max_freqs_2 = dbuilder.max_frequencies_with_float_window(dbuilder.high_filter(channels[1], sampling_frequency, 2), sampling_frequency, 1, 0.5)
t3, max_freqs_3 = dbuilder.max_frequencies_with_float_window(dbuilder.high_filter(channels[2], sampling_frequency, 2), sampling_frequency, 1, 0.5)
t4, max_freqs_4 = dbuilder.max_frequencies_with_float_window(dbuilder.high_filter(channels[3], sampling_frequency, 2), sampling_frequency, 1, 0.5)

axes[0, 3].plot(t1 + (frame_duration * offset), max_freqs_1)
axes[1, 3].plot(t2 + (frame_duration * offset), max_freqs_2)
axes[2, 3].plot(t3 + (frame_duration * offset), max_freqs_3)
axes[3, 3].plot(t4 + (frame_duration * offset), max_freqs_4)
axes[0, 3].axes.grid()
axes[1, 3].axes.grid()
axes[2, 3].axes.grid()
axes[3, 3].axes.grid()

axes[0, 3].set_xlabel('t, s')
axes[0, 3].set_ylabel('F, Hz')
axes[1, 3].set_xlabel('t, s')
axes[1, 3].set_ylabel('F, Hz')
axes[2, 3].set_xlabel('t, s')
axes[2, 3].set_ylabel('F, Hz')
axes[3, 3].set_xlabel('t, s')
axes[3, 3].set_ylabel('F, Hz')
plt.show()
