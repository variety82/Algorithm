
# coding: utf-8

# In[137]:


"""
2021-08-05
idea : food의 길이만큼씩 k를 감소시키며 food_times를 최대한 줄인다, k가 0이 될 때 까지 food를 찾아 줄이기 시작한다
       k가 0이되면 k가 0이 된 인덱스에서 1씩 늘려가며 그 다음 먹을 음식의 순서를 찾는다. 
       
"""

import numpy as np
def solution(food_times,k):
    if(sum(food_times)<k):
        return -1
    food_times=np.array(food_times)
    while(food_times.min()!=0):
        food_times-=1
        k-=len(food_times)
    food_times=list(food_times)
    while(k!=0):
        for i in range(len(food_times)):
            if(k==0):
                break
            if(food_times[i]!=0):
                food_times[i]-=1
                k-=1
            else:
                continue
            check=i
    temp=-1
    while temp!=0:
        check+=1
        if(check>=len(food_times)):
            check=check%len(food_times)
        if(food_times[check]!=0):
            return check+1
        
        
"""
회고 : 리스트 원소 연산 np로하면 max같은 함수의 사용법이 바뀜에 주의, 

       프로그래머스에서 돌릴 때 는 정확도 체크 25/32 효율성 0/8이 나왔다, 정확도체크에서 실패도 시간초과로 실패하였다..
       무지성으로 차례대로 구현하다보니 효율성이 떨어졌다, 아직까지는 어떻게 문제를 풀어나갈지 잘 생각나지 않아 문제를 많이 풀어봐야 할 것 같다 
"""

