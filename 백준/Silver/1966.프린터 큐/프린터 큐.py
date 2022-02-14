from collections import deque

n = int(input())

for _ in range(n):
    __, pos = map(int, input().split())
    tmp = list(map(int, input().split()))
    q = deque()
    cnt = 0
    # 값이 같은 숫자를 처리하기위해 각자 고유 index부여
    for idx, v in enumerate(tmp):
        q.append([idx, v])
        
    while q:
        if max(q, key = lambda x: x[1])[1] == q[0][1]: # 제일 왼쪽에 있는게 가장 크면 빼기
            if q[0][0] == pos:  #내가 원하는 번호 index면 종료
                print(cnt + 1)
                break
            q.popleft()
            cnt += 1
            
        else:
            tmp1 = q.popleft()
            q.append(tmp1)