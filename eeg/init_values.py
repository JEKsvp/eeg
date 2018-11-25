import eeg.data_builder as dbuilder

file = open('../data/rat22agonist12mg.wdq', 'rb')
offset = 1  # offset in frames
bytes_in_value = 2
number_of_channels = 4
sampling_frequency = 512
frame_duration = 20  # in seconds
spec_max_frequency = 25  # in seconds

channels = dbuilder.build_channels(file, offset, bytes_in_value, number_of_channels, sampling_frequency, frame_duration)