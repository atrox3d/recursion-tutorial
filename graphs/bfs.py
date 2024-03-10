from loaders.jsongraph import JsonGraph
from loaders.txtgraphs import TxtGraph

class Queue(list):
    ''' adds alias methods push and shift to list '''
    def push(self, *args, **kwargs):
        return self.append(*args, **kwargs)
    
    def shift(self):
        return self.pop(0)

def breadthfirst(graph: list[list[str]], source:str, print=lambda *args, **kwargs:None):
    stack = Queue([source])                 # start from source

    while len(stack):                       # process all stack
        current = stack.shift()             # shit queue next node
        print(current)

        for neighbour in graph[current]:    # push node neighbours
            stack.push(neighbour)
        

if __name__ == '__main__':
    tg = TxtGraph('graphs/graph.txt')
    graph = tg.load()

    for k, v in graph.items():
        print(f'{k}: {v}')
    
    breadthfirst(graph, 'A', print)
