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

    def __init__(self, path, edges='-|<>^v', nodechars=ascii_uppercase) -> None:
        self.path = Path(path).absolute()
        self.nodechars = nodechars
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

    def _parse(self, lines, frontier=None):
        def normalize(lines):
            maxlen = max(map(len, lines))
            for line in lines:
                line += [' '] * (maxlen-len(line))
            return lines

        def process(lines, r, c, neighbours, visited, node_stack, coord_stack):
            neighbour = lines[r][c]
            neighbours.append(neighbour)
            if neighbour not in visited:
                node_stack.append(neighbour)
                coord_stack.append((r, c))

        lines = normalize(lines)

        ROWS = len(lines)
        r, c = 0, 0
        node_stack = [lines[r][c]]
        coord_stack = [(r,c)]
        visited = []

        while len(node_stack):
            current = node_stack.pop()
            r, c = coord_stack.pop()
            visited.append(current)
            if current in self.nodechars:
                neighbours = []
                self.data[current] = neighbours
                COLS = len(lines[r])

                left = lines[r][c-1] if c else None
                up = lines[r-1][c] if r else None
                right = lines[r][c+1] if c < COLS-1 else None
                down = lines[r+1][c] if r < ROWS-1 else None 

                if left in (self.HORIZONTAL, self.LEFT):
                    process(lines, r, c-2, neighbours, visited, node_stack, coord_stack)
                if up in (self.VERTICAL, self.UP):
                    process(lines, r-2, c, neighbours, visited, node_stack, coord_stack)
                if right in (self.HORIZONTAL, self.RIGHT):
                    process(lines, r, c+2, neighbours, visited, node_stack, coord_stack)
                if down in (self.VERTICAL, self.DOWN):
                    process(lines, r+2, c, neighbours, visited, node_stack, coord_stack)


    def load(self):
        with open(str(self.path), 'r') as file:
            lines = [list(line.strip()) for line in file.readlines()]
        self._parse(lines)
    
if __name__ == '__main__':
    tg = TxtGraph('graphs/graph.txt')
    # print(tg.UP)
    tg.load()
    for k, v in tg.data.items():
        print(k, ':', v)
    exit()
    jg = JsonGraph('graphs/graph.json')
    jg.load()
    print(jg.data)

    jg.data['a'] = []
    jg.save()
