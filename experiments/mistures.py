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

def mixtures_list(total: int, n: int):
    if n == 1:
        start = total
    else:
        start = 0

    combos = []
    for i in range(start, total + 1):
        left = total - i
        if n - 1:
            for y in mixtures_list(left, n - 1):
                combos.append([i] + y)
        else:
            combos.append([i])
    return combos


if __name__ == '__main__':
    mix1 = list(mixtures(4, 3))
    mix2 = mixtures_list(3, 4)
    # print(mix2)
    # print(len(mix2))
    assert mix1 == mix2
    print('ok')