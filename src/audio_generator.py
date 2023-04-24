import gtts
from playsound import playsound
import os


class AudioGenerator:
    #class to generate audio file from text using Google tts
    def __init__(self):
        self.tts = None

    def generate_audio(self, text):
        #creates an audio from the input text
        self.tts = gtts.gTTS(text)
        

    def save_audio(self, save_path):
        #save the file to the path
        self.tts.save(save_path)

    def play_audio(self, play_path):
        #plays the audio file saved at play_path
        playsound(play_path)

    def delete_file(self, delete_path):
        #deletes the file save at delete_path
        os.remove(delete_path)