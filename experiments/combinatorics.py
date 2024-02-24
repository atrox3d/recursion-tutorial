import logging

logger = logging.getLogger(__name__)

def f(total, columns, start=0):
    '''
    good.
    https://stackoverflow.com/a/74454054
    '''
    if columns < start:
        return []
    if columns == start:
        return [(total,)]
    if columns == 2:
        ret = [(i,total-i) for i in range(start, total-columns+2+1)]
        return ret
    
    return [tup[:-1] + ab 
            for tup in f(total, columns-1) 
            for ab in f(tup[-1], 2)]

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG', format='%(message)s')
    # print(f(5, 4))
    print(f(4, 2))
