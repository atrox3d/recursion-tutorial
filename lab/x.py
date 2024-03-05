def x(target, portions):
    res = []
    buckets = [0 for x in range(portions)]
    for i in range(portions-1):
        buckets[i] = target
        for x in range(target):
            buckets[i] -= 1
            buckets[i+1] += 1
            print(buckets)
            res.append(tuple(buckets))
    return res

def y(total_amount, columns, start=0, print_steps=True):
    print(f'{total_amount, columns = }')
    if not columns:
        return []
    
    columns -= 1
    amounts = []
    
    for amount in range(start, total_amount+1):
        rest = total_amount - amount
        amounts.append(amount)
        a = y(rest, columns)
        print(f'{a = }')
        # for b in a:
        # amounts.extend(a)
        # for amount2 in range(start, rest1+1):
        #     rest2 = rest1 - amount2
        #     for amount3 in range(start, rest2+1):
        #         amount4 = rest2 - amount3
        #         # print_header()
        #         assert amount1+amount2+amount3+amount4 == total_amount
        #         amounts.append((amount1, amount2, amount3, amount4))
    return amounts

print(y(5, 2))
