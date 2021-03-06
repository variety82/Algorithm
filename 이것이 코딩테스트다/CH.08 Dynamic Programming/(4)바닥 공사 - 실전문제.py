
# coding: utf-8

# In[11]:


"""
2021-07-28

idea : i번째까지 타일을 기준으로 i-2번째에서는 세로벽돌 두개나 2*2사이즈의 타일 하나가 가능, i-2에선 가로타일 하나가 가능
        이를 점화식으로 표현시 A_n=A_n-1+(A_n-2)*2 
"""

N=int(input())

dp=[0]*1000
dp[0]=1
dp[1]=3
for i in range(2,N):
    dp[i]=(dp[i-2]*2+dp[i-1])%796796
print(dp[N-1])

"""
회고 : 간단히 점화식관점에서 접근하면 되는데 너무 경우의수를 세는 쪽으로 생각했다, DP같은 경우 점화식을 잘 세우는게 중요한듯
"""

