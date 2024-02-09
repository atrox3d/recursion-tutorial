def reverse_string(string: str) -> str:
    print(f'{string = }')
    if string == '':
        print(f'return \'\'')
        return string
    
    print(f'call: {string[1:]!r} + {string[0]}')
    rev  = reverse_string(string[1:]) 
    ret = rev + string[0]
    print(f'return {rev} + {string[0]}')
    return ret

def print_string(string):
    try:
        print(string[0] + string[1:])
        print_string(string[1:])
    except IndexError:
        return

if __name__ == '__main__':
    print(reverse_string('1234'))
    # print_string('hello')