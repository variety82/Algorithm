import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
target = int(input())
answer = arr.count(target)
print(answer)

