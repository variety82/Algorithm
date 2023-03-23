import sys

input = sys.stdin.readline
INF = int(1e5)

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
R, G, B = 0, 1, 2
answer = INF

for color in [R, G, B]:
    dp = [[INF] * 3 for _ in range(N)]
    dp[0][color] = cost[0][color]
    for i in range(1, N):
        dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + cost[i][R]
        dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + cost[i][G]
        dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + cost[i][B]
    dp[N-1][color] = INF
    answer = min(answer, min(dp[N-1]))
print(answer)