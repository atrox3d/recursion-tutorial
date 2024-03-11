from datastructs import Stack
from loaders.jsongraph import JsonGraph
from loaders.txtgraphs import TxtGraph

dontprint = lambda *args, **kwargs:None


if __name__ == '__main__':
    jg = JsonGraph('graphs/haspath.json')
    # jg.data = {
    #     'F': ['G', 'I'],
    #     'G': ['H'],
    #     'H': [],
    #     'I': ['G', 'K'],
    #     'J': ['I'],
    #     'K': [],
    # }
    data =  jg.load()
    jg.print(data, indent=4)
