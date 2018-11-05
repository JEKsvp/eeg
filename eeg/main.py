from eeg.init_values import *
import matplotlib.pyplot as plt
import eeg.data_builder as dbuilder
import eeg.plotter as custom_plt
import numpy as np

figure, axes = plt.subplots(nrows=4, ncols=3)
figure.subplots_adjust(hspace=1.0, wspace=.6)
custom_plt.plot_signal(axes[0, 0], channels[0], range_between_points)
custom_plt.plot_signal(axes[1, 0], channels[1], range_between_points)
custom_plt.plot_signal(axes[2, 0], channels[2], range_between_points)
custom_plt.plot_signal(axes[3, 0], channels[3], range_between_points)

custom_plt.custom_specgram(axes[0, 1], channels[0], sampling_frequency, spec_max_frequency)
custom_plt.custom_specgram(axes[1, 1], channels[1], sampling_frequency, spec_max_frequency)
custom_plt.custom_specgram(axes[2, 1], channels[2], sampling_frequency, spec_max_frequency)
custom_plt.custom_specgram(axes[3, 1], channels[3], sampling_frequency, spec_max_frequency)

vars0 = dbuilder.build_vars(channels[0], int(sampling_frequency))
vars1 = dbuilder.build_vars(channels[1], int(sampling_frequency))
vars2 = dbuilder.build_vars(channels[2], int(sampling_frequency))
vars3 = dbuilder.build_vars(channels[3], int(sampling_frequency))
custom_plt.plot_var(axes[0, 2], vars0)
custom_plt.plot_var(axes[1, 2], vars1)
custom_plt.plot_var(axes[2, 2], vars2)
custom_plt.plot_var(axes[3, 2], vars3)
plt.show()
