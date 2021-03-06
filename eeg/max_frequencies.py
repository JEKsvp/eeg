from eeg.init_values import *
import matplotlib.pyplot as plt
import eeg.data_builder as dbuilder
import eeg.plotter as custom_plt
import numpy as np

t1, max_freqs_1 = dbuilder.build_max_frequencies(channels[0], sampling_frequency)
t2, max_freqs_2 = dbuilder.build_max_frequencies(channels[1], sampling_frequency)
t3, max_freqs_3 = dbuilder.build_max_frequencies(channels[2], sampling_frequency)
t4, max_freqs_4 = dbuilder.build_max_frequencies(channels[3], sampling_frequency)

figure, axes = plt.subplots(nrows=4, ncols=1)
figure.subplots_adjust(hspace=1.0, wspace=.6)

axes[0].plot(t1, max_freqs_1)
axes[1].plot(t2, max_freqs_2)
axes[2].plot(t3, max_freqs_3)
axes[3].plot(t4, max_freqs_4)

axes[0].set_xlabel('t, s')
axes[0].set_ylabel('F, Hz')
axes[1].set_xlabel('t, s')
axes[1].set_ylabel('F, Hz')
axes[2].set_xlabel('t, s')
axes[2].set_ylabel('F, Hz')
axes[3].set_xlabel('t, s')
axes[3].set_ylabel('F, Hz')

custom_plt.custom_style(axes[0], max_freqs_1, 1 / (frame_duration / len(t1)))
custom_plt.custom_style(axes[1], max_freqs_2, 1 / (frame_duration / len(t2)))
custom_plt.custom_style(axes[2], max_freqs_3, 1 / (frame_duration / len(t3)))
custom_plt.custom_style(axes[3], max_freqs_4, 1 / (frame_duration / len(t4)))
plt.show()