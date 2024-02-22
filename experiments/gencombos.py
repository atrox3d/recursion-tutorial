
def gencombos( target, column ):
    '''
    https://stackoverflow.com/a/70342171
    does not work well
    '''
    if column == 1:
        yield [target]
    else:
        # print(f'for i in range( 0, target//column+1 ):')
        # print(f'for i in range( 0, {target//column+1} ):')
        for i in range( 0, target//column+1 ):
            # print(f'for row in gencombos( target-i*column, column-1 ):')
            # print(f'for row in gencombos( {target-i*column}, {column-1} ):')
            for row in gencombos( target-i*column, column-1 ):
                yield row+[i]

# for row in gencombos( 7, 3 ):
    # print(row)

def f(sum, k):
    '''
    good.
    https://stackoverflow.com/a/74454054
    '''
    if k < 1:
        return []
    if k == 1:
        return [(sum,)]
    if k == 2:
        return [(i,sum-i) for i in range(1, sum-k+2)]
    
    return [tup[:-1] + ab for tup in f(sum, k-1) for ab in f(tup[-1], 2)]

print(f(10, 2))