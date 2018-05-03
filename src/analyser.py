import tensorflow as tf
from audio.wav_file_reader import WavFileReader
from categories.category_audio_container import CategoryAudioContainer
import os

def collate_audio_in_directory(directory):
    category_audio_container = CategoryAudioContainer()
    for file in os.listdir(directory):
        if file.endswith(".wav"):
            read_wav_file = WavFileReader(os.path.join(directory, file))
            if "sarcasm" in file:
                category_audio_container.add_sarcasm_audio(read_wav_file.get_audio())
            elif "happy" in file:
                category_audio_container.add_happy_audio(read_wav_file.get_audio())
            elif "angry" in file:
                category_audio_container.add_angry_audio(read_wav_file.get_audio())
            elif "sad" in file:
                category_audio_container.add_sad_audio(read_wav_file.get_audio())
    return category_audio_container

def analyse_audio(category_audio_container):
    print category_audio_container


def main():
    audio_container = collate_audio_in_directory('/home/andrew/Downloads/')
    analyse_audio(audio_container)


if __name__ == "__main__": main()