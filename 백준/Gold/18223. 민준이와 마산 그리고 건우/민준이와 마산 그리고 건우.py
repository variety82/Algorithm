import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E, P = map(int, input().split())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distance = [INF] * (V + 1)
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
    return distance

masan = dijkstra(1)[V]
gunwoo = dijkstra(1)[P] + dijkstra(P)[V]

print("SAVE HIM" if masan >= gunwoo else "GOOD BYE")
