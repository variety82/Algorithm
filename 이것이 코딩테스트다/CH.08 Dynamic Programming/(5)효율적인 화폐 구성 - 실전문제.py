
# coding: utf-8

# In[41]:


"""
2021-07-29

idea : 화폐를 내림차순으로 정렬한 한 후 dp테이블의 처음인덱스에는 목표금액인 M을 넣고, 그 뒤로 dp테이블에 화폐를 빼서 영보다 크다면 
       뺄 수 있는만큼 빼주고 dp테이블을 갱신해나간다.
"""

N,M=map(int,input().split())
money=list()
for i in range(N):
    money.append(int(input()))
money.sort(reverse=True)
dp=[0]*(N+1)
dp[0]=M
cnt=0
for i in range(1,N+1):
    if(dp[i-1]-money[i-1]>=0):
        dp[i]=dp[i-1]%money[i-1]
        cnt+=dp[i-1]//money[i-1]
    else:
        dp[i]=dp[i-1]
if(dp[N]>0):
    print(-1)
else:
    print(cnt)
    
"""
회고 : 문제해설의 정답과는 아예 달라서 사실 이 풀이가 DP로 작성한 풀이인지 잘 모르겠다, 좀 더 공부하고 다시 체크해봐야할듯

"""
#문제해설 -> 책 참고

