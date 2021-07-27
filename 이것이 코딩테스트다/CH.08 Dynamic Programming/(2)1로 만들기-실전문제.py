
# coding: utf-8

# In[9]:


"""
2021-07-27

idea : a_i=min(a_i-1,a_i/2,a_i/3,a_i/5)+1 의 점화식으로 DP테이블 채워나가기

"""

x=int(input())

d=[0]*27

for i in range(2,x+1):
    d[i]=d[i-1]+1
    if (i%2==0):
        d[i]=min(d[i],d[i//2]+1)
    if(i%3==0):
        d[i]=min(d[i],d[i//3]+1)
    if(i%5==0):
        d[i]=min(d[i],d[i//5]+1)
        
print(d)

"""
회고 : 무지성으로 ifififif,elif 구현으로 해결하였음..dp를 좀 더 이해해보기 
"""


# In[ ]:




