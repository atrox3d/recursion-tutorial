from combinatorics import combos_for_total
from getcombinations import get_combinations

combos1 = combos_for_total(100, 4)
combos2 = list(get_combinations(100, 4))

print(len(combos1))
print(len(combos2))
assert combos1 == combos2 # True
