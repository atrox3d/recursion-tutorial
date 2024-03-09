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
        self.rows = 0
        self.cols = 0

    def _setup_edges(self):
        (   
            self.HORIZONTAL, self.VERTICAL,
            self.LEFT, self.RIGHT,
            self.UP, self.DOWN
        ) = list(self.edges)
    
    def _get_valid_coords(self, r, c):
        coords = [  (r, c) for r, c in 
                    [(r+y, c+x) for y in range(-1, 2) for x in range(-1, 2) if abs(y)!=abs(x)]
                    if 0 <= r <= self.rows and 0 <= c <= self.cols
                ]
        return coords

    def _parse(self, lines):
        self.rows = len(lines)
        self.cols = len(lines[0])
        for r, row in enumerate(lines):
            for c, char in enumerate(row):
                if char in ascii_lowercase:
                    self.data[char] = {'coords': (r, c), 'neighbours':[]}
                    neighbours = self.data[char]['neighbours']
                    for y, x in self._get_valid_coords(r, c):
                        edge = lines[y][x]
                        if edge in self.edges:
                            match edge:
                                case self.LEFT:
                                    neighbours.append[lines[y][x-1]]
                                case self.RIGHT:
                                    pass
                                case self.UP:
                                    neighbours.append[lines[y-1][x]]
                                case self.DOWN:
                                    pass

    def load(self):
        with open(str(self.path), 'r') as file:
            lines = [line.strip() for line in file.readlines()]
        self._parse(lines)
    
if __name__ == '__main__':
    tg = TxtGraph('graphs/graph.txt')
    print(tg.UP)
    tg.load()

    jg = JsonGraph('graphs/graph.json')
    jg.load()
    print(jg.data)

    jg.data['a'] = []
    jg.save()
