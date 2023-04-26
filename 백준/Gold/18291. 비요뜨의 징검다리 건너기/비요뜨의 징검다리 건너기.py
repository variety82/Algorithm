import sys
input = sys.stdin.readline

T = int(input())
c = 10 ** 9 + 7
def power(a, n):
    if(n == 0):
        return 1
    else:
        x = power(a, n // 2)
        if(n % 2 == 0):
            return (x * x) % c
        else:
            return (x * x * a) % c

for _ in range(T):
    N = int(input())
    if(N == 1):
        print(1)
    else:
        print(power(2, N - 2))
