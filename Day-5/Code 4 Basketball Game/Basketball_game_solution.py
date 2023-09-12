
def check(arr):
    temp = []
    
    for i in arr:
        if i.isdigit() or (i[0] == '-' and i[1:].isdigit()):
            temp.append(int(i))
        elif i=="C":
            temp.pop()
        elif i=="D":
            num1 = temp.pop()
            temp.extend([num1, 2*num1])
        elif i=="+":
            num1 = temp.pop()
            num2 = temp.pop()
            temp.extend([num2, num1, num1 + num2])
        
    return sum(temp)
        
    
    
n = int(input())
arr = input().split()
    
print(check(arr))
