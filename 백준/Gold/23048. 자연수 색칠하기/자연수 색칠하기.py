import sys
input = sys.stdin.readline

N = int(input())
arr = list(range(N + 1))
sieve = [True] * (N + 1)
cnt = 2
for i in range(2, N + 1):
    if sieve[i] == True:
        arr[i] = cnt
        for j in range(i * 2, N + 1, i):
            sieve[j] = False
            arr[j] = cnt
        cnt += 1

print(cnt - 1)
print(*arr[1:])