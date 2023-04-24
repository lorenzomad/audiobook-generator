import gtts
import os

from playsound import playsound
from bark import SAMPLE_RATE, generate_audio, preload_models
from IPython.display import Audio
from scipy.io.wavfile import write as write_wav

class AudioGenerator:
    #class to generate audio file from text using Google tts or bark
    def __init__(self):
        self.tts_type = None
        self.bark_audio = None
        self.google_audio = None

    def google_generate_audio(self, text, save_path):
        #creates an audio from the input text using google tts
        self.google_audio = gtts.gTTS(text)
        self.google_audio.save(save_path)
        self.tts_type = "google"

    def bark_generate_audio(self, text, save_path):
        #creates the audio from tetx using bark model
        preload_models()
        self.bark_audio = generate_audio(text)
        write_wav(save_path, SAMPLE_RATE, self.bark_audio)
        self.tts_type = "bark"

    def play_audio(self, play_path):
        #plays the audio file saved at play_path
        playsound(play_path)

    def delete_file(self, delete_path):
        #deletes the file save at delete_path
        os.remove(delete_path)