import sys
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
start, end = 0, N - 1
start_idx, end_idx = 0, N - 1
M = int(1e10) * 2


while(start < end):
    _sum = data[start] + data[end]
    if(_sum == 0):
        start_idx, end_idx = start, end
        break
    if(abs(_sum) < M):
        start_idx, end_idx = start, end
        M = abs(_sum)
    if(_sum < 0):
        start += 1
    else:
        end -= 1
print(data[start_idx], data[end_idx])

