import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
gift = [-x for x in list(map(int, input().split()))]
heapq.heapify(gift)

children = list(map(int, input().split()))

flag = True
for i in range(M):
    element = -heapq.heappop(gift)
    if(element >= children[i]):
        heapq.heappush(gift, -(element - children[i]))
        continue
    else:
        flag = False

print(0) if flag == False else print(1)
