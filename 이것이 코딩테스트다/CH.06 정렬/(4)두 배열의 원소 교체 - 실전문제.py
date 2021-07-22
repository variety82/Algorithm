
# coding: utf-8

# In[19]:


"""
2021-07-22

idea: A는 오름차순, B는 내림차순으로 기본 라이브러리 정렬을 이용해 정렬 후 조건에 맞게 swap 
"""

N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))

A=sorted(A)
B=sorted(B,reverse=True)
for i in range(K):
    if(A[i]<B[i]):
        A[i],B[i]=B[i],A[i]
    else:
        continue
print(sum(A))

"""
회고 : 배열의 원소가 100,000이므로 O(NlogN)이 보장되는 정렬을 사용해야한다. 
"""

