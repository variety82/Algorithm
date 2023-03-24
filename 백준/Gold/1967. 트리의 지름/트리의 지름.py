import sys
import heapq

input = sys.stdin.readline
n = int(input())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstar(start):
    distance = [INF] * (n + 1)
    distance[start] = 0
    q = []
    q.append((0, start))
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

distance = dijkstar(1)
idx = distance.index(max(distance[1:]))
print(max(dijkstar(idx)[1:]))