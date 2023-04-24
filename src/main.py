from text_extractor import TextExtractor
from audio_generator import AudioGenerator

AUDIOPATH = "../audio/sample.mp3"

text_extractor = TextExtractor()

text = text_extractor.read_text("../sample_file/sample.pdf")

print(text)

audio_generator = AudioGenerator()

audio_generator.generate_audio(text)
audio_generator.save_audio(AUDIOPATH)
# audio_generator.delete_file(AUDIOPATH)
