
import numpy as np
from scipy.io import wavfile
from scipy import interpolate

# Python class for reading wavfiles
class WavFileReader:

    def __init__(self, file, SAMPLE_RATE):
        self.SAMPLE_RATE = SAMPLE_RATE
        self.file = file
        rate, data = wavfile.read(file)
        self.rate = rate
        self.data = data
        self.convert_sample_rate()
        self.rate, self.data = wavfile.read(file)

    def get_audio(self):
        return self.data

    def get_rate(self):
        return self.rate

    def convert_sample_rate(self):
        if float(self.rate) != float(self.SAMPLE_RATE):
            print "Converting sample rate of audio to {0}".format(self.SAMPLE_RATE) + " for file {0}".format(self.file) + " from {0}".format(self.rate)
            duration = self.data.shape[0] / self.rate

            time_old = np.linspace(0, duration, self.data.shape[0])
            time_new = np.linspace(0, duration, int(self.data.shape[0] * self.SAMPLE_RATE / self.rate))

            interpolator = interpolate.interp1d(time_old, self.data.T)
            new_audio = interpolator(time_new).T

            wavfile.write(self.file, self.SAMPLE_RATE, np.round(new_audio).astype(self.data.dtype))