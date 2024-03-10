from loaders.jsongraph import JsonGraph
from loaders.txtgraphs import TxtGraph

def depthfirst(graph, source):
    ...


if __name__ == '__main__':
    tg = TxtGraph('graphs/graph.txt')
    graph = tg.load()

    for k, v in graph.items():
        print(f'{k}: {v}')

