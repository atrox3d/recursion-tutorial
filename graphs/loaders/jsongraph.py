import json
from pathlib import Path


class JsonGraph:
    def __init__(self, path: str, data: dict=None) -> None:
        self.path = Path(path).absolute()
        self.data = data

    def save(self, indent=2) -> None:
        with open(str(self.path), 'w') as file:
            json.dump(self.data, file, indent=indent)

    def print(self, data=None, indent=None):
        data = data if data is None else self.data
        print(json.dumps(data, indent=indent))

    def load(self) -> dict:
        with open(str(self.path), 'r') as file:
            self.data = json.load(file)
        return self.data
