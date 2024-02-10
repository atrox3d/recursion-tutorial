def recursive_sum(n:int) -> int:
    if n <= 1:
        return n
    
    return n + recursive_sum(n-1)


print(recursive_sum(int(input('number: '))))
