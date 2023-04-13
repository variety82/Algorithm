import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
start, end = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
m = int(input())

for n in range(1, n + 1):
    graph[n][n] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def floyd():
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

floyd()
print(-1 if graph[start][end] == INF else graph[start][end])
