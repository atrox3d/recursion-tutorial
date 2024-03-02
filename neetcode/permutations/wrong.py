def perms(nums:list, cast=tuple, duplicates=False, sort=True, reverse=True):
    def _perms(nums: list[int], level=0) -> list[list[int]]:
        result = []
        if len(nums) == 1: return [nums[:]] # base case
        
        for i, value in enumerate(nums):
            # in every loop value must not be inside the array
            new_nums = nums[:i] + nums[i+1:]
            perms = _perms(new_nums, level+1)
            for perm in perms:
                perm.append(value)
            result.extend(perms)
        return result
    
    result = _perms(nums)
    if not duplicates:
        result = list(set([tuple(perm) for perm in result]))
    result = [cast(perm) for perm in result]
    if sort:
        result = sorted(result)
    if reverse:
        result = list(reversed(sorted(result)))
    return result

if __name__ == '__main__':
    nums = [1, 2, 3]
    nums = [10, 9, 8]
    nums = [9, 1, 0]
    nums = [8, 2, 0, 0]
    perms = perms(nums)
    print(perms, len(perms))