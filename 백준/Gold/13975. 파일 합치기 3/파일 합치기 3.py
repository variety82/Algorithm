import sys
import heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    chapters = list(map(int, input().split()))
    heapq.heapify(chapters)

    answer = 0
    while(len(chapters) != 1):
        chapter1 = heapq.heappop(chapters)
        chapter2 = heapq.heappop(chapters)
        chapter3 = chapter1 + chapter2
        answer += chapter3
        heapq.heappush(chapters, chapter3)
    print(answer)
