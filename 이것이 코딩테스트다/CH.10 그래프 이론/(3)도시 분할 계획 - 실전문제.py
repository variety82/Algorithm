
# coding: utf-8

# In[15]:


"""
2021-08-11
idea : 최소신장트리를 구성한뒤 가장 코스트가 높은 엣지 하나를 잘라 두개의 최소신장트리로 만든다.
"""def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
v,e=map(int,input().split())
parent=[0]*(v+1) 
edges=[]
result=0
for i in range(1,v+1):
    parent[i]=i

for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))
edges.sort()
max_cost=0
for edge in edges:
    cost,a,b=edge
    if(find_parent(parent,a)!=find_parent(parent,b)):
        union_parent(parent,a,b)
        result+=cost
        max_cost=cost
print(result-max_cost)

"""
회고 : 처음엔 그냥 엣지중 코스트가 가장 큰걸 결과값에서 빼버렸는데 최소신장트리 구성한 엣지중에 가장 큰 걸 빼야한다! 
       어떤것을 구성하기 위한 조건 잘 생각하기 
"""

