# from combinatorics import combos_for_total
# from getcombinations import get_combinations
import combinatorics
import combinatorics_for
import getcombinations
import getcombinations_list
import mixtures
import recipes

combos1 = list(set(combinatorics.combos_for_total(5, 4)))
print(f'{combos1 = }', len(combos1))
combos2 = combinatorics_for.combos_for_total(5, 4)
print(f'{combos2 = }', len(combos2))

combos3 = list(getcombinations.get_combinations(5, 4))
print(f'{combos3 = }', len(combos3))
combos4 = getcombinations_list.get_combinations(5, 4)
print(f'{combos4 = }', len(combos4))

combos5 = list(mixtures.mixtures(5, 4))
print(f'{combos5 = }', len(combos5))
combos6 = mixtures.mixtures_list(5, 4)
print(f'{combos6 = }', len(combos6))

combos7 = recipes.possible_recipes4(5, start=0)
print(f'{combos7 = }', len(combos7))


assert combos1 == combos2 == combos3 == combos4 == combos5 == combos6 == combos7 # True
