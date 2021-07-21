
# coding: utf-8

# In[11]:


"""
2021-07-21

idea: 그래프 전체를 완전탐색으로 DFS 실행, 0인부분을 DFS로 쭉 순회하면서 카운트를 늘려준다

"""

N,M=map(int,input().split())
ice_map=list()
for _ in range(N):
    ice_map.append(list(map(int,input())))
    
def bfs(x,y,graph):
    if(x<0 or y<0 or x>=N or y>=M):
        return False
    if(graph[x][y]==0):
        graph[x][y]=1
        bfs(x-1,y,graph)
        bfs(x,y-1,graph)
        bfs(x+1,y,graph)
        bfs(x,y+1,graph)
        return True #처음 0으로 시작한 부분만 카운트해주고 탐색해나가기 
    return False #나머지 부딫치는 부분은 카운트 x 

cnt=0
for i in range(N):
    for j in range(M):
        if(bfs(i,j,ice_map)==True):
            cnt+=1

print(cnt)

"""
회고 : 굳이 DFS로 이름을 붙인 이유를 아직 모르겠다.. 그냥 완전탐색과 재귀로 탐색하는 것 같은데 조금 더 생각해봐야할듯 
"""

