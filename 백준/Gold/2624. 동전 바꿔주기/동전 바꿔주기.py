T = int(input())
K = int(input())
coins = []

def make_dp(coins):
    dp = [0] * (T + 1)
    dp[0] = 1
    for coin, cnt in coins:
        for money in range(T, 0, -1):
            for cnt in range(1, cnt + 1):
                if(money - coin * cnt >= 0):
                    dp[money] += dp[money - coin * cnt]
    return dp

for _ in range(K):
    p, n = map(int, input().split())
    coins.append([p, n])
# coins = dict(sorted(coins.items()))
dp = make_dp(coins)
print(dp[T])