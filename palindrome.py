def is_palindrome(string: str) -> bool:
    if len(string) <= 1:
        print(f'{string = }: {len(string) = }, return True')
        return True
    
    if string[0] == string[-1]:
        print(f'{string = }: {string[0]} == {string[-1]}')
        string = string[1:-1]
        print(f'{string = }: call: {string}')
        ret = is_palindrome(string)
        print(f'{string = }: return {ret = }')
        return ret
    
    print(f'{string = }: {string[0]} != {string[-1]}, return False')
    return False

print(is_palindrome('racecar'))