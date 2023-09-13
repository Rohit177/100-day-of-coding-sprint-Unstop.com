n = int(input())
nums = list(map(int, input().split()))

squared_nums = [num ** 2 for num in nums]

squared_nums.sort()

print(" ".join(map(str, squared_nums)))
