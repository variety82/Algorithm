import sys
import heapq
input = sys.stdin.readline

T = int(input())
modulo = 1000000007

def solution(slime):
    heapq.heapify(slime)
    cost = 1
    while(len(slime) != 1):
        first = heapq.heappop(slime)
        second = heapq.heappop(slime)
        multiple = first * second
        cost = (cost * multiple) % modulo
        heapq.heappush(slime, multiple)
    return cost % modulo

for _ in range(T):
    N = int(input())
    slime = list(map(int, input().split()))
    print(1 if(len(slime) == 1) else solution(slime))
