import eeg.data_builder as dbuilder

file = open('../data/rat2.bin', 'rb')
offset = 1  # offset in frames
bytes_in_value = 2
number_of_channels = 4
sampling_frequency = 3400
frame_duration = 35  # in seconds
spec_max_frequency = 10  # in seconds
range_between_points = 1 / sampling_frequency

channels = dbuilder.build_channels(file, offset, bytes_in_value, number_of_channels, sampling_frequency, frame_duration)