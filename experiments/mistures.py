def mixtures(total: int, columns: int):
    if columns == 1:
        start = total
    else:
        start = 0

    for i in range(start, total + 1):
        left = total - i
        if columns - 1:
            for y in mixtures(left, columns - 1):
                yield [i] + y
        else:
            yield [i]

def mixtures_list(total: int, columns: int):
    if columns == 1:
        start = total
    else:
        start = 0

    combos = []
    for i in range(start, total + 1):
        left = total - i
        if columns - 1:
            for y in mixtures_list(left, columns - 1):
                combos.append([i] + y)
        else:
            combos.append([i])
    return combos


if __name__ == '__main__':
    mix1 = list(mixtures(4, 3))
    mix2 = mixtures_list(4, 3)
    # print(mix2)
    # print(len(mix2))
    assert mix1 == mix2
    print('ok')