n, m = map(int, input().split())

gift_r = [0] * (n+1)
    
gave_gift = set()
    
for i in range(m):
    a, b = map(int, input().split())
    gift_r[b] += 1
    gave_gift.add(a)
        
y = -1
    
for i in range(1, n+1):
    if i not in gave_gift and gift_r [i] == n - 1:
        y = i
        break

print(y)
