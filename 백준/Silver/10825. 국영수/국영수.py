import sys
from pprint import pprint
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().split())) for _ in range(N)]
arr.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in arr:
    print(student[0])