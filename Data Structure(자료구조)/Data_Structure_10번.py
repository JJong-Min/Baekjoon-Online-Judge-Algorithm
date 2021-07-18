# 풀이 1
def twoSum1(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]


# 풀이 2
def twoSum2(nums, target):
    for i, n in enumerate(nums):
        new_target = target - nums[i]

        if new_target in nums[i+1:]:
            return [nums.index(n), nums.index(new_target)]
            

# 풀이 3
def twoSum3(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]:
            return [nums.index(num), nums_map[target-num]]

# 풀이 4
def twoSum4(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target-num in nums_map:
            return [nums_map[target-num], i]
        nums_map[num] = i

nums = [2, 5, 7, 9, 10]
target = 9
print(twoSum1(nums, target))
print(twoSum2(nums, target))
print(twoSum3(nums, target))
print(twoSum4(nums, target))
