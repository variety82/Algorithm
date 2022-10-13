from collections import deque


deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
pipe = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]


def count_ans(arr):
    cnt = 0
    for r in range(N):
        cnt += arr[r].count(True)
    return cnt


def is_in(r, c):
    return 0 <= r < N and 0 <= c < M


def bfs(r, c):
    global L
    q = deque()
    q.append([r, c, arr[r][c]])
    visited[R][C] = True
    while(q):
        size = len(q)
        if L == 1:
            break
        while(size != 0):
            pos = q.popleft()
            r = pos[0]
            c = pos[1]
            status = pos[2]
            for d in pipe[status]:
                nr = r + deltas[d][0]
                nc = c + deltas[d][1]
                if(is_in(nr, nc) and not visited[nr][nc]):
                    if(d == 0 or d == 1):
                        if((1-d) not in pipe[arr[nr][nc]]):
                            continue
                    elif(d == 2 or d == 3):
                        if ((5 - d) not in pipe[arr[nr][nc]]):
                            continue
                    q.append([nr, nc, arr[nr][nc]])
                    visited[nr][nc] = True
            size -= 1
        L -= 1


T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    bfs(R, C)
    print(f"#{tc} {count_ans(visited)}")