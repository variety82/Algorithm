from collections import deque
N, K = map(int, input().split())

def make_Josephus(N):
    seq = list(range(1, N + 1))
    arr = []
    cnt = 0
    q = deque(seq)
    while(q):
        temp = q.popleft()
        cnt += 1
        if(cnt == K):
            arr.append(temp)
            cnt = 0
        else:
            q.append(temp)
    return arr

seq = make_Josephus(N)
answer = "<"

for idx, value in enumerate(seq):
    if(idx != len(seq) - 1):
        answer += str(value) + ", "
    else:
        answer += str(value) + ">"
        
print(answer)