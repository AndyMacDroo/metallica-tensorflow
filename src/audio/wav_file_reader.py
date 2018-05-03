from scipy.io import wavfile

# Python class for reading wavfiles
class WavFileReader:

    def __init__(self, file):
        rate, data = wavfile.read(file)
        self.rate  = rate
        self.data = data

    def get_audio(self):
        return self.data

    def get_rate(self):
        return self.rate