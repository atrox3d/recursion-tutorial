def find_binary(decimal: int, result: str='') -> str:
    if decimal == 0:
        print(f'{decimal = }: return {result}')
        return result
    
    intdiv = decimal // 2
    modulus = decimal % 2
    print(f'{decimal = }: {intdiv = }, {modulus = }')
    
    result = str(modulus) + result
    print(f'{decimal = }: {result = }')

    print(f'call: {intdiv, result = }')
    ret =  find_binary(intdiv, result)
    print(f'return {ret = }')
    return ret

print(find_binary(4))
