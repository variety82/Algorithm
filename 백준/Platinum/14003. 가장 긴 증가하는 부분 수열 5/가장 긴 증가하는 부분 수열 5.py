import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
answer = []
seq = [-1000000001]
seq_idx = [0] * (N + 1)

for i in range(len(A)):
    if seq[-1] < A[i]:
        seq.append(A[i])
        seq_idx[i] = len(seq) - 1
    else:
        idx = bisect_left(seq, A[i])
        seq_idx[i] = idx
        seq[idx] = A[i]

length = len(seq) - 1
print(length)
for i in range(N, -1, -1):
    if seq_idx[i] == length:
        answer.append(A[i])
        length -= 1

print(*answer[::-1])