import eeg.constant_frequency_detector as cfd
import eeg.test_signal as ts

x, y = ts.get_test_signal()
sampling_frequency = 1000
result = cfd.find(y, sampling_frequency, cfd.FrequencySpan(7, 9))

print(result)