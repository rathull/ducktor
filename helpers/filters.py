import pandas as pd
import time
from openai import OpenAI
import os
import csv
import wave
import struct

def wav2text(filename):
    audio_file = open(f'helpers/resources/{filename}', 'rb')
    
    # Open client connection and transcribe
    client = OpenAI()
    transcript = client.audio.transcriptions.create(
        model="whisper-1", 
        file=audio_file,
        response_format='text'
    )
    
    return transcript

def create_wav(csv_filename, wav_filename, sample_rate=100, num_channels=1, sample_width=2):

    # Read PCM data from CSV file
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        pcm_data = [int(row[0]) for row in reader]

    # Create a WAV file
    with wave.open(wav_filename, 'w') as wav_file:
        wav_file.setparams((num_channels, sample_width, sample_rate, len(pcm_data), 'NONE', 'not compressed'))
        
        for sample in pcm_data:
            wav_file.writeframes(struct.pack('<h', sample))

    
create_wav('helpers/resources/sound_ow.csv', 'helpers/resources/sound_ow.wav')
print(wav2text(filename = 'sound_ow.wav'))