import logging

logger = logging.getLogger(__name__)

INDENTLEVEL = None
INDENTSTEP = 4
INDENTCHAR = ' '
INDENT = None

LOGGERMETHOD = logger.debug

def log(message, loggermethod=LOGGERMETHOD):
    message = f'{INDENT}{message}'
    loggermethod(message)

def indented(func):
    def wrapper(*args, **kwargs):
        global INDENTLEVEL, INDENT, INDENTSTEP
        if INDENTLEVEL is None:
            INDENTLEVEL = 0
        else:
            INDENTLEVEL += INDENTSTEP
        INDENT = INDENTLEVEL * INDENTCHAR
        ret = func(*args, **kwargs)
        if INDENTLEVEL > 0:
            INDENTLEVEL -= INDENTSTEP
            INDENT = INDENTLEVEL * INDENTCHAR
        return ret
    return wrapper

@indented
def f(sum, k):
    '''
    good.
    https://stackoverflow.com/a/74454054
    '''
    if k < 1:
        log(f'BASE CASE: {sum=}, {k=}')
        log(f'BASE CASE: {k} < 1, return []')
        return []
    if k == 1:
        log(f'BASE CASE: {sum=}, {k=}')
        log(f'BASE CASE: k == {k} , return [({sum=},)]')
        return [(sum,)]
    if k == 2:
        log(f'BASE CASE: {sum=}, {k=}')
        log(f'BASE CASE: k == {k}')
        log(f'BASE CASE: return [(i,{sum}-i) for i in range(1, {sum}-{k}+2)]')
        # ret = [(i,sum-i) for i in range(1, sum-k+2)]
        ret = []
        # for i in range(1, sum-k+2):
        for i, j in zip(range(1, sum), range(sum-1, 0, -1)):
            combo = (i, j)
            log(f'BASE CASE: {combo=}')
            ret.append(combo)
        log(f'BASE CASE: return {ret}')
        return ret
    
    log(f'RECURSIVE CASE: {sum=}, {k=}')
    # ret = [tup[:-1] + ab for tup in f(sum, k-1) for ab in f(tup[-1], 2)]
    ret = []
    log(f'RECURSIVE CASE: tups = f(sum={sum}, k=({k}-1))')
    tups = f(sum, k-1)
    log(f'RECURSIVE CASE: {tups=}')
    for tup in tups:
        log(f'RECURSIVE CASE: {tup=}')
        log(f'RECURSIVE CASE: {tup[-1]=}')
        log(f'RECURSIVE CASE: abs=f(sum={tup[-1]}, "2")')
        abs = f(tup[-1], 2)
        for ab in abs:
            log(f'RECURSIVE CASE: {ab=}')
            log(f'RECURSIVE CASE: {tup[:-1]=}')
            log(f'RECURSIVE CASE: {tup[:-1]+ab=}')
            ret.append(tup[:-1] + ab)
    return ret

if __name__ == '__main__':
    LOGGERMETHOD = logger.debug

    logging.basicConfig(level='DEBUG', format='%(message)s')
    # @indented
    # def rec(n):
        # log(n)
        # if n == 0:
            # return
        # rec(n-1)
    # rec(5)
    # 
    print(f(4, 3))