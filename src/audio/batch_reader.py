
from src.audio.wav_file_reader import WavFileReader
from src.audio.audio_chunker import generate_audio_chunks
from src.categories.category_audio_container import CategoryAudioContainer
import os


def collate_and_convert_audio_in_directory(directory, SAMPLE_RATE, AUDIO_MILLISECONDS):
    category_audio_container = CategoryAudioContainer(SAMPLE_RATE * (AUDIO_MILLISECONDS / 1000))
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            generate_audio_chunks(os.path.join(directory, file), AUDIO_MILLISECONDS, file, directory)
    for file in os.listdir(directory):
        if file.endswith(".wav") and "chunk" in file:
            read_wav_file = WavFileReader(os.path.join(directory, file), SAMPLE_RATE)
            category_audio_container.add_and_categorise_audio(read_wav_file.get_audio(), file)
    return category_audio_container
