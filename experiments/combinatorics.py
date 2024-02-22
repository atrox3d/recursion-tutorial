import logging

logger = logging.getLogger(__name__)

def f(sum, k):
    '''
    good.
    https://stackoverflow.com/a/74454054
    '''
    logger.debug(f'ENTER: {sum=}, {k=}')
    if k < 1:
        logger.debug(f'{k=} < 1, return []')
        return []
    if k == 1:
        logger.debug(f'k == {k} , return [({sum=},)]')
        return [(sum,)]
    if k == 2:
        logger.debug(f'k == {k}')
        logger.debug(f'return [(i,{sum}-i) for i in range(1, {sum}-{k}+2)]')
        ret = [(i,sum-i) for i in range(1, sum-k+2)]
        logger.debug(f'return {ret}')
        return ret
    
    logger.debug('RECURSIVE CASE')
    return [tup[:-1] + ab 
            for tup in f(sum, k-1) 
            for ab in f(tup[-1], 2)]

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG', format='%(message)s')
    print(f(5, 3))
