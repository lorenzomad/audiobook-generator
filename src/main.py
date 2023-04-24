from text_extractor import TextExtractor
from audio_generator import AudioGenerator

text_extractor = TextExtractor()

text = text_extractor.read_text("../sample_file/sample.pdf")

print(text)

audio_generator = AudioGenerator()

audio_path = "../audio/sample.mp3"
audio_generator.generate_audio(text)
audio_generator.save_audio(audio_path)
audio_generator.play_audio(audio_path)