def bestsum(targetsum: int, numbers: list, memo=None) -> list:
    '''
    write a function that takes in a targersum and an array of
    numbers as argument

    the function should return an array containing the shortest
    combination of numbers that add up to exactly the taegetsum

    if there is a tie for the shortest combination, you may return
    any one of the shortest

    brute force:
    time: O(len(numbers)^targetsum * targetsum)
    space: O(targetsum^2)

    memoized:
    time: O(targetsum^2 * len(numbers))
    space: O(targetsum^2)

    '''
    memo = {} if memo is None else memo
    try:
        return memo[targetsum]
    except:
        pass

    if targetsum == 0: return []
    if targetsum <0: return None

    shortest = None
    for num in numbers:
        remainder = targetsum - num
        result = bestsum(remainder, numbers, memo)
        if result is not None:
            combo = [*result, num]
            if shortest is None or len(combo) < len(shortest):
                shortest = combo
    try:
        memo[targetsum] = shortest
    except:
        pass

    return shortest

data = (
    (7, [5, 3, 4, 7]),
    (8, [2, 3, 5]),
    (8, [1, 4, 5]),
    (100, [1, 2, 5, 25]),
)

for targetsum, numbers in data:
    outer_memo = {}
    result = bestsum(targetsum, numbers, outer_memo)
    print(f'{targetsum = }')
    print(f'{numbers = }')
    print(f'{result = }')
    print(f'{outer_memo = }')
