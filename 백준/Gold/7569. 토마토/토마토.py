import sys
from collections import deque

input = sys.stdin.readline

deltas = [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [-1, 0, 0], [1, 0, 0]]

M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

def is_in(h, r, c):
    return r >= 0 and r < N and c >= 0 and c < M and h >= 0 and h < H and graph[h][r][c] != -1

def init():
    q = deque()
    non_tomato_size = 0
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if(graph[h][r][c] == 1):
                    q.append((h, r, c))
                elif(graph[h][r][c] == 0):
                    non_tomato_size += 1
    return q, non_tomato_size

def solution(graph):
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if(graph[h][r][c] == 0):
                    return False
    return True

def bfs(q):
    global cnt
    while(q):
        size = len(q)
        while(size != 0):
            h, r, c = q.popleft()
            for delta in deltas:
                nh = h + delta[0]
                nr = r + delta[1]
                nc = c + delta[2]
                if(not is_in(nh, nr, nc)):
                    continue
                if(graph[nh][nr][nc] == 0):
                    graph[nh][nr][nc] = 1
                    q.append((nh, nr, nc))
            size -= 1
        cnt += 1

cnt = 0
q, size = init()
# bfs(q)
# pprint(graph)
if(size == 0):
    print(0)
else:
    bfs(q)
    if(not solution(graph)):
        print(-1)
    else:
        print(cnt - 1)
