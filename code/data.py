"""Module for loading plaintext data"""

class DataLoader:
    def __init__(self, path):
        self.path = path
        with open(path) as f:
            self.text = f.read()  

    """removes execution metatdata from plaintext"""
    def clean_agiga_text(self):
        self.text = " ".join(self.get_lines()[13:-7])

    def get_text(self):
        return self.text

    def get_lines(self):
        lines = self.text.split("\n")
        return lines

def build_loader():
    loader = DataLoader("data/agiga/export.txt")
    loader.clean_agiga_text()
    return loader