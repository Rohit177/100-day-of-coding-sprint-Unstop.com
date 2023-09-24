def findMiddle(n, arr):
    arr.sort()
    middle_index = n // 2
    middle_element = arr[middle_index]
    return middle_element

# Input
n = int(input())
arr = list(map(int, input().split()))

# Output
print(findMiddle(n, arr))
