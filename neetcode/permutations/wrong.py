def perms(nums:list, cast=tuple, duplicates=False):
    def _perms(nums: list[int], level=0) -> list[list[int]]:
        # print(f'wrong: {level, nums = }')
        result = []
        # base case
        if len(nums) == 1:
            return [nums[:]]
        
        for i, value in enumerate(nums):
            '''
            in every loop value must not be inside the array
            '''
            # comprehension
            new_nums = [n for n in nums if n != value]
            # slice
            new_nums = nums[:i] + nums[i+1:]
            perms = _perms(new_nums, level+1)

            for perm in perms:
                perm.append(value)
            result.extend(perms)
        return result
    result = _perms(nums)

    if not duplicates:
        result = list(set([tuple(perm) for perm in result]))
    else:
        result = [cast(perm) for perm in result]
    return result

if __name__ == '__main__':
    nums = [1, 2, 3]
    nums = [10, 9, 8]
    nums = [9, 1, 0]
    nums = [8, 2, 0, 0]
    perms = perms(nums)
    print(perms, len(perms))