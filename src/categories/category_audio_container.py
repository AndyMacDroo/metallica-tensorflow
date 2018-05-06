
# Class storing audio as a numpy array against different categories
class CategoryAudioContainer:

    def __init__(self, AUDIO_LENGTH):
        self.audio = []
        self.AUDIO_LENGTH = AUDIO_LENGTH
        self.one_hot_encoding_category = []

    def add_and_categorise_audio(self, audio_array, file_label):
        print "Audio array length is {0}".format(len(audio_array)) + " for file {0}".format(file_label)
        if len(audio_array) == self.AUDIO_LENGTH:
            if 'Metallica' in file_label:
                self.one_hot_encoding_category.append([0,1])
                self.audio.append(audio_array)
            elif 'R.E.M' in file_label:
                self.one_hot_encoding_category.append([1,0])
                self.audio.append(audio_array)

    def get_audio_and_encoded_category(self):
        return self.audio, self.one_hot_encoding_category
