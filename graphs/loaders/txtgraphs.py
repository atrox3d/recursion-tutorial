from pathlib import Path
from string import ascii_uppercase


class TxtGraph:
    HORIZONTAL = '-'
    VERTICAL = '|'
    LEFT = '<'
    RIGHT = '>'
    UP = '^'
    DOWN = 'v'

    edges = HORIZONTAL + VERTICAL + LEFT + RIGHT + UP + DOWN

    def __init__(self, path: str, edges: str='-|<>^v', nodechars: str=ascii_uppercase) -> None:
        self.path = Path(path).absolute()
        self.nodechars = nodechars
        if self.edges != edges:
            self._setup_edges()
        self.data = {}

    def _setup_edges(self) -> None:
        ''' convert string to class contants of graph edges '''
        (
            self.HORIZONTAL, self.VERTICAL,
            self.LEFT, self.RIGHT,
            self.UP, self.DOWN
        ) = list(self.edges)

    def _parse(self, lines: list[list[str]]) -> None:
        ''' parse matrix of chars to graph dict '''

        def normalize_matrix(lines):
            ''' add spaces to each line to make lines even '''
            maxlen = max(map(len, lines))
            for line in lines:
                line += [' '] * (maxlen-len(line))
            return lines

        def process_node(lines: list[list[str]], r: int, c: int, 
                         neighbours: list, visited: list, 
                         node_stack: list, coord_stack: list) -> None:
            ''' updates neighbours of node and control stacks '''
            neighbour = lines[r][c]
            neighbours.append(neighbour)
            if neighbour not in visited:
                node_stack.append(neighbour)
                coord_stack.append((r, c))
        
        def sort_graph(data: dict) -> dict:
            return {k:sorted(v) for k, v in sorted(data.items())}

        lines = normalize_matrix(lines)

        ROWS = len(lines)
        COLS = len(lines[0])
        r, c = 0, 0

        node_stack = [lines[r][c]]  # push first node
        coord_stack = [(r,c)]       # push first node coords
        visited = []

        while len(node_stack):
            current = node_stack.pop()
            r, c = coord_stack.pop()
            visited.append(current)

            # process only nodes, not edges
            if current in self.nodechars:
                # default node structure
                neighbours = []
                self.data[current] = neighbours
                
                # check 4 directions
                left = lines[r][c-1] if c else None
                up = lines[r-1][c] if r else None
                right = lines[r][c+1] if c < COLS-1 else None
                down = lines[r+1][c] if r < ROWS-1 else None

                # process neighbours if edges found
                if left in (self.HORIZONTAL, self.LEFT):
                    process_node(lines, r, c-2, neighbours, visited, node_stack, coord_stack)
                if up in (self.VERTICAL, self.UP):
                    process_node(lines, r-2, c, neighbours, visited, node_stack, coord_stack)
                if right in (self.HORIZONTAL, self.RIGHT):
                    process_node(lines, r, c+2, neighbours, visited, node_stack, coord_stack)
                if down in (self.VERTICAL, self.DOWN):
                    process_node(lines, r+2, c, neighbours, visited, node_stack, coord_stack)
        
        self.data = sort_graph(self.data)

    def load(self) -> dict:
        with open(str(self.path), 'r') as file:
            lines = [list(line.strip()) for line in file.readlines()]
        self._parse(lines)
        return self.data
    
    def save(self):
        raise NotImplementedError()
