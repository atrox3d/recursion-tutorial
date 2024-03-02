def permute(nums: list[int], level=0) -> list[list[int]]:
    print(f'permute: {level, nums = }')
    result = []
    # base case
    if len(nums) == 1:
        return [nums[:]]
    
    for value in range(len(nums)):
        current = nums.pop(0)
        perms = permute(nums, level+1)

        for perm in perms:
            perm.append(current)
        result.extend(perms)
        nums.append(current)
    return result

if __name__ == '__main__':
    from wrong import wrong
    nums = [1, 2, 3]
    print(nums)
    print(perms1:=permute(nums))
    print(perms2:=wrong(nums))

    assert sorted(perms1) == sorted(perms2)
