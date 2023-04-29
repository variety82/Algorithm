import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [x for x in range(0, N + 1)]
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

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
    _max = 0
    for edge in edges:
        a, b, c = edge
        if(find(parent, a) != find(parent, b)):
            union(parent, a, b)
            cost += c
            _max = c
    return cost - _max

print(kruskal(parent, edges))