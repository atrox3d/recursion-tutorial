def collatz(n):
    '''
    the collatz conjecture applies to positive integers and
    speculates that is always possible to get back to 1
    if you follow these steps:
    - if n is 1, stop
    - if n is even repeat for n/2
    - if n is odd repeat for 3n+1 
    '''
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + collatz(n/2)
    else:
        return 1 + collatz(3*n+1)

print(collatz(1))
print(collatz(2))
print(collatz(3))
print(collatz(5))
