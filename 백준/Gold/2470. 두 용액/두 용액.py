import sys

input = sys.stdin.readline
N = int(input())
data = sorted(list(map(int, input().split())))
start, end = 0, N - 1
left_idx, rigth_idx = start, end
M = int(1e10) * 2

while(start < end):
    _sum = data[start] + data[end]
    if(_sum == 0):
        left_idx, right_idx = start, end
        break
    if(abs(_sum) < M):
        left_idx, right_idx = start, end
        M = abs(_sum)
    if(_sum < 0):
        start += 1
    else:
        end -= 1
print(data[left_idx], data[right_idx])
