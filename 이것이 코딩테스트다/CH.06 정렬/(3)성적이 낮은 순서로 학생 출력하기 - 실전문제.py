
# coding: utf-8

# In[17]:


"""
2021-07-22

idea: sorted의 key를 점수를 기준으로 해서 기본 라이브러리 정렬을 사용 
"""

N=int(input())
seq=list()
for _ in range(N):
    seq.append(list(input().split()))
for i in range(N):
    seq[i][1]=int(seq[i][1])

seq=sorted(seq, key=lambda x:x[1])

for i in range(N):
    print(seq[i][0],end=' ')
    
"""
회고 : 인풋을 받을 때 점수를 int처리하느라 for문을 두번 사용했다. 그러나 for문 한 번에 인풋데이터를 받은 후 따로 처리하면 더 간결하다
       input_data=input().split() 
       array.append((input_data[0],int(input_data[1])))  이렇게 ! 
"""

