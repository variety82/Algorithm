import sys
input = sys.stdin.readline

V = int(input())
E = int(input())
parent = [x for x in range(V + 1)]
edges = [tuple(map(int, input().split())) for _ in range(E)]

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
    edges.sort(key = lambda x : x[2])
    cost = 0
    for edge in edges:
        a, b, c = edge
        if(find(parent, a) != find(parent, b)):
            union(parent, a, b)
            cost += c
    return cost

print(kruskal(parent, edges))