def minDifficulty(taskdifficulty, d):
    n = len(taskdifficulty)
    if n < d:
        return -1
      
    # Initialize dp array with maximum values
    dp = [[float('inf')] * (d + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    
    for i in range(1, n + 1):
        for j in range(1, d + 1):
            max_difficulty = 0
            for k in range(i - 1, j - 2, -1):
                max_difficulty = max(max_difficulty, taskdifficulty[k])
                dp[i][j] = min(dp[i][j], dp[k][j - 1] + max_difficulty)
    
    return dp[n][d] if dp[n][d] != float('inf') else -1

# Input
n = int(input())
taskdifficulty = list(map(int, input().split()))
d = int(input())

# Output
print(minDifficulty(taskdifficulty, d))
