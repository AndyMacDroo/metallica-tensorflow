
label_categories = ["R.E.M", "Metallica"]


def one_hot_encoding_category_array(category_array, category_label):
    one_hot_category = []
    for category in category_array:
        if category in category_label:
            one_hot_category.append(1)
        else:
            one_hot_category.append(0)
    return one_hot_category


# Class storing audio as a numpy array against different categories
class CategoryAudioContainer:
    def __init__(self, global_audio_length):
        self.audio = []
        self.audio_length = global_audio_length
        self.one_hot_encoding_category = []

    def add_and_categorise_audio(self, audio_array, file_label):
        print "Audio array length is {0}".format(len(audio_array)) + " for file {0}".format(file_label)
        if len(audio_array) == self.audio_length:
            for category_label in label_categories:
                if category_label in file_label:
                    one_hot_array = one_hot_encoding_category_array(label_categories, category_label)
                    if 1 in one_hot_array:
                        self.one_hot_encoding_category.append(one_hot_array)
                        self.audio.append(audio_array)

    def get_audio_and_encoded_category(self):
        return self.audio, self.one_hot_encoding_category
