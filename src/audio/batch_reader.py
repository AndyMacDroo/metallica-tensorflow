
from src.audio.wav_file_reader import WavFileReader
from src.categories.category_audio_container import CategoryAudioContainer
import os

def collate_audio_in_directory(directory):
    category_audio_container = CategoryAudioContainer()
    for file in os.listdir(directory):
        if file.endswith(".wav"):
            read_wav_file = WavFileReader(os.path.join(directory, file))
            category_audio_container.add_audio(read_wav_file.get_audio(), file)
    return category_audio_container