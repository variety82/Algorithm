import sys
from collections import deque
input = sys.stdin.readline

deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

N = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(N)]


def is_in(r, c):
    return 0 <= r < N and 0 <= c < N

def bfs(r, c):
    cnt = 1
    visited[r][c] = True
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for delta in deltas:
            nr = r + delta[0]
            nc = c + delta[1]
            if not is_in(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            if graph[nr][nc] == 0:
                continue
            visited[nr][nc] = True
            cnt += 1
            q.append((nr, nc))
    return cnt

visited = [[False] * N for _ in range(N)]
answer = []
for r in range(N):
    for c in range(N):
        if graph[r][c] == 1 and not visited[r][c]:
            answer.append(bfs(r, c))

answer.sort()
print(len(answer))
for cnt in answer:
    print(cnt)


