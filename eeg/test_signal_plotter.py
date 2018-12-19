import eeg.test_signal as ts
import matplotlib.pyplot as plt
import eeg.plotter as custom_plt
import eeg.data_builder as dbuilder

figure, axes = plt.subplots(nrows=1, ncols=4)
figure.subplots_adjust(hspace=0.5, wspace=.3)

x, y = ts.get_test_signal()
sampling_frequency = 1000
frame_duration = 10
offset = 0

custom_plt.plot_signal(axes[0], y, sampling_frequency)

custom_plt.custom_specgram(axes[1], dbuilder.butter_highpass_filter(y, sampling_frequency, 2), sampling_frequency, frequency_limit=20)

vars0 = dbuilder.build_vars(y, int(sampling_frequency), frame_duration)
custom_plt.plot_var(axes[2], vars0, range(offset * frame_duration, offset * frame_duration + frame_duration))

t1, max_freqs_1 = dbuilder.max_frequencies_with_float_window(dbuilder.butter_highpass_filter(y, sampling_frequency, 2), sampling_frequency, 0.5, 0.2)
axes[3].plot(t1 + (frame_duration * offset), max_freqs_1)

axes[3].axes.grid()

axes[3].set_xlabel('t, s')
axes[3].set_ylabel('F, Hz')

plt.show()