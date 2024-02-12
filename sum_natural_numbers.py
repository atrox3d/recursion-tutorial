def recursive_sum(n:int, stack=None) -> int:
    stack = [] if stack is None else stack
    stack.append(n)

    if n <= 1:
        return n
    
    return n + recursive_sum(n-1, stack)

stack=[]
res = recursive_sum(int(input('number: ')), stack)
print(res, '=',  ' + '.join(map(str, stack)))
