
# import sys
# print(sys.path)
from loaders.jsongraph import JsonGraph
from loaders.txtgraphs import TxtGraph

if __name__ == '__main__':

    tg = TxtGraph('graphs/graph.txt')
    # print(tg.UP)
    tg.load()
    for k, v in tg.data.items():
        print(k, ':', v)

    jg = JsonGraph('graphs/graph.json')
    jg.load()
    print(jg.data)

    jg.data['a'] = []
    jg.save()
