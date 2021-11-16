'''
2021-11-16
idea :  
       달팽이는 처음엔 n번 한방향으로 가고 그다음은 n-1번 다른 방향으로 간다.
       달팽이가 가는 방향은 3가지이다, 이를 이용해 3으로 나눈 나머지대로 아래, 오른쪽, 대각선으로
       갈 방향을 정한뒤 움직이는 횟수만큼 이동시킨다.
       
'''
def solution(n):
    answer = []
    dal = [[0]*n for _ in range(n)]
    r, c = -1, 0
    cnt = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                dal[r+1][c] = cnt
                r += 1
            elif i % 3 == 1:
                dal[r][c+1] = cnt
                c += 1
            else:
                dal[r-1][c-1] = cnt
                r -= 1
                c -= 1
            cnt += 1
    for i in range(n):
        for j in range(n):
            if dal[i][j] != 0 :
                answer.append(dal[i][j])
    return answer

'''
회고 : 처음에 n=4 일때에 맞춰 나머지가 1이면 아래 2면 오른쪽 이렇게 했다가 일반화가 되지 않는다는걸
      알았다, 항상 일반화된 방법을 생각하자 ! 
'''