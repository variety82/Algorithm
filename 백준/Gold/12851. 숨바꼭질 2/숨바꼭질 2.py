import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [False] * 100001
q = deque()
q.append(N)
answer = 0
time = 0

while answer == 0:
    new_q = deque()
    size = len(q)
    while size != 0:
        pos = q.popleft()
        size -= 1
        if pos == K:
            answer += 1
            continue
        if pos + 1 <= 100000 and not visited[pos + 1]:
            new_q.append(pos + 1)
        if pos - 1 >= 0 and not visited[pos - 1]:
            new_q.append(pos - 1)
        if pos * 2 <= 100000 and not visited[pos * 2]:
            new_q.append(pos * 2)
        visited[pos] = True
    time += 1
    q = new_q

print(time - 1)
print(answer)
