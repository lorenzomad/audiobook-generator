from pypdf import PdfReader


class TextExtractor:
    def __init__(self):
        pass


    def read_text(self, pdf_file):
        #reads a file and outputs the text
        reader = PdfReader(pdf_file)
        text = [page.extract_text() for page in reader.pages]
        return "\n".join(text)