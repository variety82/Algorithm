import heapq
def solution(k, score):
    answer = []
    q = []
    for idx, s in enumerate(score):
        if idx < k:
            heapq.heappush(q, s)
            temp = heapq.heappop(q)
            answer.append(temp)
            heapq.heappush(q, temp)
        else:
            heapq.heappush(q, s)
            heapq.heappop(q)
            temp = heapq.heappop(q)
            answer.append(temp)
            heapq.heappush(q, temp)
    return answer