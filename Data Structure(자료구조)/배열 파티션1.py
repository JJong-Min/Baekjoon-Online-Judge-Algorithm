#풀이 1
def arrayPairSum1(nums):
    nums.sort()
    pair = []
    answer = 0
    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            answer += min(pair)
            pair = []
    return answer

# 풀이 2
def arrayPairSum2(nums):
    nums.sort()
    answer =0
    for i, n in enumerate(nums):
        if i%2 == 0:
            answer += n
    return answer
# 풀이 3
def arrayPairSum3(nums):
    answer = sum(sorted(nums)[::2])
    return answer

nums = [1,4,3,2]
print(arrayPairSum1(nums))
print(arrayPairSum2(nums))
print(arrayPairSum3(nums))
