
# coding: utf-8

# In[62]:


"""
2021-08-05
idea : 무게기준으로 오름차순 정렬을 한다, set을 이용해 무게정보만 들어있는 리스트를 생성한다. 
       A가 앞의 무게부터 선택하고 B가 고를 수 있는 경우들을 곱해나가면서 카운트한다. 
"""

N,M=map(int,input().split())
ball=list(map(int,input().split()))
ball.sort()
ball_set=list(set(ball))
cnt=0
for i in range(len(ball_set)):
    for j in range(i+1,len(ball_set)):
        cnt+=(ball.count(ball_set[i])*ball.count(ball_set[j]))
        
"""
회고, 해설과 비교 : 해설도 큰 아이디어 측면에서는 비슷하다 다만 나는 for를 두번 돌려 시간 복잡도가 늘어난다 아래는 해설 소스코드

"""


'''

n,m=map(int,input().split())
data=list(map(int,input().split()))
arr=[0]*11
for x in data:
    arr+=1

result=0
for i in range(1,m+1):
    n-=arr[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result+=arr[i]*n #B가 선택하는 경우의 수 곱하기

'''

