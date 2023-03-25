import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V = int(input())
graph = [[] for _ in range(V + 1)]
def init():
    for _ in range(V):
        _input = list(map(int, input().split()))
        start = _input[0]
        for i in range(1, len(_input) - 2, 2):
            graph[start].append((_input[i], _input[i + 1]))    


def dijkstra(start):
    q = []
    distance = [INF] * (V + 1)

    heapq.heappush(q, (0, start))
    distance[start] = 0
    while(q):
        dist, now = heapq.heappop(q)
        if(distance[now] < dist):
            continue
        for b, c in graph[now]:
            cost = dist + c
            if(cost < distance[b]):
                distance[b] = cost
                heapq.heappush(q, (cost, b))
    distance[0] = -1
    return distance

init()
distance = dijkstra(1)
tree_start_idx = distance.index(max(distance))
print(max(dijkstra(tree_start_idx)[1:]))