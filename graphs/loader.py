import json
from pathlib import Path
from string import ascii_lowercase
class JsonGraph:
    def __init__(self, path, data=None) -> None:
        self.path = Path(path).absolute()
        self.data = data
    
    def save(self):
        with open(str(self.path), 'w') as file:
            json.dump(self.data, file)
    
    def load(self):
        with open(str(self.path), 'r') as file:
            self.data = json.load(file)


class TxtGraph:
    HORIZONTAL = '-'
    VERTICAL = '|'
    LEFT = '<'
    RIGHT = '>'
    UP = '^'
    DOWN = 'v'

    def __init__(self, path, edges='-|<>^v') -> None:
        self.path = Path(path).absolute()
        self.edges = edges
        self._setup_edges()
        self.data = {}

    def _setup_edges(self):
        (   
            self.HORIZONTAL, self.VERTICAL,
            self.LEFT, self.RIGHT,
            self.UP, self.DOWN
        ) = list(self.edges)
    
    def load(self):
        with open(str(self.path), 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        # print(ascii_lowercase)
        ROWS = len(lines)
        COLS = len(lines[0])
        for r, row in enumerate(lines):
            for c, char in enumerate(row):
                if char in ascii_lowercase:
                    self.data[char] = (r, c)
                    

    
if __name__ == '__main__':
    tg = TxtGraph('graphs/graph.txt')
    print(tg.UP)
    tg.load()

    jg = JsonGraph('graphs/graph.json')
    jg.load()
    print(jg.data)

    jg.data['a'] = []
    jg.save()
