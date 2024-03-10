from abc import ABC, abstractmethod

from datastructs import Queue, Stack
from loaders.txtgraphs import TxtGraph

class GraphStrategy(ABC):
    store: Queue | Stack

    @abstractmethod
    def get():
        pass

    @abstractmethod
    def put(value):
        pass

    def __getattr__(self, attr):
        return getattr(self.store, attr)

    def __len__(self):
        return len(self.store)

    
class BreadthFirstStrategy(GraphStrategy):
    store = Queue()

    def get(self):
        return self.store.shift()
    
    def put(self, value):
        self.store.push(value)

class DepththFirstStrategy(GraphStrategy):
    store = Stack()

    def get(self):
        return self.store.pop()
    
    def put(self, value):
        self.store.push(value)

def walk(graph: list[list], source, strategy: GraphStrategy):
    strategy.put(source)

    while len(strategy):
        current = strategy.get()
        print(current)

        for neighbour in graph[current]:    # push node neighbours
            strategy.put(neighbour)

if __name__ == '__main__':
    tg = TxtGraph('graphs/graph.txt')
    tg.load()
    graph = tg.sorted(keys=True)
    for k, v in graph.items():
        print(f'{k}: {v}')
    
    walk(graph, 'A', DepththFirstStrategy())
    print()
    walk(graph, 'A', BreadthFirstStrategy())

