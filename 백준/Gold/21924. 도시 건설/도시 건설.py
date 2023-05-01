import sys
input = sys.stdin.readline


N, M = map(int, input().split())
parent = [x for x in range(N + 1)]
edges = []
cost, E, total = 0, 0, 0
for _ in range(M):
    a, b, c = map(int, input().split())
    total += c
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
    global E
    global cost
    for edge in edges:
        a, b, c = edge
        if(find(parent, a) != find(parent, b)):
            union(parent, a, b)
            cost += c
            E += 1
            
kruskal(parent, edges)

if(E != N - 1):
    print(-1)
else:
    print(total - cost)
