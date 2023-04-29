import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [x for x in range(N + 1)]
edges = [((map(int, input().split()))) for _ in range(M)]

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
    for idx, edge in enumerate(edges):
        a, b = edge
        if(find(parent, a) != find(parent, b)):
            union(parent, a, b)
        else:
            print(idx + 1)
            return
    print(0)

kruskal(parent, edges)