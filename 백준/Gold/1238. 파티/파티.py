import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start, N):
    q = []
    distance = [INF] * (N + 1)
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
    return distance

distance = dijkstra(X, N)
distance[0] = 0
for i in range(1, N + 1):
    distance[i] += dijkstra(i, N)[X]
print(max(distance))