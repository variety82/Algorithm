import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

for r in range(n):
    for c in range(n):
        if(graph[r][c] == 0):
            graph[r][c] = INF

def floyd():
    for k in range(n):
        for a in range(n):
            for b in range(n):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


floyd()
for r in range(n):
    for c in range(n):
        if(graph[r][c] == INF):
            graph[r][c] = 0
        else:
            graph[r][c] = 1

for r in range(n):
    print(*graph[r])
