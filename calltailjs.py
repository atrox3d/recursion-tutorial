def iter_sumnats(n):
    '''
    benefits:
    - gets the job done, but could be cleaner
    - more intuitive for devs who have exp w iteration
    problems:
    - verbose cose, describing each step (imperative)
    '''
    result = 0      # tail call default parameter
    
    while n >= 1:
        result = result + n         
                    #  |
                    #  +-> tail call param update
                    #  +-> linear return
        
        n = n - 1                   # recursive param update
    return result

def linear_sumnats(n):              # n = initial value
    if n <= 0:                      # base case
        return 0
    return n + linear_sumnats(n-1)  # recursive case
        #    |                 |
        #    |                 +-> while decrease
        #    +-> while accumulator

def tailcall_sumnats(n, result=0):
                        # |
                        # +-> while init

    if n <= 0:                      # -> linear base case 
        return result               # -> linear base case return

    return tailcall_sumnats(n-1, result+n)
                        #    |      |
                        #    |      +-> while accumulator
                        #    |      +-> linear return
                        #    +-> while decrease
                        #    +-> linear decrease 

print(iter_sumnats(3))
print(linear_sumnats(3))
print(tailcall_sumnats(3))