def gridtraveler(m: int, n: int, memo:dict=None) -> int:
    '''
    Say that you have a traveler on a 2D grid.
    You begin in the top-left corner and your goal is to
    travel to the bottom-right corner.
    you may only move down or right.

    In how many ways can you travel to the goal on a grid with 
    dimension m * n ?

    write a function gridtraveler(m, n) that calculates this
    '''
    memo = {} if memo is None else memo
    try:
        key = (m, n)
        if key in memo:
            return memo[key]
    except TypeError:
        pass

    if m == n == 1: return 1
    if 0 in (m, n): return 0

    ret = gridtraveler(m-1, n, memo) + gridtraveler(m, n-1, memo)
    
    try:
        memo[key] = ret
    except TypeError:
        pass

    return ret


print(gridtraveler(1, 1))
print(gridtraveler(2, 3))

# memo = {}
print(gridtraveler(3, 3))
# print(memo)

memo = {}
print(gridtraveler(18, 18, memo))

memo = {}
print(gridtraveler(100, 100, memo))
