from loaders.jsongraph import JsonGraph
from loaders.txtgraphs import TxtGraph

tg = TxtGraph('graphs/graph.txt')
tg.load()

print(tg.data)