n = int(input())
e = int(input())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)
cnt = 0
for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(node):
    global cnt
    visited[node] = True
    for adj in range(1, n + 1):
        if graph[node][adj] and not visited[adj]:
            dfs(adj)
            cnt += 1
dfs(1)
print(cnt)