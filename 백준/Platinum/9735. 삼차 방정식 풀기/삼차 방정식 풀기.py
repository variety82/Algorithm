import sys
import math
input = sys.stdin.readline

def bread(a, b, c, d):
    for x in range(-1000000, 1000000 + 1):
        if(a * x ** 3 + b * x ** 2 + c *x + d == 0):
            alpha = a
            beta = x * alpha + b
            gamma = beta * x + c
            break
    return x, alpha, beta, gamma            


def root_foluma(a, b, c):
    if(b ** 2 - 4 * a * c) < 0:
        return []
    x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return [x, x2]


T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    sol, alpha, beta, gamma = bread(a, b, c, d)
    root = [sol]
    root += root_foluma(alpha, beta, gamma)
    root = sorted(set(root))
    print(*root)
