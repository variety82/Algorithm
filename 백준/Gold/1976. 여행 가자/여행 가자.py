import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
parent = list(range(N + 1))


def find(parent, x):
    if(parent[x] != x):
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if(a < b):
        parent[b] = a
    else:
        parent[a] = b

graph = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if(graph[i][j] == 1):
            union(parent, i + 1, j + 1)

root = list(map(int, input().split()))

flag = True
pre_root = parent[root[0]]

for i in range(1, M):
    if(pre_root != parent[root[i]]):
        flag = False
        break

print("YES" if(flag) else "NO")
