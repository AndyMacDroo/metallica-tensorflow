
# Class storing audio as a numpy array against different categories
class CategoryAudioContainer:

    def __init__(self):
        self.audio = []
        self.one_hot_encoding_category = []

    def add_audio(self, audio_array, file_label):
        if 'positive' in file_label:
            self.one_hot_encoding_category.append([0,1])
            self.audio.append(audio_array)
        elif 'negative' in file_label:
            self.one_hot_encoding_category.append([1,0])
            self.audio.append(audio_array)

    def get_audio_and_encoded_category(self):
        return self.audio, self.one_hot_encoding_category
