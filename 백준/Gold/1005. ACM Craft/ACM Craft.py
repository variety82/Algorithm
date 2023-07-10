import sys
import heapq
input = sys.stdin.readline

T = int(input())


def topology_sort(indegree, times):
    q = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
            dp[i] = times[i]

    while q:
        now = heapq.heappop(q)
        for i in graph[now]:
            indegree[i] -= 1
            dp[i] = max(dp[now] + times[i], dp[i])
            if indegree[i] == 0:
                q.append(i)


for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    dp = [0] * (N + 1)
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    W = int(input())
    topology_sort(indegree, times)
    print(dp[W])