"""Module for loading plaintext data"""

class DataLoader:
    def __init__(self, path):
        self.path = path
        with open(path) as f:
            self.text = f.read()        

    def get_text(self):
        return self.text

    def get_lines(self):
        lines = self.text.split("\n")
        return lines