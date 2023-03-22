import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def dijkstra(start, N):
    q = []
    heapq.heappush(q, (0, start))
    distance = [[INF, 0] for _ in range(N + 1)]
    distance[start] = [0, start]
    while(q):
        dist, now = heapq.heappop(q)
        if(dist > distance[now][0]):
            continue
        for b, c in graph[now]:
            cost = dist + c
            if(cost < distance[b][0]):
                distance[b] = [cost, now]
                heapq.heappush(q, (cost,  b))
    return distance

distance = dijkstra(start, N)

def solution(start, end, distance):
    answer = [end]
    while(True):
        end = distance[end][1]
        answer.append(end)
        if(end == start):
            break
    return answer

distance = dijkstra(start, N)
print(distance[end][0])
answer = solution(start, end, distance)[::-1]
print(len(answer))
print(*answer)