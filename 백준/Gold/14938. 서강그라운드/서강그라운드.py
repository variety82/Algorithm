INF = int(1e9)
n, m , r = map(int, input().split())
item = list(map(int, input().split()))

def init(n, r):
    graph = [[INF] * n for _ in range(n)]
    for i in range(n):
            graph[i][i] = 0
    for _ in range(r):
        a, b, c = map(int ,input().split())
        graph[a - 1][b - 1] = c
        graph[b - 1][a - 1] = c

    return graph

def floyd(n, graph):
    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
    return graph

graph = init(n, r)
graph = floyd(n, graph)

max_item = 0
for r in range(n):
     temp = 0
     for c in range(n):
          if(graph[r][c] <= m and graph[r][c] != INF):
               temp += item[c]
     max_item = max(max_item, temp)

print(max_item)