
# coding: utf-8

# In[26]:


"""
2021-07-21

idea : 괴물이 없는 1을 따라서 bfs로 쭉 탐색하면서 탐색한 길을 한 칸 갈 때 마다 1씩 증가시킴
"""

from collections import deque

N,M=map(int,input().split())
monster_map=list()
for _ in range(N):
    monster_map.append(list(map(int,input())))
                            
                            
def bfs(x,y,graph):
    dx=[0,0,-1,1]
    dy=[-1,1,0,0]
    
    q=deque([(x,y)]) 
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if(nx<0 or ny<0 or nx>=N or ny>=M):
                            continue
            if graph[nx][ny]==0:
                            continue
            if(graph[nx][ny]==1):
                            graph[nx][ny]=graph[x][y]+1
                            q.append((nx,ny))
    return graph[N-1][M-1]
                                     
print(bfs(0,0,monster_map))

"""
회고 : 이론상으로만 알았던 bfs,dfs를 직접 문제에 구현하려니 아직 익숙하지도 않고 잘 모르겠다 흙흙..다음회차에는 조금 더 나아지길

       queue에 (x,y)와 같은 순서쌍을 집어넣으려면 q=deque()하고 q.append((x,y)하든가 [] 로 감싸주든가 해야한다,
       q=deque((1,1))와  deque([1,1])는 1을 두번 삽입하는 내용이고  deque([(1,1)])는 순서쌍 (1,1) 을 삽입하는 코드이다.   
"""

