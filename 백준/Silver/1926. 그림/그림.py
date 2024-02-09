import sys
from pprint import pprint
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visitied = [[False] * m for _ in range(n)]
answer = 0
area = 0

def is_in(r, c):
    return 0 <= r < n and 0 <= c < m

def bfs(graph, r, c):
    q = deque()
    q.append((r, c))
    visitied[r][c] = True
    cnt = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + deltas[i][0]
            nc = c + deltas[i][1]
            if not is_in(nr, nc):
                continue
            if graph[nr][nc] == 0:
                continue
            if visitied[nr][nc]:
                continue
            visitied[nr][nc] = True
            cnt += 1
            q.append((nr, nc))
    return cnt

for r in range(n):
    for c in range(m):
        if graph[r][c] == 0:
            continue
        if visitied[r][c]:
            continue
        else:
            area = max(area, bfs(graph, r, c))
            answer += 1
print(answer)
print(area)

