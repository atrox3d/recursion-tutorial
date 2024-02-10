def fib(n: int, cache=None) -> int:
    if n in (0, 1):
        return n
    
    if cache is not None:
        try:
            return cache[n]
        except KeyError:
            cache[n] = fib(n-1, cache) + fib(n-2, cache)
            return cache[n]
    else:
        ret = fib(n-1, cache) + fib(n-2, cache)
        return ret

cache = {}
print(fib(30, cache=cache))
print(cache)