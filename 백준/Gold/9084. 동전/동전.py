T = int(input())

def make_table(coins, goal):
    dp = [0] * (goal + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, goal + 1):
            if(i >= coin):
                dp[i] += dp[i -coin]
    return dp


for _ in range(T):
    N = int(input())
    coins = [int(x) for x in input().split()]
    goal = int(input())
    dp = make_table(coins, goal)
    print(dp[goal])
