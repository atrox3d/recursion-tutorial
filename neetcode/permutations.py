def permute(nums: list[int]) -> list[list[int]]:
    result = []
    # base case
    if len(nums) == 1:
        return [nums[:]]
    
    for value in range(len(nums)):
        current = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(current)
        result.extend(perms)
        nums.append(current)
    return result

def permute(nums: list[int]) -> list[list[int]]:
    result = []
    # base case
    if len(nums) == 1:
        return [nums[:]]
    
    for value in nums:
        perms = permute(nums[1:])

        for perm in perms:
            perm.append(value)
        result += perms
    return result

print(permute(nums:=[1, 2, 3]))
print(nums)
