import logging

logger = logging.getLogger(__name__)

def f(sum, k, start=0):
    '''
    good.
    https://stackoverflow.com/a/74454054
    '''
    if k < start:
        return []
    if k == start:
        return [(sum,)]
    if k == 2:
        ret = [(i,sum-i) for i in range(start, sum-k+2+1)]
        return ret
    
    return [tup[:-1] + ab 
            for tup in f(sum, k-1) 
            for ab in f(tup[-1], 2)]

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG', format='%(message)s')
    # print(f(5, 4))
    print(f(4, 2))
