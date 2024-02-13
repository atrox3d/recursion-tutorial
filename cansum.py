def cansum(targetsum: int, numbers: list, memo: dict=None) -> bool:
    memo = {} if memo is None else memo
    try:
        ret = memo[targetsum]
        return memo[targetsum]
    except:
        pass

    if targetsum == 0:
        return True
    
    if targetsum < 0:
        return False

    for number in numbers:
        ret = cansum(targetsum-number, numbers, memo)
        try:
            memo[targetsum] = ret
        except:
            pass
        if ret == True:
            return ret
    return False

# print(cansum(7, [2, 3]))
# print(cansum(7, [5, 3, 4, 7]))
# print(cansum(7, [2, 4]))
# print(cansum(8, [2, 3, 5]))
# # 
# out_memo = {}
# print(cansum(300, [7, 14], out_memo))
# print(f'{out_memo = }')

data = (
    (7, [2, 3]),
    (7, [5, 3, 4, 7]),
    (7, [2, 4]),
    (8, [2, 3, 5]),
)

for targetsum, numbers in data:
    outer_memo = {}
    result = cansum(targetsum, numbers, outer_memo)
    print(f'{targetsum = }')
    print(f'{numbers = }')
    print(f'{result = }')
    print(f'{outer_memo = }')
