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
                    
def possible_recipes4(total_amount, start=1):
    amounts = []
    for amount1 in range(start, total_amount+1):
        rest1 = total_amount - amount1
        for amount2 in range(start, rest1+1):
            rest2 = rest1 - amount2
            for amount3 in range(start, rest2+1):
                amount4 = rest2 - amount3
                assert amount1+amount2+amount3+amount4 == total_amount
                amounts.append((amount1, amount2, amount3, amount4))
    return amounts

if __name__ == '__main__':
    amounts = possible_recipes4(5, start=0)
    print(amounts)