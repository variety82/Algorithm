import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while(q):
        dist, now = heapq.heappop(q)
        if(distance[now] < dist):
            continue
        for b, c in graph[now]:
            cost = dist + c
            if(cost < distance[b]):
                distance[b] = cost
                heapq.heappush(q, (cost, b))


dijkstra(1)
print(distance[N])