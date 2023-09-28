# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
merged_list = list(map(int, input().split()))

product_ids = merged_list[:n]
product_sizes = merged_list[n:]

recovered_list = []
for i in range(n):
    recovered_list.append(product_ids[i])
    recovered_list.append(product_sizes[i])

print(*recovered_list)
