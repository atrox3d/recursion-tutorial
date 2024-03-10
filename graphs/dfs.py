from loaders.jsongraph import JsonGraph
from loaders.txtgraphs import TxtGraph

class Stack(list):
    ''' adds alias method push to list '''
    def push(self, *args, **kwargs):
        return self.append(*args, **kwargs)

def depthfirst(graph: list[list[str]], source:str, print=lambda *args, **kwargs:None):
    stack = Stack([source])                 # start from source

    while len(stack):                       # process all stack
        current = stack.pop()               # pop next node
        print(current)

        for neighbour in graph[current]:    # push node neighbours
            stack.push(neighbour)
        

if __name__ == '__main__':
    tg = TxtGraph('graphs/graph.txt')
    graph = tg.load()

    for k, v in graph.items():
        print(f'{k}: {v}')
    
    depthfirst(graph, 'A', print)
