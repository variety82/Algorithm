
# coding: utf-8

# In[7]:


"""
2021-07-14

idea : 모든 행의 최소값을 담은 리스트를 만든 후 그 중 최대값 출력

"""

N,M=map(int,input().split())
data=[]
min_list=[] #각 row에서 최소값을 저장할 리스트 

for i in range(N):
    data.append(list(map(int,input().split())))
   
#row의 최소값들 중 제일 큰 값 출력
for i in range(N):
    min_list.append(min(data[i]))
print(max(min_list))

# 답지 해설은 행 하나 입력받을 때 마다 최소값을 저장하면서 갱신 

