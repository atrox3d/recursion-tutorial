from datastructs import Queue
from loaders.jsongraph import JsonGraph
from loaders.txtgraphs import TxtGraph

dontprint = lambda *args, **kwargs:None

def breadthfirst(graph: list[list[str]], source:str, print=dontprint):
    stack = Queue([source])                 # start from source

    while len(stack):                       # process all stack
        current = stack.shift()             # shit queue next node
        print(current)

        for neighbour in graph[current]:    # push node neighbours
            stack.push(neighbour)
        
def rbreadthfirst(graph: list[list[str]], source:str, print=dontprint):
    ''' cannot use recursion with bfs because the function call STACK '''
    print(source)
    for neighbour in graph[source]:
        rbreadthfirst(graph, neighbour, print)


if __name__ == '__main__':
    tg = TxtGraph('graphs/graph.txt')
    tg.load()
    graph = tg.sorted(keys=True)
    for k, v in graph.items():
        print(f'{k}: {v}')
    
    print()
    breadthfirst(graph, 'A', print)
    print()
    rbreadthfirst(graph, 'A', print)
