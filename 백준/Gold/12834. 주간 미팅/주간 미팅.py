import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
N, V, E = map(int, input().split())
A, B = map(int, input().split())
homes = list(map(int, input().split()))

def init(E):
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b, l = map(int, input().split())
        graph[a].append((b, l))
        graph[b].append((a, l))
    return graph

def dijkstra(start):
    distance = [INF] * (V + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while(q):
        dist, now = heapq.heappop(q)
        if(distance[now] < dist):
            continue
        for b, l in graph[now]:
            cost = dist + l
            if(cost < distance[b]):
                distance[b] = cost
                heapq.heappush(q, (cost, b))
    return distance

def solution(homes):
    dist = 0
    for home in homes:
        distance = dijkstra(home)
        dist_to_kist = distance[A] if distance[A] != INF else -1
        dist_to_food = distance[B] if distance[B] != INF else -1
        dist += (dist_to_kist + dist_to_food)
    return dist

graph = init(E)
print(solution(homes))