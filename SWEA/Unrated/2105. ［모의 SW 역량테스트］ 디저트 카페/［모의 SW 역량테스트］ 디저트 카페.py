import copy

deltas = [[1, 1], [1, -1], [-1, -1], [-1, 1]]  # 오른쪽으로 네모

def is_in(r, c):
    return 0 <= r < N and 0 <= c < N

def dfs(r, c, dir, start, cnt):
    global eat_cnt
    nr = r + deltas[dir][0]
    nc = c + deltas[dir][1]
    if ([nr, nc] == start):
        eat_cnt = max(eat_cnt, cnt)
        return
    if (not is_in(nr, nc)):
        return
    if (visited[desert[nr][nc]]):
        return
    visited[desert[nr][nc]] = True
    dfs(nr, nc, dir, start, cnt + 1)
    if(dir < 3):
        dfs(nr, nc, dir + 1, start, cnt + 1)
    visited[desert[nr][nc]] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    desert = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * 101
    eat_cnt = 0
    for r in range(N - 1):
        for c in range(1, N - 1):
            visited[desert[r][c]] = True
            dfs(r, c, 0, [r, c], 1)
            visited[desert[r][c]] = False
    if(eat_cnt == 0):
        eat_cnt = -1
    print(f"#{tc} {eat_cnt}")
