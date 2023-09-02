# Enter your code here.
def minDifficulty(taskdifficulty, d):
    n = len(taskdifficulty)
    
    if n < d:
        return -1
    
    dp = [[float('inf')] * (n + 1) for _ in range(d + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for k in range(1, min(d, i) + 1):
            maxDifficulty = 0
            for j in range(i, 0, -1):
                maxDifficulty = max(maxDifficulty, taskdifficulty[j - 1])
                dp[k][i] = min(dp[k][i], dp[k - 1][j - 1] + maxDifficulty)
    
    return dp[d][n]


n = int(input())
taskdifficulty = list(map(int, input().split()))
d = int(input())

result = minDifficulty(taskdifficulty, d)
print(result)
