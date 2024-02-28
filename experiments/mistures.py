def mixtures(n: int, total: int):
    if n == 1:
        start = total
    else:
        start = 0

    for i in range(start, total + 1):
        left = total - i
        if n - 1:
            for y in mixtures(n - 1, left):
                yield [i] + y
        else:
            yield [i]

def mixtures_list(n: int, total: int):
    if n == 1:
        start = total
    else:
        start = 0

    for i in range(start, total + 1):
        left = total - i
        if n - 1:
            for y in mixtures(n - 1, left):
                yield [i] + y
        else:
            yield [i]


if __name__ == '__main__':
    mix = list(mixtures(4, 3))
    print(mix)
    print(len(mix))