# Code
def count_set_bits(n):
    count = 0
    for i in range(1, n + 1):
        count += bin(i).count('1')
    return count

# Input
N = int(input())

# Result
result = count_set_bits(N)
print(result)
