
# coding: utf-8

# In[6]:


"""
2021-07-22

idea: 주어지는 수의 범위가 작아 따로 정렬을 구현하기보다 기본 정렬 라이브러리를 이용해 내림차순으로 정렬 
"""

N=int(input())
seq=list()
for _ in range(N):
    seq.append(int(input()))
    
seq=sorted(seq,reverse=True)
for i in range(N):
    print(seq[i],end=' ')

