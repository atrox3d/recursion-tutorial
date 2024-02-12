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

print(cansum(7, [2, 3]))
print(cansum(7, [5, 3, 4, 7]))
print(cansum(7, [2, 4]))
print(cansum(8, [2, 3, 5]))
# 
out_memo = {}
print(cansum(300, [7, 14], out_memo))
print(f'{out_memo = }')