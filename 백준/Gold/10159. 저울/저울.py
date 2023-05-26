import sys
input = sys.stdin.readline


INF = int(1e9)
N = int(input())
M = int(input())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1


def floyd():
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


floyd()

for a in range(1, N + 1):
    cnt = 0
    for b in range(1, N + 1):
        if (graph[a][b] != INF or graph[b][a] != INF):
            cnt += 1
    print(N - cnt)
