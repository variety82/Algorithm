import sys
import heapq
input = sys.stdin.readline

T = int(input())
INF = int(1e9)

def init(d, graph):
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))
    return graph

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while(q):
        dist, now = heapq.heappop(q)
        if(distance[now] < dist):
            continue
        for b, s in graph[now]:
            cost = dist + s
            if(cost < distance[b]):
                distance[b] = cost
                heapq.heappush(q, (cost, b))
    return distance

def solution(distance):
    cnt = 0
    for i in range(len(distance)):
        if(distance[i] == INF):
            distance[i] = -1
            cnt += 1
    return len(distance) - cnt


for tc in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    graph = init(d, graph)
    distance = dijkstra(c)
    print(solution(distance), max(distance))