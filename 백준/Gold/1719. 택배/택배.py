import sys
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
answer = [['-'] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c
    graph[b][a] = c

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if(a != b and graph[a][b] != INF):
            answer[a][b] = b

def floyd():
    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if(graph[a][b] > graph[a][k] + graph[k][b]):
                    graph[a][b] = graph[a][k] + graph[k][b]
                    answer[a][b] = answer[a][k]


floyd()
for i in range(1, n + 1):
    print(*answer[i][1:])