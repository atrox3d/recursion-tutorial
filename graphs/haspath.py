from datastructs import Stack, Queue
from loaders.jsongraph import JsonGraph
from loaders.txtgraphs import TxtGraph

dontprint = lambda *args, **kwargs:None

def dfs_haspath(graph, source, dest, print=dontprint):
    if source == dest:
        print(f'DFS: found {dest}')
        return True
    
    for neighbour in graph[source]:
        print(f'DFS: from {source} to {neighbour}')
        if dfs_haspath(graph, neighbour, dest, print):
            return True
    return False

def bfs_haspath(graph, source, dest, print=dontprint):
    queue = Queue(source)
    while len(queue):
        current = queue.shift()
        if current == dest:
            print(f'BFS: found {dest}')
            return True
        for neighbour in graph[current]:
            print(f'BFS: from {current} to {neighbour}')
            queue.push(neighbour)
    return False

if __name__ == '__main__':
    jg = JsonGraph('graphs/haspath.json')
    data =  jg.load()
    jg.print(data, indent=4)
    '''
    {                       
        'F': ['G', 'I']     F->G->H
        'G': ['H']          |  ^
        'H': []             v /
        'I': ['G', 'K']     I<-J
        'J': ['I']          |
        'K': []             v
    }                       K
    '''
    print()
    print(dfs_haspath(data, 'F', 'K', print))
    print()
    print(bfs_haspath(data, 'F', 'K', print))
