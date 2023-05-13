import sys
import heapq
input = sys.stdin.readline

INF = int(1e11)
N, M = map(int, input().split())
graph = [[] for _ in range(N)]
distance = [INF] * N
eyesight = list(map(int, input().split()))
eyesight[-1] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    if (eyesight[a] == 1 or eyesight[b] == 1):
        continue
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
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


answer = dijkstra(0)[-1]

print(answer if answer != INF else -1)
