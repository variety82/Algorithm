import sys
input = sys.stdin.readline

N = int(input())

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


parent = [x for x in range(N + 1)]
edges = []
x, y, z = [], [], []

for i in range(1, N + 1):
    a, b, c, = map(int, input().split())
    x.append((a, i))
    y.append((b, i))
    z.append((c, i))

x.sort()
y.sort()
z.sort()

for i in range(N - 1):
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

edges.sort()

def kruskal(parent, edges):
    cost = 0
    for edge in edges:
        c, a, b = edge
        if(find(parent, a) != find(parent, b)):
            union(parent, a, b)
            cost += c
    return cost

print(kruskal(parent, edges))