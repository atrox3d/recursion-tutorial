def possible_recipes4(total_amount, start=1, print_steps=True):
    amounts = []
    for amount1 in range(start, total_amount+1):
        rest1 = total_amount - amount1
        for amount2 in range(start, rest1+1):
            rest2 = rest1 - amount2
            for amount3 in range(start, rest2+1):
                amount4 = rest2 - amount3
                # print_header()
                assert amount1+amount2+amount3+amount4 == total_amount
                amounts.append((amount1, amount2, amount3, amount4))
    return amounts

def base(target, start):
    for amount in range(start, target):
        result = target - amount
        print(f'{start, target = } -> {amount, result = }')

base(5, 0)
