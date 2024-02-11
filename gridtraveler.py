def gridtraveler(m: int, n: int, memo={}) -> int:
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

memo = {}
print(gridtraveler(3, 3, memo))
print(memo)

memo = {}
print(gridtraveler(18, 18, memo))

memo = {}
print(gridtraveler(100, 100, memo))
