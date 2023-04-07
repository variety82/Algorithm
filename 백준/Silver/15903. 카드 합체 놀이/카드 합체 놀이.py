import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
card = list(map(int, input().split()))
heapq.heapify(card)

while(m != 0):
    x = heapq.heappop(card)
    y = heapq.heappop(card)
    heapq.heappush(card, x + y)
    heapq.heappush(card, x + y)
    m -= 1


print(sum(card))