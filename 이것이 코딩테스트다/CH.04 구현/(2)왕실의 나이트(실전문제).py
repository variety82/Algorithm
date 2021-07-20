
# coding: utf-8

# In[30]:


"""
2021-07-20
구현 실전문제 2- 왕실의 나이트 

idea: 총 8개의 방향으로 이동이 가능하다, 8개의 방향모두 이동시킨 후 좌표평면을 벗어난다면 카운트 하지 않는 방식으로 구현하였다.
        눈에 보이는 방식으로 쉽게 연산을 하기 위해 ndarray를 사용하였다. 
        실제 문제는 col은 영문으로 받지만 숫자쌍으로 입력받게 문제를 조금 변형하였다. 
        영문으로 받으려면 col=int(ord(intput_data[0]))-int(ord('a'))+1을 사용한다. 

"""
import numpy as np
pos=np.array(list(map(int,input().split())))
move_type=np.array([[-2,-1],[-2,1],[2,-1],[2,1],[-1,2],[1,2],[-1,-2],[-1,2]])
cnt=0
for move in move_type:
    nx,ny=pos+move
    if(nx<1 or ny<1 or nx>8 or ny>8):
        continue
    else:
        cnt+=1
print(cnt)

"""
답안과의 비교 : 답안은 8가지 방향을 튜플로 받고 row,col을 따로따로 계산하였으나 나는 그냥 ndarray를 사용하였다.
"""

