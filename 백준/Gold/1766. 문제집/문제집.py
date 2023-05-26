import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = []
    for i in range(1, N + 1):
        if (indegree[i] == 0):
            heapq.heappush(q, i)

    while (q):
        now = heapq.heappop(q)
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            if (indegree[i] == 0):
                heapq.heappush(q, i)

    return result


answer = topology_sort()

print(*answer)
