from loaders.jsongraph import JsonGraph
from loaders.txtgraphs import TxtGraph

def depthfirst(graph: list[list[str]], source:str, print=lambda *args, **kwargs:None):
    stack = [source]

    while len(stack):
        current = stack.pop()
        print(current)

        for neighbour in graph[current]:
            stack.append(neighbour)
        

if __name__ == '__main__':
    tg = TxtGraph('graphs/graph.txt')
    graph = tg.load()

    for k, v in graph.items():
        print(f'{k}: {v}')
    
    depthfirst(graph, 'A', print)
