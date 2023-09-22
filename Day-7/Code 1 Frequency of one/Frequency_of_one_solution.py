def count_set_bits(n):
    count = 0
    while n:
        count += 1
        n &= (n - 1)
    return count

def total_set_bits_from_1_to_n(n):
    total_count = 0
    for i in range(1, n + 1):
        total_count += count_set_bits(i)
    return total_count

n = int(input().strip())
result = total_set_bits_from_1_to_n(n)
print(result)
