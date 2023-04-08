import sys
input = sys.stdin.readline

N = int(input())        
INF = int(1e9)
graph = [[INF] * (N + 1) for _ in range(N + 1)]
while(True):
    a, b = map(int, input().split())
    if(a == -1):
        break
    graph[a][b] = 1
    graph[b][a] = 1

for a in range(1, N + 1):
    graph[a][a] = 0

def floyd(graph):
    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

def solution():
    answer = []
    for r in range(1, N + 1):
        answer.append(max(graph[r][1:]))
    _min = min(answer)
    cnt = answer.count(_min)
    print(_min, cnt)
    for i in range(N):
        if(answer[i] == _min):
            print(i + 1, end = " ")

floyd(graph)
solution()

