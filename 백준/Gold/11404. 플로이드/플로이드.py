INF = 1e9
n = int(input())
m = int(input())

def init(n, m):
    graph = [[INF] * n for _ in range(n)]
    for r in range(n):
            graph[r][r] = 0

    for _ in range(m):
        a, b, c = map(int ,input().split())
        graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)

    return graph

def floyd(n, graph):
    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    return graph

graph = init(n, m)
graph = floyd(n, graph)

for r in range(n):
     for c in range(n):
          if(graph[r][c] == INF):
               graph[r][c] = 0

for i in range(n):
    print(*graph[i])