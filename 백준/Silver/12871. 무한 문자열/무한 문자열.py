# import sys
import math
# sys.stdin = open("input.txt", "r")
s = input()
t = input()

lcm = math.lcm(len(s), len(t))

s = s * (lcm // len(s))
t = t * (lcm // len(t))

if (s == t):
    print(1)
else:
    print(0)