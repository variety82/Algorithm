import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e9)
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
deltas = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

def init(N, M):
    for r in range(N):
        for c in range(M):
            if(graph[r][c] == 1):
                graph[r][c] = -1
            else:
                graph[r][c] = INF

def is_in(r, c):
    return r >= 0 and r < N and c >= 0 and c < M

def bfs(r, c):
    q = deque()
    q.append((r, c))
    while(q):
        r, c = q.popleft()
        for delta in deltas:
            nr = r + delta[0]
            nc = c + delta[1]
            if(not is_in(nr, nc)):
                continue
            if(graph[nr][nc] != -1 and graph[nr][nc] > graph[r][c] + 1):
                if(graph[r][c] == -1):
                    graph[nr][nc] = graph[r][c] + 2
                else:
                    graph[nr][nc] = graph[r][c] + 1
                q.append((nr, nc))

def solution():
    answer = -1
    for r in range(N):
        answer = max(answer, max(graph[r]))
    return answer

init(N, M)
for r in range(N):
    for c in range(M):
        if(graph[r][c] == -1):
            bfs(r, c)

print(solution())