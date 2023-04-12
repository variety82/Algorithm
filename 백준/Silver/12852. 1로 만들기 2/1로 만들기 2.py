import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
# 숫자, 어디서 왔는지
answer_path = [N]

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    if(i % 3 == 0 and i % 2 == 0):
        dp[i] = min(dp[i // 3] + 1, dp[i // 2] + 1, dp[i -1] + 1)
    elif(i % 3 == 0):
        dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)
    elif(i % 2 == 0):
        dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)
idx = N

while(True):
    if(idx == 1):
        break
    if(idx % 3 == 0 and (dp[idx // 3] == dp[idx] - 1)):
        answer_path.append(idx // 3)
        idx //= 3
    elif(idx % 2 == 0 and (dp[idx // 2] == dp[idx] - 1)):
        answer_path.append(idx // 2)
        idx //= 2
    else:
        answer_path.append(idx - 1)
        idx -= 1
print(dp[N])
print(*answer_path)