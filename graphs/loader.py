import json
from pathlib import Path
from string import ascii_uppercase


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

    # def _parse(self, lines):
    #     self.rows = len(lines)
    #     self.cols = len(lines[0])
    #     for r, row in enumerate(lines):
    #         for c, char in enumerate(row):
    #             if char in ascii_uppercase:
    #                 self.data[char] = {'coords': (r, c), 'neighbours':[]}
    #                 neighbours = self.data[char]['neighbours']
    #                 for y, x in self._get_valid_coords(r, c):
    #                     edge = lines[y][x]
    #                     if edge in self.edges:
    #                         match edge:
    #                             case self.LEFT:
    #                                 neighbours.append[lines[y][x-1]]
    #                             case self.RIGHT:
    #                                 pass
    #                             case self.UP:
    #                                 neighbours.append[lines[y-1][x]]
    #                             case self.DOWN:
    #                                 pass
    def _parse(self, lines, frontier=None):
        for line in lines:
            print(line)
        
        ROWS = len(lines)
        r, c = 0, 0
        stack = [lines[r][c]]
        while len(stack):
            current = stack.pop()
            print(f'{current=}')
            if current in ascii_uppercase:
                neighbours = []
                self.data[current] = neighbours
                COLS = len(lines[r])

                left = lines[r][c-1] if c else None
                up = lines[r-1][c] if r else None
                right = lines[r][c+1] if c < COLS-1 else None
                down = lines[r+1][c] if r < ROWS-1 else None 
                print(f'{left = }')
                print(f'{up = }')
                print(f'{right = }')
                print(f'{down = }')
                if left in (self.HORIZONTAL, self.LEFT):
                    neighbour = lines[r][c-2]
                    neighbours.append(neighbour)
                    stack.append(neighbour)
                if up in (self.VERTICAL, self.UP):
                    neighbour = lines[r-2][c]
                    neighbours.append(neighbour)
                    stack.append(neighbour)
                if right in (self.HORIZONTAL, self.RIGHT):
                    neighbour = lines[r][c+2]
                    neighbours.append(neighbour)
                    stack.append(neighbour)
                if down in (self.VERTICAL, self.DOWN):
                    neighbour = lines[r+2][c]
                    neighbours.append(neighbour)
                    stack.append(neighbour)
                # input()


    def load(self):
        with open(str(self.path), 'r') as file:
            lines = [list(line.strip()) for line in file.readlines()]
        self._parse(lines)
    
if __name__ == '__main__':
    tg = TxtGraph('graphs/graph.txt')
    # print(tg.UP)
    tg.load()
    exit()
    jg = JsonGraph('graphs/graph.json')
    jg.load()
    print(jg.data)

    jg.data['a'] = []
    jg.save()
