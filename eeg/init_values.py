import eeg.data_builder as dbuilder

file = open('../data/rat2.bin', 'rb')
offset = 0  # offset in frames
bytes_in_value = 2
number_of_channels = 4
sampling_frequency = 3400
frame_duration = 45  # in seconds
spec_max_frequency = 20  # in seconds

channels = dbuilder.build_channels(file, offset, bytes_in_value, number_of_channels, sampling_frequency, frame_duration)