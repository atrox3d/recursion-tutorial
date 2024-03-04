def possible_recipes5(names, total_amount):
    for amount1 in range(1, total_amount+1):
        rest1 = total_amount - amount1
        for amount2 in range(1, rest1+1):
            rest2 = rest1 - amount2
            for amount3 in range(1, rest2+1):
                rest3 = rest2 - amount3
                for amount4 in range(1, rest3+1):
                    amount5 = rest3 - amount4
                    assert amount1+amount2+amount3+amount4+amount5 == total_amount
                    yield zip(names, [amount1, amount2, amount3, amount4, amount5])
                    
def possible_recipes4(total_amount, start=1, print_steps=True):
    amounts = []
    if print_steps: print_header()
    for amount1 in range(start, total_amount+1):
        rest1 = total_amount - amount1
        for amount2 in range(start, rest1+1):
            rest2 = rest1 - amount2
            for amount3 in range(start, rest2+1):
                amount4 = rest2 - amount3
                # print_header()
                if print_steps: print_state(**locals())
                assert amount1+amount2+amount3+amount4 == total_amount
                amounts.append((amount1, amount2, amount3, amount4))
    return amounts

def print_header():
    print(f'total - amount1 = rest1 - amount2 = rest2 - amount3 = amount4: sum -> tuple')

def print_state(**locals):
    total = locals['total_amount']
    amount1 = locals['amount1']
    amount2 = locals['amount2']
    amount3 = locals['amount3']
    amount4 = locals['amount4']
    rest1 = locals['rest1']
    rest2 = locals['rest2']

    print(f'{total}     - [{amount1}]     = {rest1}     - [{amount2}]     = {rest2}     - [{amount3}]     = [{amount4}]    : '
          f'{amount1+amount2+amount3+amount4}   -> {amount1, amount2, amount3, amount4}')


if __name__ == '__main__':
    amounts = possible_recipes4(5, start=0)
    print(amounts)