from pydub import AudioSegment
from pydub.utils import make_chunks
import os

def generate_audio_chunks(file, chunk_length_ms, tag, directory):
    myaudio = AudioSegment.from_mp3(file)
    chunks = make_chunks(myaudio, chunk_length_ms)
    for i, chunk in enumerate(chunks):
        chunk_name = tag + "-chunk{0}.wav".format(i)
        print "exporting", chunk_name
        chunk.export(os.path.join(directory, chunk_name), format="wav")