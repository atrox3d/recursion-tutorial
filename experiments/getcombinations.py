def get_combinations(target, num_elements, combinations=None, start=0):
    # Initialise an empty list
    if combinations == None:
        combinations = []
    # Calculate the sum of the current list of numbers
    combinations_sum = sum(combinations)
    # Check if the target is reached -> No further recursion necessary
    if combinations_sum == target:
        if len(combinations) == num_elements:
            # Return this combination of numbers
            return [tuple(combinations)]
    else:
        combos = []
        if len(combinations) < num_elements:
            # The combination of numbers doesn't yet total to target value
            # Iterate over each number from 1 to the target value 
            for number in range(start, target + 1):
                # Check that neither the target value nor number of elements will be exceeded
                if combinations_sum + number <= target:
                    # Add the number to the list
                    new_combo = combinations + [number]
                    # Find all solutions for the list
                    # empty generator == []
                    # temp = list(get_combinations(target, num_elements, new_combo))
                    temp = get_combinations(target, num_elements, new_combo)
                    # temp = [] if temp is None else temp
                    # temp = [temp] if isinstance(temp, tuple) else temp
                    # for c in temp:
                        # return c
                    if temp:
                        for t in temp:
                            combos.append(t)
        return combos
if __name__ == '__main__':
    from pathlib import Path
    import sys
    import logging

    print(list(get_combinations(4, 3)))

    if False:
        LOGFILE = str(Path(sys.argv[0]).parent / Path(__file__).stem) + '.log'
        handlers = [logging.FileHandler(LOGFILE, mode='w'), logging.StreamHandler()]
        
        logging.basicConfig(level='INFO', format='%(message)s', handlers=handlers)
        logger = logging.getLogger(__name__)
        
        # print(f(4, 3))
        print(list(get_combinations(4, 2)))
        for combo in get_combinations(100, 4):
            logger.info(combo)