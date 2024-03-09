import json
from pathlib import Path


class JsonGraph:
    def __init__(self, path, data=None) -> None:
        self.path = Path(path).absolute()
        self.data = data

    def save(self, indent=2):
        with open(str(self.path), 'w') as file:
            json.dump(self.data, file, indent=indent)

    def load(self):
        with open(str(self.path), 'r') as file:
            self.data = json.load(file)

