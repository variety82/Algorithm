import sys
import heapq

input = sys.stdin.readline
N = int(input())
max_heap = []
for _ in range(N):
    element = int(input())
    if(element == 0):
        if(len(max_heap) == 0):
            print(0)
        else:
            print(-heapq.heappop(max_heap))
    else:
        heapq.heappush(max_heap, -element)