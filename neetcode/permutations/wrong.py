def wrong(nums: list[int], level=0) -> list[list[int]]:
    print(f'wrong: {level, nums = }')
    result = []
    # base case
    if len(nums) == 1:
        return [nums[:]]
    
    for i, value in enumerate(nums):
        perms = wrong(nums[:i] + nums[i+1:], level+1)

        for perm in perms:
            perm.append(value)
        result.extend(perms)
    return result

if __name__ == '__main__':
    nums = [1, 2, 3]
    print(nums)
    print(perms1:=wrong(nums))
