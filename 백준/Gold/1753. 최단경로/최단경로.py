import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
start = int(input())

graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while(q):
        dist, now = heapq.heappop(q)
        if(distance[now] < dist):
            continue
        for v, w in graph[now]:
            cost = dist + w
            if(cost < distance[v]):
                distance[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(start)

for i in range(1, V + 1):
    if(distance[i] == INF):
        print("INF")
    else:
        print(distance[i])
