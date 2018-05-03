
# Class storing audio as a numpy array against different categories
class CategoryAudioContainer:

    def __init__(self):
        self.sarcasm_audio = []
        self.happy_audio = []
        self.sad_audio = []
        self.angry_audio = []

    def add_sarcasm_audio(self, audio_array):
        self.sarcasm_audio.append(audio_array)

    def add_happy_audio(self, audio_array):
        self.happy_audio.append(audio_array)

    def add_sad_audio(self, audio_array):
        self.sad_audio.append(audio_array)

    def add_angry_audio(self, audio_array):
        self.angry_audio.append(audio_array)

    def get_sarcasm_audio(self):
        return self.sarcasm_audio

    def get_happy_audio(self):
        return self.happy_audio

    def get_sad_audio(self):
        return self.sad_audio

    def get_angry_audio(self):
        return self.angry_audio
