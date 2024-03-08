import json
from pathlib import Path

class JsonGraph:
    def __init__(self, path, data=None) -> None:
        self.path = Path(path).absolute()
        self.data = data
    
    def save(self):
        with open(str(self.path), 'w') as jfile:
            json.dump(self.data, jfile)
    
    def load(self):
        with open(str(self.path), 'r') as jfile:
            self.data = json.load(jfile)


if __name__ == '__main__':
    jg = JsonGraph('graphs/graph.json')
    jg.load()
    print(jg.data)

    jg.data['a'] = []
    jg.save()
