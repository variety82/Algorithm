def dfs(node, computers, visited):
    visited[node] = True
    for adj in range(n):
        if computers[node][adj] and not visited[adj]:
            dfs(adj, computers, visited)


def solution(n, computers):
    visited = [False] * n
    cnt = 0
    
    def dfs(node):
        visited[node] = True
        for adj in range(n):
            if computers[node][adj] and not visited[adj]:
                dfs(adj)
    
    
    for node in range(n):
        if not visited[node]:
            dfs(node)
            cnt += 1
    return cnt