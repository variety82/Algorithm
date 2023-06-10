import sys
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

K = int(input())
cities = list(map(int, input().split()))

def floyd():
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][k] + graph[k][b], graph[a][b])

floyd()
answer = []

_min = INF
for i in range(1, N + 1):
    _max = 0
    for city in cities:
        if(city == i):
            continue
        dist = graph[city][i] + graph[i][city]
        _max = max(_max, dist)
    if(_min > _max):
        answer = []
        answer.append(i)
        _min = _max
    elif(_min == _max):
        answer.append(i)

answer.sort()
print(*answer)