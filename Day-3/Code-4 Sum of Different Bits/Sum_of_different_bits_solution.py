def findTotalSum(a,b):
    n = len(a)
    m = len(b)
    total_sum = 0
    
    for i in range(m - n+1):
        diff_count = 0 
        for j in range(n):
            if a[j] != b[i+j]:
                diff_count += 1 
        total_sum += diff_count
        
    return total_sum
    
a = input().strip()
b = input().strip()

result = findTotalSum(a, b)
print(result)
