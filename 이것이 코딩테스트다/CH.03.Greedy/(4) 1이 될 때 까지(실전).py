
# coding: utf-8

# In[11]:


"""
2021-07-14

idea : 그냥 조건따라 그대로..

"""

N,K=map(int,input().split())
cnt=0
while N!=1:
    if(N%K==0):
        N=int(N/K)
    else:
        N-=1
    cnt+=1

print(cnt)


