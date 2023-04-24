from text_extractor import TextExtractor


text_extractor = TextExtractor()

text = text_extractor.read_text("../sample_file/sample.pdf")

print(text)