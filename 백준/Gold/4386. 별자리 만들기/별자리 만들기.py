import sys
input = sys.stdin.readline

N = int(input())
parent = [x for x in range(N + 1)]
arr = [tuple(map(float, input().split())) for _ in range(N)]
edges = []

for i in range(N):
    a, b = arr[i]
    for j in range(i + 1, N):
        c, d = arr[j]
        cost = ((a - c) ** 2 + (b - d) ** 2) ** 0.5
        edges.append((i + 1, j + 1, cost))

edges.sort(key = lambda x : x[2])

def find(parent, x):
    if(x != parent[x]):
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if(a < b):
        parent[b] = a
    else:
        parent[a] = b

def kruskal(parent, edges):
    cost = 0
    for edge in edges:
        a, b, c = edge
        if(find(parent, a) != find(parent, b)):
            union(parent, a, b)
            cost += c
    return cost

print(round(kruskal(parent, edges), 2))