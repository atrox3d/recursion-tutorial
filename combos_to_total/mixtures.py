def mixtures(total: int, columns: int):
    if columns == 1:
        start = total
    else:
        start = 0

    for i in range(start, total + 1):
        left = total - i
        if columns - 1:
            for y in mixtures(left, columns - 1):
                yield tuple([i]) + y
        else:
            yield tuple([i])

def mixtures_list(total: int, ingredients: int, level=0):
    if ingredients == 1:
        start = total
    else:
        start = 0

    combos = []
    for spoons in range(start, total + 1):
        left = total - spoons
        if ingredients - 1 > 0:
            mixes = mixtures_list(left, ingredients - 1, level+1)
            for mix in mixes:
                combos.append(tuple([spoons]) + mix)
        else:
            combos.append(tuple([spoons]))
    return combos


if __name__ == '__main__':
    mix1 = list(mixtures(5, 4))
    mix2 = mixtures_list(5, 4)
    # print(mix2)
    # print(len(mix2))
    assert mix1 == mix2
    print(mix1)
    print(mix2)
    print('ok')