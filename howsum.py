def howsum(targetsum: int, numbers: list) -> list:
    if targetsum == 0:
        return []
    if targetsum < 0:
        return None
    
    for num in numbers:
        ret = howsum(targetsum-num, numbers)
        if ret is not None:
            return ret + [num]
    
    return None

data = (
    (7, [2, 3]),
    (7, [5, 3, 4, 7]),
    (7, [2, 4]),
    (8, [2, 3, 5]),
)

for targetsum, numbers in data:
    array = howsum(targetsum, numbers)
    print(array)
    assert array is None or sum(array) == targetsum


# print(howsum(7, [5, 3, 4, 7]))
# print(howsum(7, [2, 4]))
# print(howsum(8, [2, 3, 5]))
# 
# out_memo = {}
# print(howsum(300, [7, 14]))
# print(f'{out_memo = }')