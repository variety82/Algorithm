import sys
input = sys.stdin.readline

deltas = [[1, 0], [0, 1]]

N = int(input())
graph = [list(map(str, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

_min = int(1e9)
_max = -int(1e9)

def is_in(r, c):
    return 0 <= r < N and 0 <= c < N


def dfs(r, c, oper, pre):
    global _min, _max
    if r == N -1 and c == N - 1:
        _min = min(_min, pre)
        _max = max(_max, pre)
        return
    for delta in deltas:
        nr = r + delta[0]
        nc = c + delta[1]
        if not is_in(nr, nc):
            continue
        if visited[nr][nc]:
            continue
        visited[nr][nc] = True
        if (nr % 2 == 0 and nc % 2 == 0) or (nr % 2 == 1 and nc % 2 == 1):
            next_num = int(graph[nr][nc])
            if oper == '+':
                next_num = pre + next_num
            elif oper == '-':
                next_num = pre - next_num
            else:
                next_num = pre * next_num
        else:
            if graph[nr][nc] == '+':
                oper = '+'
            elif graph[nr][nc] == '-':
                oper = '-'
            else:
                oper = '*'
            next_num = pre
        dfs(nr, nc, oper, next_num)
        visited[nr][nc] = False
        
visited[0][0] = True
dfs(0, 0, '+', int(graph[0][0]))
print(f"{_max} {_min}")