
# coding: utf-8

# In[4]:


"""
2021-07-28

idea: 왼쪽부터 바텀업방식으로 dp테이블 갱신, 한 칸 건너가서 식량을 털거나 그 전 테이블과 비교해서 큰 걸 선택

"""

N=int(input())
ant_house=list(map(int,input().split()))

dp=[0]*100
dp[0]=ant_house[0]
dp[1]=max(ant_house[0],ant_house[1])

for i in range(2,N):
    dp[i]=max(ant_house[i]+dp[i-2],dp[i-1])
    
print(dp[N-1])


