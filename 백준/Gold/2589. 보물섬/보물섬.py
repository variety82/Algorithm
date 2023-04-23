import sys
from collections import deque
input = sys.stdin.readline

deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

def is_in(r, c):
    return r >= 0 and r < N and c >= 0 and c < M and graph[r][c] == 'L'

def bfs(r, c):
    visited = [[False] * M for _ in range(N)]
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    cnt = 0
    while(q):
        size = len(q)
        while(size != 0):
            r, c = q.popleft()
            for delta in deltas:
                nr = r + delta[0]
                nc = c + delta[1]
                if(not is_in(nr, nc)):
                    continue
                if(visited[nr][nc]):
                    continue
                q.append((nr, nc))
                visited[nr][nc] = True
            size -= 1
        cnt += 1
    return cnt 

_max = 0

for r in range(N):
    for c in range(M):
        if(graph[r][c] == 'L'):
            root_length = bfs(r, c)
            _max = max(_max, root_length)

print(_max - 1)