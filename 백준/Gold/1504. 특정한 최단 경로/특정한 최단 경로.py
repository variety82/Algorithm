import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
N, E = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start, end, N):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (N + 1)
    distance[start] = 0
    while(q):
        dist , now = heapq.heappop(q)
        if(dist < distance[now]):
            continue
        for b, c in graph[now]:
            cost = dist + c
            if(cost < distance[b]):
                distance[b] = cost
                heapq.heappush(q, (cost,  b))
    return distance[end]

case1 = dijkstra(1, v1, N) + dijkstra(v1, v2, N) + dijkstra(v2, N, N)
case3 = dijkstra(1, v2, N) + dijkstra(v2, v1, N) + dijkstra(v1, N, N)
answer = min(case1, case3)

print(-1 if answer >= INF else answer)
