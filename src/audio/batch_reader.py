
from src.audio.wav_file_reader import WavFileReader
from src.audio.audio_chunker import generate_audio_chunks
from src.categories.category_audio_container import CategoryAudioContainer
import os


def collate_and_convert_audio_in_directory(directory, sample_rate, audio_ms, audio_channels):
    category_audio_container = CategoryAudioContainer(sample_rate * (audio_ms / 1000))
    for file in os.listdir(directory):
        if file.endswith(".mp3"):
            generate_audio_chunks(os.path.join(directory, file), audio_ms, file, directory, audio_channels)
    for file in os.listdir(directory):
        if file.endswith(".wav") and "chunk" in file:
            read_wav_file = WavFileReader(os.path.join(directory, file), sample_rate)
            category_audio_container.add_and_categorise_audio(read_wav_file.get_audio(), file)
    return category_audio_container
