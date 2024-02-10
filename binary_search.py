def binary_search(array: list, left: int, right: int, x) -> int:
    if left > right:
        return -1
    
    mid = int((left + right) / 2)

    if x == array[mid]:
        return mid
    
    if x < array[mid]:
        return binary_search(array, left, mid -1, x)
    
    return binary_search(array, mid +1, right, x)

array = list(range(-1, 20))
for x in range(-2, 20):
    y = binary_search(
        array,
        0,
        len(array) -1,
        x
    )
    print(x, y)