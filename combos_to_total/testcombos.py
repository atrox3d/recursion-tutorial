# from combinatorics import combos_for_total
# from getcombinations import get_combinations
import combinatorics
import combinatorics_for
import getcombinations
import getcombinations_list
import mixtures
import recipes

def compare(l1:list[tuple], l2:list[tuple], names: str) -> bool:
    if l1 is l2:
        raise ValueError('cannot compare same list')
    
    if len(l1) != len(l2):
        print(f'DIFFERENT lentgths: {len(l1)} - {len(l2)}', ', '.join(names.split()))
        print()
        return False
    
    if sorted(l1) != sorted(l2):
        print(f'DIFFERENT ordered contents: ', ', '.join(names.split()))
        print()
        return False
    
    if l1 != l2:
        print(f'DIFFERENT unordered contents: ', ', '.join(names.split()))
        print()
        return False

    print(f'EQUAL unordered content: ', ', '.join(names.split()))
    print()
    return True

def norepetitions(l1:list[tuple], name: str) -> bool:
    if sorted(set(l1)) != sorted(l1):
        print(f'REPETITIONS detected in {name}')
        print()
        return False
    return True

combos1 = list(set(combinatorics.combos_for_total(5, 4)))
print(f'{combos1 = }', len(combos1), end='\n\n')
norepetitions(combos1, 'combos1')
combos2 = combinatorics_for.combos_for_total(5, 4)
print(f'{combos2 = }', len(combos2), end='\n\n')
norepetitions(combos2, 'combos2')
compare(combos1, combos2, 'combos1 combos2')

# TODO: check why different
combos3 = list(getcombinations.get_combinations(5, 4))
print(f'{combos3 = }', len(combos3), end='\n\n')
norepetitions(combos3, 'combos3')
combos4 = getcombinations_list.get_combinations(5, 4)
print(f'{combos4 = }', len(combos4), end='\n\n')
norepetitions(combos4, 'combos4')
compare(combos3, combos4, 'combos3 combos4')

combos5 = list(mixtures.mixtures(5, 4))
print(f'{combos5 = }', len(combos5), end='\n\n')
norepetitions(combos5, 'combos5')
combos6 = mixtures.mixtures_list(5, 4)
print(f'{combos6 = }', len(combos6), end='\n\n')
norepetitions(combos6, 'combos6')
compare(combos5, combos6, 'combos5 combos6')

combos7 = recipes.possible_recipes4(5, start=0, print_steps=False)
norepetitions(combos7, 'combos7')
print(f'{combos7 = }', len(combos7), end='\n\n')

compare(combos7, combos6, 'combos7 combos6')
compare(combos7, combos5, 'combos7 combos5')
compare(combos7, combos2, 'combos7 combos2')


assert (combos1 == combos2 == 
        combos3 == combos4 == 
        combos5 == combos6 == 
        combos7), 'lists are different'
