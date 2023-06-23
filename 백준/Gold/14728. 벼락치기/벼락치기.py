import sys
input = sys.stdin.readline

N, T = map(int, input().split())
dp = [[0] * (T + 1) for _ in range(N + 1)]
W = [0]
V = [0]

for _ in range(N):
    K, S = map(int, input().split())
    W.append(K)
    V.append(S)

for i in range(1, N + 1):
    for w in range(T + 1):
        if W[i] == 0:
            dp[i][w] = 0
        if W[i] > w:
            dp[i][w] = dp[i - 1][w]
        else:
            dp[i][w] = max(dp[i - 1][w], V[i] + dp[i - 1][w - W[i]])
print(dp[N][T])