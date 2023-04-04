import sys
from collections import deque
input = sys.stdin.readline

deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]
R, C, N = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]

def init():
    for r in range(R):
        for c in range(C):
            if(graph[r][c] == 'O'):
                graph[r][c] = 3
            elif(graph[r][c] == '.'):
                graph[r][c] = -1

def is_in(r, c):
    return r >= 0 and r < R and c >= 0 and c < C

def insert_bomb(R, C):
    for r in range(R):
        for c in range(C):
            if(graph[r][c] == -1):
                graph[r][c] = 3

def bomb(graph):
    q = deque()
    for r in range(R):
        for c in range(C):
            if(graph[r][c] == 0):
                q.append([r, c])
    while(q):
        r, c = q.popleft()
        graph[r][c] = -1
        for delta in deltas:
            nr = r + delta[0]
            nc = c + delta[1]
            if(not is_in(nr, nc)):
                continue
            else:
                graph[nr][nc] = -1

def deal_time():
    for r in range(R):
        for c in range(C):
            if(graph[r][c] != -1):
                graph[r][c] -= 1

def game(N):
    time = 0
    while(N != time):
        time += 1
        deal_time()
        if(time == 1):
            continue
        if(time % 2 == 0):
            insert_bomb(R, C)
        bomb(graph)

    for r in range(R):
        for c in range(C):
            if(graph[r][c] == -1):
                graph[r][c] = '.'
            else:
                graph[r][c] = 'O'
init()
game(N)

for r in range(R):
    print("".join(graph[r]))