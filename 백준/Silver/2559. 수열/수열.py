import sys
input = sys.stdin.readline

N, K = map(int, input().split())
data = list(map(int, input().split()))
start, end = 0, K - 1
M = sum(data[start:end + 1])
_sum = M

while(start < N - K):
    end +=1
    _sum -= (data[start] - data[end])
    start += 1
    M = max(M, _sum)

print(M)
