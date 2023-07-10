import sys
import math
input = sys.stdin.readline

a, b = map(int, input().split())

answer = b * math.log(a, 10)
print(int(answer) + 1)