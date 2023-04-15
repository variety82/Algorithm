import sys
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
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

def solution():
    answer = 0
    for r in range(1, N + 1):
        flag = True
        for c in range(1, N + 1):
            if(graph[r][c] == INF and graph[c][r] == INF):
                flag = False
                break
        if(flag == True):
            answer += 1
    return answer

floyd()
answer = solution()
print(answer)