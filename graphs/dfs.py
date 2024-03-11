from datastructs import Stack
from loaders.jsongraph import JsonGraph
from loaders.txtgraphs import TxtGraph

dontprint = lambda *args, **kwargs:None

def depthfirst(graph: list[list[str]], source:str, print=dontprint):
    stack = Stack([source])                 # start from source

    while len(stack):                       # process all stack
        current = stack.pop()               # pop next node
        print(current)

        for neighbour in graph[current]:    # push node neighbours
            stack.push(neighbour)
        
def rdepthfirst(graph: list[list[str]], source:str, print=dontprint):
    ''' 
    - using implicit function call stack instead of Stack() 
    - the base case is also implicit: graph[source] != []
    '''
    print(source)                             # print current node
    for neighbour in reversed(graph[source]): # get near nodes, if any
                                              # reversed simulates stack obj
        rdepthfirst(graph, neighbour, print)  # recurse on every neighbour


if __name__ == '__main__':
    tg = TxtGraph('graphs/graph.txt')
    tg.load()
    graph = tg.sorted(keys=True)
    for k, v in graph.items():
        print(f'{k}: {v}')
    
    print()
    depthfirst(graph, 'A', print)
    print()
    rdepthfirst(graph, 'A', print)
