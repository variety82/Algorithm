INF = int(1e9)
N, M = map(int, input().split())

def init(N, M):
    friends = [[INF] * N for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        friends[A - 1][B - 1] = 1
        friends[B - 1][A - 1] = 1
    for i in range(N):
        friends[i][i] = 0
    return friends

def floyd(graph, N):
    for k in range(N):
        for a in range(N):
            for b in range(N):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


def solution(graph, N):
    answer = 0
    _min = 1e9
    for i in range(N):
        if(sum(graph[i]) < _min):
            answer = i + 1
            _min = sum(graph[i])
    return answer

friends = init(N, M)
floyd(friends, N)
print(solution(friends, N))


