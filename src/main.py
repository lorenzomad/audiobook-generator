from text_extractor import TextExtractor
from audio_generator import AudioGenerator

AUDIOPATH = "../audio/sample.mp3"
EXAMPLE_PDF = "../sample_file/sample.pdf"
text_extractor = TextExtractor()

text = text_extractor.read_text(EXAMPLE_PDF)

audio_generator = AudioGenerator()

audio_generator.google_generate_audio(text, AUDIOPATH)
# audio_generator.play_audio(AUDIOPATH)
audio_generator.delete_file(AUDIOPATH)
