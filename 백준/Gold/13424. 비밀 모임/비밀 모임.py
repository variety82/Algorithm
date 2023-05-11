import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
T = int(input())

def dikjstra(start):
    q = []
    distance = [INF] * (N + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while (q):
        dist, now = heapq.heappop(q)
        if (distance[now] < dist):
            continue
        for b, c in graph[now]:
            cost = dist + c
            if (cost < distance[b]):
                distance[b] = cost
                heapq.heappush(q, (cost, b))
    return distance


for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    K = int(input())

    friends = list(map(int, input().split()))
    friends_with_distance = [[] for _ in range(K)]

    for idx, friend in enumerate(friends):
        friends_with_distance[idx] = dikjstra(friend)

    answer = -1
    _max = INF
    for i in range(1, N + 1):
        _sum = 0
        for j in range(K):
            _sum += friends_with_distance[j][i]
        if (_sum < _max):
            _max = _sum
            answer = i

    print(answer)
