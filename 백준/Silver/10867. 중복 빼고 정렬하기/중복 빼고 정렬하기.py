N = int(input())
arr = list(set([int(x) for x in input().split()]))
arr.sort()
print(*arr)