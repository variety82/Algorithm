
# coding: utf-8

# In[6]:


"""
2021-08-11
idea : union,find 연산을 활용하여 인풋의 오퍼레이션에 따라 결과값 출력
"""
n,m=map(int,input().split())
com=[]
for _ in range(m):
    com.append(list(map(int,input().split())))
def find_parent(parent,x):
    if(parent[x]!=x):
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
parent=[0]*(n+1)
for i in range(n+1):
    parent[i]=i
for i in range(m):
    if(com[i][0]==0):
        union(parent,com[i][1],com[i][2])
    else:
        if(find_parent(parent,com[i][1])==find_parent(parent,com[i][2])):
            print("Y")
        else:
            print("N")
            
"""
회고 : com리스트에 append를 사용하여 모든 인풋을 보관한 뒤 꺼내어 사용했는데 M값이 커지면 이것 때문에 효율성이 떨어질 수 도 있겠다 생각했다
       23번째 라인에서부터 그냥 oper,a,b=map(int,)와 같이 인풋을 받아서 바로 사용하는 방식이 나을 듯! 
"""

