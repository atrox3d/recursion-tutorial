def get_combinations(target, num_elements, combinations=None, start=0):
    # Initialise an empty list
    if combinations == None:
        combinations = []
    # Calculate the sum of the current list of numbers
    combinations_sum = sum(combinations)
    # Check if the target is reached -> No further recursion necessary
    if (combinations_sum == target and len(combinations) == num_elements):
        # Return this combination of numbers
        yield tuple(combinations)
    else:
        # The combination of numbers doesn't yet total to target value
        # Iterate over each number from 1 to the target value 
        for number in range(start, target + 1):
            # Check that neither the target value nor number of elements will be exceeded
            if (combinations_sum + number <= target 
                and len(combinations) < num_elements):
                # Add the number to the list
                new_combo = combinations + [number]
                # Find all solutions for the list
                for c in get_combinations(target, num_elements, new_combo):
                    yield c


print(list(get_combinations(4, 2)))