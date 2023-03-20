N = int(input())
seq = list(map(int, input().split()))
dp = [1] * N

for i in range(N):
    pos = seq[i]
    for j in range(i, N):
        if(pos < seq[j]):
            dp[j] = max(dp[j], dp[i] + 1)
print(max(dp)) 