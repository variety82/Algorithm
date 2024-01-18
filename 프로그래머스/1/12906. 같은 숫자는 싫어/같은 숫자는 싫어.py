from collections import deque
def solution(arr):
    answer = []
    q = deque(arr)
    e = q.popleft()
    answer.append(e)
    while q:
        temp = q.popleft()
        if e == temp:
            continue
        else:
            e = temp
            answer.append(e)
    return answer