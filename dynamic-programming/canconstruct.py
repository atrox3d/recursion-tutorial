def canconstruct(target: str, wordbank: list[str], memo: dict=None) -> bool:
    '''
    write a function canconstruct(target, wordbank) that accepts 
    a target string and an array of strings as arguments

    the function should return a boolelan indicating wether
    or not target can be constructed by concatenating elements of
    the wordbank array

    you may reuse elements of wordbank as many times as needed
    '''
    memo = {} if memo is None else memo
    try:
        return memo[target]
    except: pass
    if target == '': return True

    for word in wordbank:
        if target.startswith(word):
            result = canconstruct(target[len(word):], wordbank, memo)
            try:
                memo[target] = result
            except: pass

            if result == True:
                return True
    return False

data = (
    ('abcdef', 'ab abc cd def abcd'.split()),
    ('skateboard', 'bo rd ate t ska sk boar'.split()),
    ('enterapotentpot', 'a p ent enter ot o t'.split()),
    ('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', 
     'e ee eee eeee eeeee eeeeee'.split()),
)

for target, wordbank in data:
    outer_memo = {}
    print(f'{target = }')
    print(f'{wordbank = }')
    result = canconstruct(target, wordbank, outer_memo)
    print(f'{result = }')
    print(f'{outer_memo = }')
    print()
