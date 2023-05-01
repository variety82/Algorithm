import sys
input = sys.stdin.readline

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

while(True):
    N, M = map(int, input().split())
    if(N == 0 and M == 0):
        break
    parent = [x for x in range(N + 1)]
    edges = []
    total = 0
    for _ in range(M):
        a, b, c = map(int, input().split())
        total += c
        edges.append((a, b, c))
    edges.sort(key = lambda x : x[2])
    cost = kruskal(parent, edges)
    print(total - cost)


