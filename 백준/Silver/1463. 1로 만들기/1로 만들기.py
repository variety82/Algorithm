X = int(input())

dp = [0] * (X + 1)
for i in range(2, X + 1):
    dp[i] = dp[i-1] + 1
    if(i % 3 == 0 and i % 2 == 0):
        dp[i] = min(dp[i-1] + 1, dp[i // 3] + 1, dp[i // 2] + 1)
    elif(i % 3 == 0):
        dp[i] = min(dp[i-1] + 1, dp[i // 3] + 1)
    elif(i % 2 == 0):
        dp[i] = min(dp[i-1] + 1, dp[i // 2] + 1)
print(dp[X])