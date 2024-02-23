import logging

logger = logging.getLogger(__name__)

INDENTLEVEL = None
INDENTSTEP = 2
INDENTCHAR = '.'
INDENT = None

LOGGERMETHOD = logger.debug

def getindent():
    global INDENTLEVEL, INDENT, INDENTSTEP
    INDENTLEVEL = 0 if INDENTLEVEL is None else INDENTLEVEL+INDENTSTEP
    INDENT = INDENTLEVEL * INDENTCHAR
    return INDENT

def log(message, loggermethod=LOGGERMETHOD):
    message = f'{INDENT}{message}'
    loggermethod(message)

def f(sum, k):
    '''
    good.
    https://stackoverflow.com/a/74454054
    '''
    INDENT = getindent()
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
        for i in range(1, sum-k+2):
            combo = (i, sum-i)
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
        abs = f(tup[-1], 2)
        for ab in abs:
            ret.append(tup[:-1] + ab)
    return ret

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG', format='%(message)s')
    print(f(5, 3))
