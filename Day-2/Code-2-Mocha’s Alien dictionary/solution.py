def can_be_segmented(s, dictionary):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for word in dictionary:
            if dp[i - len(word)] and s[i - len(word):i] == word:
                dp[i] = True

    return dp[n]

# Input handling
s = input().strip()
n = int(input())
dictionary = [input().strip() for _ in range(n)]

# Check if the string can be segmented using the dictionary
result = can_be_segmented(s, dictionary)

# output
print("true" if result else "false")
