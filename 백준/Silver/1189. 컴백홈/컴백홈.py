import sys

input = sys.stdin.readline
R, C, K = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(R)]
deltas = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def init(graph):
    visited = [[False] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if(graph[r][c] == 'T'):
                visited[r][c] = True
    return visited

def is_in(r, c):
    return r >= 0 and r < R and c >= 0 and c < C


def dfs(r, c, cnt):
    global answer
    if(cnt > K):
        return
    if(r == 0 and c == C - 1 and K == cnt):
        answer += 1
        return
    
    for delta in deltas:
        nr = r + delta[0]
        nc = c + delta[1]
        if(not is_in(nr, nc)):
            continue
        if(visited[nr][nc]):
            continue
        visited[nr][nc] = True
        dfs(nr, nc, cnt + 1)
        visited[nr][nc] = False

visited = init(graph)
answer = 0
visited[R-1][0] = True
dfs(R - 1, 0, 1)
print(answer)