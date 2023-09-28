def maximizeSumOfPairs(nums):
    nums.sort() 
    max_sum = 0
    
    for i in range(0, len(nums), 2):
        max_sum += nums[i]
    
    return max_sum


n = int(input())
nums = list(map(int, input().split()))

result = maximizeSumOfPairs(nums)
print(result)
