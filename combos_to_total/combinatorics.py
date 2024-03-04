import logging

logger = logging.getLogger(__name__)

def combos_for_total(total, columns, start=0):
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
            for tup in combos_for_total(total, columns-1) 
            for ab in combos_for_total(tup[-1], 2)]

if __name__ == '__main__':
    logging.basicConfig(level='DEBUG', format='%(message)s')
    # print(f(5, 4))
    print(combos_for_total(5, 4))
