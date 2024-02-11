def gridtraveler(m: int, n: int, memo={}) -> int:
    if memo is not None:
        key = (m, n)
        if key in memo:
            return memo[key]

    if m == n == 1: return 1
    if 0 in (m, n): return 0

    ret = gridtraveler(m-1, n, memo) + gridtraveler(m, n-1, memo)
    if memo is not None:
        memo[key] = ret
    
    return ret

memo = {}
print(gridtraveler(1, 1, memo))

memo = {}
print(gridtraveler(2, 3, memo))

memo = {}
print(gridtraveler(3, 3, memo))

memo = {}
print(gridtraveler(18, 18, memo))