from collections import deque

N, M = map(int, input().split())
block = [list(map(int, input())) for _ in range(N)]
dist = [[[-1, -1] for _ in range(M)] for _ in range(N)]
dist[0][0][0] = 1

deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def is_in(r, c):
    return r >= 0 and r < N and c >= 0 and c < M

def bfs(r, c, k):
    q = deque()
    q.append([r, c, k])
    while(q):
        pos = q.popleft()
        r = pos[0]
        c = pos[1]
        k = pos[2]
        for d in range(4):
            nr = r + deltas[d][0]
            nc = c + deltas[d][1]
            if(not is_in(nr, nc)):
                continue
            if(block[nr][nc] == 0 and dist[nr][nc][k] == -1):
                dist[nr][nc][k] = dist[r][c][k] + 1
                q.append((nr, nc, k))
            elif(block[nr][nc] == 1 and dist[nr][nc][1] == -1):
                if(dist[r][c][0] != -1):
                    dist[nr][nc][1] = dist[r][c][0] + 1
                    q.append((nr, nc, 1))

    if(dist[-1][-1][0] == -1):
        dist[-1][-1][0] = 10000000
    if(dist[-1][-1][1] == -1):
        dist[-1][-1][1] = 10000000
    answer = min(dist[-1][-1][0], dist[-1][-1][1])
    if(answer == 10000000):
        answer = -1
    print(answer)

bfs(0, 0, 0)